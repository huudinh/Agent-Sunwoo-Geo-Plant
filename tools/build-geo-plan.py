# -*- coding: utf-8 -*-
"""
build-geo-plan.py — Sinh file kế hoạch GEO Sunwoo 2 TAB (KPI + Công việc triển khai)
từ `data/lines.json` + `data/query-sets/*.json`.

    python tools/build-geo-plan.py --start 2027-01 --months 6
    python tools/build-geo-plan.py --start 2027-01 --months 4 --scope brand,threadlift,filler
    python tools/build-geo-plan.py --start 2027-01 --months 12 --tiers A,B,C -o out/ke-hoach.xlsx

Tham số:
  --start   YYYY-MM, tháng bắt đầu chu kỳ
  --months  số tháng (3 · 4 · 6 · 12 · bất kỳ)
  --scope   danh sách key bộ, phẩy ngăn cách; mặc định `all`
  --tiers   tầng đưa vào chu kỳ, mặc định `A,B,C` (D đẩy backlog)
  --tran    trần thẩm định bài/bác sĩ/tháng, mặc định 24 (xem geo-phuong-phap-luan §6.4)
  -o        đường dẫn file xuất

Ba điểm khác bộ Kangnam, đều có lý do:
  ① ĐỊNH TUYẾN TÊN MIỀN — cụm C08/C12/C13/C14 của MỌI bộ được chuyển về line SWM và
    tên miền trục, đúng bảng định tuyến ở knowledge/geo-luat-ba-ten-mien.md §3.
    Không làm thế thì kế hoạch sinh ra 10 trang /doctors/ trên ba tên miền.
  ② CỔNG CHẶN R4 — bộ nào thuộc line có `trang_thai = blocked` thì mọi dòng công việc
    mang nhãn [BLOCKED · R4], nền hồng, hạn chót ghi "tính từ ngày có nha sĩ".
  ③ TRẦN THẨM ĐỊNH BÁC SĨ — sản lượng PHÁT HÀNH mỗi tháng bị chặn bởi số bác sĩ ×
    `--tran`. Vượt trần thì script in cảnh báo và ghi một dòng cảnh báo vào panel.
"""
import argparse
import calendar
import json
import os
import sys
from collections import defaultdict

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

TEAL = "0E4F57"
INK = "10323A"
MINT = "DCECEE"
AMBER = "C98A2E"
GREY = "F1F5F6"
CREAM = "FFF9F0"
PINK = "F7DDDD"
WHITE = "FFFFFF"

THIN = Side(style="thin", color="B9CBCE")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

HUB_CUM = {"C08", "C12", "C13", "C14"}
PHASES = ["Setup", "Tăng tốc", "Đột phá", "Về đích"]
PHASE_WEIGHT = [0.20, 0.25, 0.30, 0.25]
UNVERIFIED = "⚠ Cần Sunwoo xác nhận"
VANH_DAI = ["V1 BGC / Taguig", "V2 Makati", "V2 Ortigas – Pasig", "V2 Mandaluyong",
            "V3 Alabang – Muntinlupa", "V3 Quezon City", "V3 Manila"]


# ─────────────────────────────── đọc nguồn ───────────────────────────────

def load(scope, tiers):
    lines = json.load(open(os.path.join(DATA, "lines.json"), encoding="utf-8"))
    line_of = {l["ma"]: l for l in lines["lines"]}
    hub_domain = lines["ten_mien_truc"]
    clusters = []
    for l in lines["lines"]:
        for key in l["bo"]:
            p = os.path.join(DATA, "query-sets", key + ".json")
            if not os.path.exists(p):
                continue
            if scope != ["all"] and key not in scope:
                continue
            s = json.load(open(p, encoding="utf-8"))
            blocked = l["trang_thai"] == "blocked"
            for c in s["cum"]:
                if c["tang"] not in tiers or c["bai"] <= 0:
                    continue
                on_hub = c["ma"] in HUB_CUM
                clusters.append(dict(
                    key=key, set_vi=s["ten_vi"], set_en=s["ten_en"],
                    src_line=l["ma"],
                    # ① ĐỊNH TUYẾN TÊN MIỀN
                    line="SWM" if on_hub else l["ma"],
                    domain=hub_domain if on_hub else s["domain"],
                    on_hub=on_hub, blocked=blocked,
                    code=c["ma"], name=c["ten_en"].replace("⭐", "").strip(),
                    name_vi=c["ten_vi"], tier=c["tang"], stage=c["gd"],
                    bai=c["bai"], core=c["bai"] if c["tang"] == "A" else 0,
                    wave=c["song"], rank=c["hang"], url=c["trang_dich"],
                ))
    return lines, line_of, clusters


# ──────────────────────────── rải cụm vào tháng ───────────────────────────

def month_labels(start, n):
    y, m = int(start[:4]), int(start[5:7])
    out = []
    for _ in range(n):
        last = calendar.monthrange(y, m)[1]
        out.append(dict(y=y, m=m, label=f"Tháng {m}",
                        header=f"THÁNG {m:02d}/{y}",
                        deadline=f"{last:02d}/{m:02d}/{y}",
                        banner=f"THÁNG {m}/{y}"))
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


def assign(clusters, n):
    """Rải cụm vào tháng theo hạn ngạch khối lượng CỦA TỪNG LINE.

    Xếp theo thứ tự ưu tiên (sóng → tầng → hạng), đổ tuần tự vào từng tháng cho tới khi
    tháng đó đầy hạn ngạch `tổng bài của line / số tháng`. Cách này giữ luật "S3/Tầng A ra
    trước" đồng thời bảo đảm sản lượng phẳng và line nào cũng có mặt ở mọi tháng.

    Riêng C14 được ép xuống tháng đầu tiên bất kể hạn ngạch — xem §6.3 quy tắc 5.
    """
    load_m = [0] * n
    by_line = defaultdict(list)
    for c in clusters:
        by_line[c["line"]].append(c)

    slices = []
    for cls in by_line.values():
        cls.sort(key=lambda c: (0 if c["code"] == "C14" else 1,
                                c["wave"], c["tier"], c["rank"], -c["bai"]))
        total = sum(c["bai"] for c in cls)
        target = [total // n + (1 if i < total % n else 0) for i in range(n)]
        m, filled = 0, 0
        for c in cls:
            remain, core_left = c["bai"], c["core"]
            while remain > 0:
                if m < n - 1 and filled >= target[m]:
                    m, filled = m + 1, 0
                room = remain if m == n - 1 else max(1, target[m] - filled)
                take = min(remain, room)
                core_take = min(core_left, round(c["core"] * take / c["bai"]))
                slices.append({**c, "month": m, "bai": take, "core": core_take,
                               "bai_total": c["bai"], "split": take != c["bai"]})
                remain -= take
                core_left -= core_take
                filled += take
                load_m[m] += take
    slices.sort(key=lambda s: (s["month"], s["line"], s["tier"], s["rank"]))
    return slices, load_m


def phase_of(i, n):
    if i == 0 or n == 1:
        return PHASES[0], PHASE_WEIGHT[0]
    seg = 1 + min(2, (i - 1) * 3 // (n - 1))
    return PHASES[seg], PHASE_WEIGHT[seg]


# ─────────────────────────────── style helper ─────────────────────────────

def put(ws, r, c, v, *, bold=False, size=10, color="14282E", fill=None,
        wrap=True, ha="left", va="center", border=True):
    cl = ws.cell(r, c, v)
    cl.font = Font(name="Arial", sz=size, b=bold, color=color)
    if fill:
        cl.fill = PatternFill("solid", fgColor=fill)
    cl.alignment = Alignment(horizontal=ha, vertical=va, wrap_text=wrap)
    if border:
        cl.border = BORDER
    return cl


def band(ws, r, c1, c2, text, fill, *, size=11, color=WHITE):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    put(ws, r, c1, text, bold=True, size=size, color=color, fill=fill, ha="center")
    for c in range(c1 + 1, c2 + 1):
        put(ws, r, c, None, fill=fill)


# ─────────────────────────────── TAB 1 — KPI ──────────────────────────────

def build_kpi(wb, months, by_line_month, lines_used, line_of, domains, total_by_month):
    ws = wb.create_sheet("BẢNG TỔNG QUAN KPI")
    n = len(months)
    C_PILLAR, C_SUB, C_ITEM, C_QTY, C_LEVEL, C_NOW = 1, 2, 3, 4, 5, 6
    C_M0 = 7
    C_TARGET = C_M0 + n
    C_W_ROW = C_TARGET + 1
    C_W_PILLAR = C_TARGET + 2
    last = C_W_PILLAR

    band(ws, 2, 1, last,
         f"BẢNG TỔNG QUAN KPI & KẾ HOẠCH GEO/SEO SUNWOO "
         f"({months[0]['header']} – {months[-1]['header']})", TEAL, size=12)

    banners = [
        (C_PILLAR, C_ITEM, "TỔNG BÀI VIẾT MỤC TIÊU",
         f"{sum(total_by_month)} bài · {n} tháng · rải theo sóng 80/20"),
        (C_QTY, C_NOW, "HẠ TẦNG 3 TÊN MIỀN & THỰC THỂ",
         "Nối ba tên miền về một thực thể · NAP · GBP · tải trang < 2s"),
        (C_M0, C_M0 + n - 1, "GEO / SEO AI SEARCH",
         "Được AI trích dẫn trên 5 nền tảng · Top từ khoá google.com.ph"),
        (C_TARGET, last, "TRAFFIC & LEAD",
         "Traffic AI theo tên miền · chuỗi lead tới KHÁCH ĐẾN KHÁM"),
    ]
    for c1, c2, title, desc in banners:
        c2 = max(c1, min(c2, last))
        band(ws, 3, c1, c2, title, TEAL, size=10)
        band(ws, 4, c1, c2, desc, GREY, size=9, color="14282E")

    hdr = ["TRỤ CỘT KPI", "", "HẠNG MỤC / CHỈ TIÊU TRỌNG TÂM", "Số lượng", "", "Hiện tại"]
    hdr += [m["header"] for m in months]
    hdr += ["ĐÍCH ĐẾN CHU KỲ (TARGET)", "TRỌNG SỐ", "TRỌNG SỐ"]
    for i, h in enumerate(hdr, start=1):
        put(ws, 6, i, h, bold=True, size=9, color=WHITE, fill=TEAL, ha="center")

    r = 7

    def pillar_block(name, weight, rows):
        nonlocal r
        start = r
        for sub, item, qty, level, now, per_month, target, w_row in rows:
            put(ws, r, C_SUB, sub, size=9)
            put(ws, r, C_ITEM, item, size=10)
            put(ws, r, C_QTY, qty, ha="center")
            put(ws, r, C_LEVEL, level, ha="center", size=9)
            put(ws, r, C_NOW, now, ha="center", size=9)
            for i in range(n):
                put(ws, r, C_M0 + i, per_month[i] if per_month else None, ha="center")
            put(ws, r, C_TARGET, target, size=9)
            put(ws, r, C_W_ROW, w_row, ha="center", size=9)
            put(ws, r, C_W_PILLAR, None)
            r += 1
        ws.merge_cells(start_row=start, start_column=C_PILLAR, end_row=r - 1, end_column=C_PILLAR)
        put(ws, start, C_PILLAR, name, bold=True, size=11, fill=GREY, ha="center")
        ws.merge_cells(start_row=start, start_column=C_W_PILLAR, end_row=r - 1, end_column=C_W_PILLAR)
        put(ws, start, C_W_PILLAR, weight, bold=True, ha="center")

    # 1 · Hạ tầng & thực thể
    pillar_block("1. Hạ tầng 3 tên miền & Thực thể", 0.10, [
        ("", "Schema thực thể nối ba tên miền (Organization · parentOrganization · sameAs)",
         None, "", UNVERIFIED, None,
         "AI trả lời ĐÚNG rằng ba tên miền là một hệ thống — đo bằng prompt kiểm tra thực thể", 0.04),
        ("", "NAP thống nhất ba tên miền · một Google Business Profile duy nhất",
         None, "", UNVERIFIED, None,
         "NAP khớp từng ký tự; mỗi bác sĩ đúng MỘT URL hồ sơ trong toàn hệ thống", 0.03),
        ("", "GA4 cross-domain + tách kênh LLM · tải trang < 2s trên 3G",
         None, "", UNVERIFIED, None,
         "Đo được traffic AI riêng từng tên miền; tải trang < 2s trên điện thoại", 0.03),
    ])

    # 2 · Sản lượng
    rows = []
    for ln in lines_used:
        per = [by_line_month[ln][i] for i in range(n)]
        l = line_of[ln]
        nhan = "  [BLOCKED · R4]" if l["trang_thai"] == "blocked" else ""
        rows.append(("", f"{l['ten_en']} — {l['ten_vi']}{nhan}", sum(per), "", "—", per,
                     ("⛔ Sản xuất đủ nhưng CHƯA PHÁT HÀNH được tới khi có nha sĩ PRC"
                      if nhan else f"Phát hành {sum(per)} bài trong chu kỳ, đúng bản đồ nội dung"),
                     round(0.20 / max(1, len(lines_used)), 3)))
    pillar_block("2. Sản lượng bài viết", 0.20, rows)

    # 3 · SEO & GEO — cắt theo TÊN MIỀN
    rows, first = [], True
    for d in domains:
        for lv in ("Top 3", "Top 5", "Top 10"):
            rows.append(("Top từ khoá google.com.ph", d, None, lv, UNVERIFIED, None,
                         "Top 3 từ khoá thương hiệu & Top 5 dịch vụ cốt lõi", 0.15 if first else ""))
            first = False
    first = True
    for d in domains:
        for lv in ("ChatGPT", "Gemini", "AI-ov", "Perplexity", "Copilot"):
            rows.append(("GEO AI Search", d, None, lv, UNVERIFIED, None,
                         "Sunwoo được AI nhắc tên — đo ẩn danh, 3 lần lấy đa số, theo xu hướng tháng",
                         0.25 if first else ""))
            first = False
    pillar_block("3. SEO & GEO AI Search", 0.40, rows)

    # 4 · Traffic — cắt theo TÊN MIỀN
    rows = []
    for i, d in enumerate(domains):
        rows.append(("google.com.ph", d, None, "", UNVERIFIED, None,
                     "Tăng organic traffic; Time-on-site > 2,5 phút", 0.08 if i == 0 else ""))
    for i, d in enumerate(domains):
        rows.append(("Traffic AI", d, None, "", UNVERIFIED, None,
                     "Phiên từ ChatGPT · Gemini · Claude · Perplexity · Copilot", 0.07 if i == 0 else ""))
    pillar_block("4. Traffic", 0.15, rows)

    # 5 · Lead & Booking
    rows = [("", f"{line_of[ln]['ten_en']}", None, "", UNVERIFIED, None,
             "Đạt tỷ lệ chuyển đổi mục tiêu của kỳ", "—") for ln in lines_used]
    rows += [("Chuỗi sau form", x, None, "", UNVERIFIED, None,
              "Đo xuyên suốt: Form/Messenger → phòng khám trả lời → đặt lịch → ĐẾN KHÁM", "—")
             for x in ("Thời gian phòng khám trả lời (trung vị)", "Số lịch hẹn đã đặt",
                       "★ KHÁCH ĐẾN KHÁM (đơn vị đo thật)")]
    pillar_block("5. Lead & Booking", 0.15, rows)

    # hai dòng trọng số
    r += 1
    put(ws, r, C_PILLAR, "TRỌNG SỐ ĐÁNH GIÁ THÁNG", bold=True, size=10, color=WHITE, fill=TEAL)
    put(ws, r, C_ITEM, "Tỷ trọng mức độ hoàn thành theo từng tháng", size=9)
    weights = [phase_of(i, n)[1] for i in range(n)]
    scale = sum(weights)
    for i in range(n):
        put(ws, r, C_M0 + i, round(weights[i] / scale, 3), ha="center")
    put(ws, r, C_TARGET, "Tổng phân bổ", bold=True, ha="center")
    put(ws, r, C_W_ROW, 1.0, bold=True, ha="center")
    r += 1
    put(ws, r, C_PILLAR, "TỔNG TRỌNG SỐ DANH MỤC", bold=True, size=10, color=WHITE, fill=TEAL)
    put(ws, r, C_ITEM, "Tổng trọng số đánh giá 5 trụ cột KPI của chu kỳ", size=9)
    for i in range(n):
        put(ws, r, C_M0 + i, phase_of(i, n)[0], ha="center", size=9)
    put(ws, r, C_TARGET, "Tổng phân bổ", bold=True, ha="center")
    put(ws, r, C_W_PILLAR, 1.0, bold=True, ha="center")

    widths = {C_PILLAR: 24, C_SUB: 22, C_ITEM: 44, C_QTY: 10, C_LEVEL: 11, C_NOW: 24,
              C_TARGET: 46, C_W_ROW: 10, C_W_PILLAR: 10}
    for c in range(C_M0, C_M0 + n):
        widths[c] = 12
    for c, wd in widths.items():
        ws.column_dimensions[get_column_letter(c)].width = wd
    ws.row_dimensions[2].height = 26
    ws.freeze_panes = "D7"
    return ws


# ──────────────────────── TAB 2 — CÔNG VIỆC TRIỂN KHAI ────────────────────

def detail_text(g):
    """Cột `Công việc chi tiết` — làm gì · cụm nào · tầng/giai đoạn · trang đích · rào nào."""
    parts = []
    for c in sorted(g, key=lambda x: (x["tier"], x["rank"])):
        qty = (f"{c['bai']}/{c['bai_total']} bài (làm tiếp ở tháng khác)"
               if c.get("split") else f"{c['bai']} bài")
        parts.append(f"{c['code']} {c['name']} (Tầng {c['tier']} · {c['stage']} · {qty} "
                     f"→ {c['url']})")
    txt = "Sản xuất theo bản đồ nội dung: " + "; ".join(parts) + \
          ". Áp 6 quy tắc trích dẫn AI (BLUF · có số · phủ 8 góc hỏi · nói cả điều bất lợi · " \
          "ngày cập nhật + BS thẩm định kèm PRC # · không nhồi từ khoá). Viết bằng English chuẩn, " \
          "⛔ không Taglish trên trang y khoa. Duyệt 2 lớp: BS đúng chuyên khoa (R4) + Pháp chế; " \
          "nhóm chạm health product nộp duyệt trước (R9)."
    if g[0]["blocked"]:
        txt = ("[BLOCKED · R4] " + txt +
               " ⛔ KHÔNG PHÁT HÀNH cho tới khi Sunwoo công bố nha sĩ có giấy phép PRC.")
    if g[0]["on_hub"]:
        txt += (" 🏠 Cụm thuộc tên miền trục — gộp với cùng cụm của các bộ khác thành MỘT trang "
                "dùng chung, ⛔ không dựng trang trùng trên tên miền dịch vụ.")
    return txt


def build_tasks(wb, months, assigned, lines_used, line_of, tran_thang):
    ws = wb.create_sheet("CÔNG VIỆC TRIỂN KHAI")
    n = len(months)
    line_code = {ln: f"KPI-{5 + i:02d}" for i, ln in enumerate(lines_used)}
    nxt = 5 + len(lines_used)
    C_AREA, C_QC, C_SEO, C_GEO, C_TRAFFIC, C_LEAD, C_LEGAL, C_DENTIST = (
        f"KPI-{nxt + k:02d}" for k in range(8))

    heads = ["Mã KPI", "Trụ cột KPI", "Hạng mục", "Tên miền", "Tháng", "CHỈ TIÊU (số bài)",
             "Trong đó CORE", "Công việc chi tiết", "Người phụ trách", "Hạn chót", "Hoàn thành"]
    for i, h in enumerate(heads, start=1):
        put(ws, 1, i, h, bold=True, size=10, color=WHITE, fill=INK, ha="center")

    by_month = defaultdict(list)
    for c in assigned:
        by_month[c["month"]].append(c)

    r = 2
    month_totals, month_published, task_rows = [], [], 0
    con_blocked = any(line_of[ln]["trang_thai"] == "blocked" for ln in lines_used)

    for i, mo in enumerate(months):
        phase, _ = phase_of(i, n)
        band(ws, r, 1, 11,
             f"════  {mo['banner']}  ·  giai đoạn {phase.upper()}  ·  "
             f"hạn chót {mo['deadline']}  ════", INK, size=11)
        r += 1

        def task(code, pillar, item, domain, qty, core, detail, owner,
                 fill=None, bold=False, deadline=None):
            nonlocal r, task_rows
            put(ws, r, 1, code, size=9, ha="center", fill=fill, bold=bold)
            put(ws, r, 2, pillar, size=9, fill=fill, bold=bold)
            put(ws, r, 3, item, size=10, fill=fill, bold=bold)
            put(ws, r, 4, domain, size=9, ha="center", fill=fill)
            put(ws, r, 5, mo["label"], size=9, ha="center", fill=fill, bold=bold)
            put(ws, r, 6, qty, ha="center", fill=fill, bold=bold)
            put(ws, r, 7, core, ha="center", fill=fill, bold=bold)
            put(ws, r, 8, detail, size=9, fill=fill)
            put(ws, r, 9, owner, size=9, ha="center", fill=fill)
            put(ws, r, 10, deadline or mo["deadline"], size=9, ha="center", fill=fill)
            put(ws, r, 11, False, ha="center", fill=fill)
            r += 1
            task_rows += 1

        setup = (i == 0)
        task("KPI-01", "1. Hạ tầng & Thực thể", "Schema thực thể nối ba tên miền", "cả ba",
             None, None,
             ("Dựng khối thực thể gốc trên tên miền trục: Organization + subOrganization, "
              "hai site dịch vụ gắn parentOrganization + sameAs đủ ba tên miền. "
              "Hồ sơ bác sĩ về MỘT URL duy nhất (L1 · L4)." if setup else
              "Rà 6 ô kiểm thực thể; chạy prompt \"Is Sunwoo Aesthetic the same company as "
              "Sunwoo Dental?\" và xử lý nếu AI còn trả lời sai"), "Team Tech/Dev")
        task("KPI-02", "1. Hạ tầng & Thực thể",
             "NAP · Google Business Profile · tải trang", "cả ba", None, None,
             ("Chuẩn hoá NAP khớp từng ký tự trên ba tên miền + GBP; chốt MỘT GBP duy nhất "
              f"({UNVERIFIED} ba tên miền có chung pháp nhân không — R3)" if setup else
              "Giữ NAP đồng bộ; đo tải trang < 2s trên 3G mô phỏng; rà trùng nội dung giữa hai tên miền (L6)"),
             "Team Tech/Dev")
        task("KPI-03", "2. Tuyến nội dung", "Quy chuẩn loại bài & checklist từ cấm", "cả ba",
             None, None,
             ("Ban hành khung loại bài + checklist từ cấm EN (guaranteed · permanent · #1 · best · "
              "cure · chê ngoại hình) cho toàn đội — R1 · R6" if setup else
              "Soát ngẫu nhiên 10% bài đã đăng theo checklist 12 ô; báo cáo vi phạm"),
             "Lead Content/SEO")
        task("KPI-04", "2. Tuyến nội dung", "Tagging theo hành trình S1–S6 × line", "cả ba",
             None, None,
             ("Thiết lập cấu trúc tag theo line × giai đoạn S1–S6 × cụm C01–C15" if setup else
              "Gắn thẻ 100% bài mới theo line × giai đoạn × cụm"), "Team Content")

        month_total = month_core = month_pub = 0
        for ln in lines_used:
            cls = [c for c in by_month[i] if c["line"] == ln]
            if not cls:
                continue
            l = line_of[ln]
            blocked_line = l["trang_thai"] == "blocked"
            groups = defaultdict(list)
            for c in cls:
                groups[c["set_vi"]].append(c)
            si = 0
            b_total = b_core = 0
            for name in sorted(groups):
                si += 1
                g = groups[name]
                bai = sum(x["bai"] for x in g)
                core = sum(x["core"] for x in g)
                b_total += bai
                b_core += core
                blocked = g[0]["blocked"]
                if not blocked:
                    month_pub += bai
                # Cụm đã định tuyến về tên miền trục phải đọc ra được là "khối thực thể",
                # nếu không người đọc tưởng bài dịch vụ bị đặt nhầm tên miền.
                hang_muc = (f"🏠 Khối trên tên miền trục — từ bộ {name}"
                            if all(x["on_hub"] for x in g) else name)
                task(f"{line_code[ln]}.{si}", f"3. Sản lượng — {l['ten_en']}", hang_muc,
                     g[0]["domain"], bai, core, detail_text(g), "Team Content",
                     fill=PINK if blocked else CREAM,
                     deadline="⛔ tính từ ngày có nha sĩ" if blocked else None)
            nhan = " [BLOCKED · R4]" if blocked_line else ""
            task(line_code[ln], f"3. Sản lượng — {l['ten_en']}",
                 f"▶ TỔNG {l['ten_en'].upper()}{nhan}", l["domain"], b_total, b_core,
                 f"Tổng sản lượng {l['ten_en']} trong tháng — cộng từ các dòng chi tiết phía trên"
                 + ("  ⛔ Toàn bộ dòng này chưa được phép phát hành (R4)" if blocked_line else ""),
                 "Lead Content", fill=PINK if blocked_line else MINT, bold=True,
                 deadline="⛔ tính từ ngày có nha sĩ" if blocked_line else None)
            month_total += b_total
            month_core += b_core

        task("KPI-TỔNG", "3. Sản lượng bài viết", "★ TỔNG SẢN LƯỢNG THÁNG (toàn hệ thống)",
             "cả ba", month_total, month_core,
             f"Con số lãnh đạo đọc. Trong đó PHÁT HÀNH được: {month_pub} bài · "
             f"bị chặn bởi R4: {month_total - month_pub} bài. "
             f"Trần thẩm định bác sĩ tháng này: {tran_thang} bài"
             + ("  ⚠️ VƯỢT TRẦN — phải giãn tiến độ hoặc bổ sung bác sĩ thẩm định"
                if month_pub > tran_thang else ""),
             "Lead Content/SEO", fill=AMBER, bold=True)
        month_totals.append(month_total)
        month_published.append(month_pub)

        a1, a2 = VANH_DAI[(i * 2) % 7], VANH_DAI[(i * 2 + 1) % 7]
        task(C_AREA, "3. Sản lượng — Trang vành đai", "Điều phối trang vành đai (không cộng sản lượng)",
             "cả ba", None, None,
             f"Tháng này đưa lên: {a1} · {a2}. Mỗi trang vành đai cần NAP chuẩn, thời gian đi thật "
             f"giờ cao điểm & thấp điểm, hướng dẫn đỗ xe, phương tiện, giờ mở cửa, liên kết sang cả "
             f"ba mảng. Số bài đã nằm trong cụm C04 ở trên — ⛔ KHÔNG cộng thêm. "
             f"⛔ Không hứa kết quả điều trị trên trang vành đai (R1)", "Team Content/SEO")
        task(C_QC, "3. Sản lượng — Kiểm duyệt", "Duyệt 2 lớp: BS đúng chuyên khoa + Pháp chế",
             "cả ba", None, None,
             "Rà checklist 12 ô; mọi bài y khoa phải có author box \"Medically reviewed by [tên], "
             "[chuyên khoa], PRC #[số]\". ⛔ Không dùng bác sĩ ngoài chuyên khoa để thẩm định (R4)",
             "BS thẩm định + Pháp chế")
        task(C_SEO, "4. SEO & GEO AI Search", "Top từ khoá google.com.ph", "cả ba", None, None,
             ("Audit từ khoá EN ba tên miền, chốt bộ theo dõi, tách theo tên miền" if setup else
              "Theo dõi Top 3/5/10 theo từng tên miền; tối ưu bài đã đăng theo khoảng cách thứ hạng"),
             "Team SEO")
        task(C_GEO, "4. SEO & GEO AI Search", "Đo GEO — 36 prompt × 5 nền tảng", "cả ba", None, None,
             ("Chạy 36 prompt ẩn danh trên ChatGPT · Gemini · AI Overview · Perplexity · Copilot, "
              "3 lần lấy đa số, KHOÁ bộ đo và lấy mốc gốc. Ghi cả đối thủ được nhắc và URL được trích"
              if setup else
              "Chạy lại bộ đo đã khoá; so xu hướng với tháng trước; xử lý mọi câu AI trích trang "
              "NGOÀI Sunwoo cho câu hỏi VỀ Sunwoo bằng cụm C14"), "Team SEO/GEO")
        task(C_TRAFFIC, "5. Traffic & Chuyển đổi", "Traffic & Time-on-site theo tên miền",
             "cả ba", None, None,
             ("Dựng GA4 cross-domain ba tên miền, tách kênh LLM, lấy mốc gốc" if setup else
              "Theo dõi organic google.com.ph + Traffic AI theo từng tên miền và từng nguồn LLM"),
             "Team Data")
        task(C_LEAD, "5. Traffic & Chuyển đổi", "Chuỗi Form/Messenger → đặt lịch → ĐẾN KHÁM",
             "cả ba", None, None,
             ("Dựng funnel 5 mắt xích; đổi trường `Your area` trên form từ ô text sang dropdown "
              "V1/V2/V3/V4 + Other. ⛔ Không gửi `Service of interest` vào pixel (R11)" if setup else
              "Đo thời gian phòng khám trả lời (trung vị); tối ưu CTA trên trang có traffic AI cao; "
              "báo cáo cắt theo vành đai V1–V4"), "Vận hành + Team Data")
        if setup:
            task(C_LEGAL, "0. Pháp lý", "Duyệt trước khi phát (FDA PH · ASC)", "cả ba", None, None,
                 "Lập danh mục nội dung bị coi là quảng cáo health product (filler · chỉ Xline · "
                 "PicoSure Pro · meso · vật liệu implant), nộp lô đầu xin duyệt trước. R9 là nút thắt "
                 "tiến độ lớn nhất — ⛔ không để sắp đăng mới nộp", "Pháp chế")
            task("KPI-00", "0. Pháp lý", "Sửa 2 lỗi cổng chặn trên trang production", "cả ba",
                 None, None,
                 "① Gỡ con số \"300++ board-certified doctors\" (site chỉ có 2 bác sĩ) — đổi sang "
                 "con số đếm được có nguồn. ② Rà FAQ nêu \"plastic surgery and wellness\": dịch vụ "
                 "nào ngoài phạm vi giấy phép thì xoá (R2 · R6). ⛔ Chưa sửa xong thì không đổ nội "
                 "dung mới lên", "Pháp chế + Team Tech/Dev")
        if con_blocked:
            task(C_DENTIST, "0. Pháp lý", "⛔ Xác minh & công bố nha sĩ có giấy phép PRC",
                 "sunwoodental.ph", None, None,
                 "CỔNG MỞ KHOÁ LINE SWD: lấy tên + số PRC + chứng chỉ chuyên khoa của ít nhất một "
                 "nha sĩ, dựng hồ sơ trên tên miền trục, gắn vào author box của mọi bài nha khoa. "
                 "Tới khi xong, toàn bộ bài nha khoa chỉ được sản xuất, ⛔ không được phát hành (R4)",
                 "HR + Pháp chế", fill=PINK)
        r += 1

    # ───────── panel phải ─────────
    band(ws, 1, 13, 14, "TỔNG SẢN LƯỢNG THEO THÁNG", AMBER)
    pr = 2
    for i, mo in enumerate(months):
        put(ws, pr, 13, f"{mo['label']} (phát hành {month_published[i]})", size=9)
        put(ws, pr, 14, month_totals[i], ha="center")
        pr += 1
    put(ws, pr, 13, "TỔNG CHU KỲ", bold=True, size=9, fill=MINT)
    put(ws, pr, 14, sum(month_totals), bold=True, ha="center", fill=MINT)
    pr += 2

    band(ws, pr, 13, 14, "TRẦN THẨM ĐỊNH BÁC SĨ", INK)
    pr += 1
    vuot = max(month_published) > tran_thang if month_published else False
    for label, val in (("Trần phát hành / tháng", tran_thang),
                       ("Tháng cao nhất (đã phát hành)", max(month_published or [0])),
                       ("Còn dư", tran_thang - max(month_published or [0])),
                       ("Trạng thái", "⚠️ VƯỢT TRẦN" if vuot else "✅ trong trần")):
        put(ws, pr, 13, label, size=9)
        put(ws, pr, 14, val, ha="center", fill=PINK if (vuot and label == "Trạng thái") else None)
        pr += 1
    pr += 1

    band(ws, pr, 13, 14, "THỐNG KÊ TIẾN ĐỘ", INK)
    pr += 1
    for label, val in (("Tổng số đầu việc KPI", task_rows), ("Đã hoàn thành", 0),
                       ("Chưa hoàn thành", task_rows), ("Tiến độ chung", 0)):
        put(ws, pr, 13, label, size=9)
        put(ws, pr, 14, val, ha="center")
        pr += 1
    pr += 1
    ws.merge_cells(start_row=pr, start_column=13, end_row=pr + 4, end_column=14)
    put(ws, pr, 13,
        "Dòng amber ★ là tổng của tháng — đọc trực tiếp ở cột CHỈ TIÊU. Dòng mint ▶ là tổng của "
        "từng line. Dòng kem là chi tiết từng bộ. DÒNG HỒNG là việc đã sản xuất nhưng CHƯA ĐƯỢC "
        "PHÉP PHÁT HÀNH — rào R4, chờ nha sĩ có giấy phép PRC.", size=9, fill=GREY)

    for c, wd in {1: 11, 2: 28, 3: 40, 4: 20, 5: 10, 6: 13, 7: 12, 8: 78, 9: 18, 10: 22,
                  11: 12, 12: 3, 13: 30, 14: 13}.items():
        ws.column_dimensions[get_column_letter(c)].width = wd
    ws.freeze_panes = "A2"
    return ws, month_published


# ─────────────────────────────────── main ─────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="YYYY-MM")
    ap.add_argument("--months", type=int, required=True)
    ap.add_argument("--scope", default="all")
    ap.add_argument("--tiers", default="A,B,C")
    ap.add_argument("--tran", type=int, default=24,
                    help="trần thẩm định bài/bác sĩ/tháng (mặc định 24)")
    ap.add_argument("-o", "--out", default=None)
    a = ap.parse_args()

    scope = [s.strip() for s in a.scope.split(",")]
    tiers = {t.strip().upper() for t in a.tiers.split(",")}
    lines, line_of, clusters = load(scope, tiers)
    if not clusters:
        sys.exit("Không có cụm nào khớp phạm vi/tầng đã chọn.")

    months = month_labels(a.start, a.months)
    assigned, load_m = assign(clusters, a.months)

    order = [l["ma"] for l in lines["lines"]]
    lines_used = [ln for ln in order if any(c["line"] == ln for c in assigned)]
    by_line_month = {ln: [0] * a.months for ln in lines_used}
    for c in assigned:
        by_line_month[c["line"]][c["month"]] += c["bai"]
    total_by_month = [sum(by_line_month[ln][i] for ln in lines_used) for i in range(a.months)]

    domains = []
    for l in lines["lines"]:
        if l["ma"] in lines_used or any(c["src_line"] == l["ma"] for c in assigned):
            if l["domain"] not in domains:
                domains.append(l["domain"])

    n_bs = sum(len(l["bac_si_tham_dinh"]) for l in lines["lines"]
               if l["vai_tro"] == "service" and l["trang_thai"] == "active")
    n_bs = n_bs or len(lines["lines"][0]["bac_si_tham_dinh"])
    tran_thang = a.tran * max(1, n_bs)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    build_kpi(wb, months, by_line_month, lines_used, line_of, domains, total_by_month)
    _, published = build_tasks(wb, months, assigned, lines_used, line_of, tran_thang)

    out = a.out or os.path.join(
        ROOT, "out",
        f"GEO-SUNWOO-T{months[0]['m']:02d}-T{months[-1]['m']:02d}-{months[-1]['y']}.xlsx")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    wb.save(out)

    print(f"OK {out}")
    print(f"   {len(assigned)} lát cụm · {sum(c['bai'] for c in assigned)} bài · "
          f"{a.months} tháng · {len(lines_used)} line · {len(domains)} tên miền")
    print("   Sản lượng theo tháng: " + " · ".join(
        f"{m['label']}={load_m[i]}(phát hành {published[i]})" for i, m in enumerate(months)))
    print(f"   Trần thẩm định: {tran_thang} bài/tháng ({n_bs} bác sĩ × {a.tran})"
          + ("  ⚠️ CÓ THÁNG VƯỢT TRẦN" if max(published) > tran_thang else "  OK"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
