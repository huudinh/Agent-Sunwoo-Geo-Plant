# -*- coding: utf-8 -*-
"""
build-botruyvan.py — Sinh bộ truy vấn GEO Sunwoo theo MẪU CHUẨN 6 SHEET.

    python tools/build-botruyvan.py                    # sinh cả 10 bộ
    python tools/build-botruyvan.py --scope threadlift # chỉ một bộ

Mẫu lấy từ `Knowledge/KN-BotruyvanGEO/mui.xlsx` (bộ Kangnam v3) — giữ nguyên trục
6 sheet, thứ tự cột và cách đọc:

    1 Hướng dẫn & Chiến lược → 2 Hành vi KH → 3 Bộ truy vấn Master
    → 4 Bản đồ nội dung → 5 Prompt đo lường → 6 Rào pháp lý

Bốn chỗ cố ý khác mẫu Kangnam, đều có lý do:
  ① Hậu tố tên sheet rút ngắn. Excel cấm tên sheet quá 31 ký tự; mẫu vừa đủ vì
    "Mũi" chỉ 3 ký tự, còn tên bộ của Sunwoo dài tới 8 ("PicoSure").
  ② Sheet 3 thêm cột TÊN MIỀN. Sunwoo chạy BA tên miền cho một phòng khám —
    một truy vấn không nói rõ trang đích nằm ở tên miền nào là một truy vấn chưa
    giao xong. Xem knowledge/geo-luat-ba-ten-mien.md §3.
  ③ Sheet 2 có BỐN rào cản (NGỜ · NGẠI · SỢ · BỀN) thay vì ba. BỀN là rào đặc thù
    của gói nội địa Philippines, không có trong bộ Việt Nam.
  ④ Sheet 5 đo trên NĂM nền tảng (thêm Perplexity · Copilot) vì thị trường PH nói
    tiếng Anh, hai công cụ này phủ nội dung tiếng Anh rộng hơn hẳn.

Nguồn dữ liệu:
  · data/lines.json          — sổ đăng ký line, trạng thái cổng chặn
  · data/query-sets/*.json   — cấp CỤM (tầng · giai đoạn · % điểm · số bài · trang đích)
  · data/truy-van/*.json     — cấp TRUY VẤN (17 dòng/cụm, tiếng Anh)
  · data/geo-prompts.json    — prompt đo GEO tiếng Anh

⚠ CƠ HỘI GEO = 1 cho MỌI cụm vì Sunwoo chưa có mốc traffic AI nào. Sau tháng Setup
đo xong mốc gốc thì phải chấm lại 1–3 và chạy lại script này.
"""
import argparse
import json
import math
import os
import sys
from collections import OrderedDict

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SRC_CUM = os.path.join(DATA, "query-sets")
SRC_TV = os.path.join(DATA, "truy-van")
OUT_DIR = os.path.join(ROOT, "doc", "BoTruyVanGEO-Sunwoo")

TV_MOI_CUM = 17

# ── bảng màu Sunwoo — khớp file kế hoạch 2 TAB của build-geo-plan.py ──────
TEAL = "0E4F57"
INK = "10323A"
MINT = "DCECEE"
AMBER = "C98A2E"
AMBER_WASH = "F8EBD4"
CREAM = "FFF9F0"
PINK = "F7DDDD"
RED = "A8162B"
WHITE = "FFFFFF"
INK_TXT = "14282E"
GREY_TXT = "7C949A"

THIN = Side(style="thin", color="B9CBCE")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

GIAI_DOAN = {
    "S1": "S1 · NHẬN BIẾT (Cold)",
    "S2": "S2 · TÌM HIỂU (Warm)",
    "S3": "S3 · CÂN NHẮC & NỖI SỢ (Warm→Hot)",
    "S4": "S4 · THỰC HIỆN (Hot)",
    "S5": "S5 · TRẢI NGHIỆM & HẬU THỦ THUẬT (Existing)",
    "S6": "S6 · GẮN BÓ & MỞ RỘNG (LTV)",
}
TANG_TEN = {
    "A": "A · CORE 80/20",
    "B": "B · Đòn bẩy chuyển đổi",
    "C": "C · Uy tín & giữ chân",
    "D": "D · Cửa vào rộng",
}
SONG_TEN = {1: "Sóng 1 · 0–30 ngày", 2: "Sóng 2 · 31–60 ngày",
            3: "Sóng 3 · 61–90 ngày", 4: "Nền · sau 90 ngày"}
DIEM_DT = {"Cao": 3, "TB": 2, "Thấp": 1}
DIEM_NHIET = {"Hot": 3, "Warm": 2, "Existing": 2, "Cold": 1}
DIEM_UT = {"P1": 3, "P2": 2, "P3": 1}
CO_HOI_GEO = 1  # Sunwoo chưa có mốc traffic AI — xem docstring

# Tên sheet Excel ≤31 ký tự. Sheet dài nhất "3. <ten>- Bo truy van Master" = 23 + len.
TEN_NGAN = {
    "brand": "Brand", "mesohair": "MesoHair", "filler": "Filler",
    "threadlift": "Xline", "acne": "Acne", "picosure": "PicoSure",
    "implant": "Implant", "veneers": "Veneers", "wisdom": "Wisdom",
    "generaldentistry": "GenDent",
}

NEN_TANG = ["ChatGPT", "Gemini", "AI Overview", "Perplexity", "Copilot"]

# Từ khoá ĐẶC TRƯNG của từng bộ — dùng để lọc prompt cấp line ở sheet 5.
# ⛔ Không tách từ `svc_en`: "Advanced Acne Treatment" cho ra "treatment", một từ
# chung chung khớp luôn cả prompt của bộ khác.
TU_KHOA_BO = {
    "brand": [],
    "mesohair": ["meso", "hair"],
    "filler": ["filler", "collagen", "booster"],
    "threadlift": ["thread lift", "xline"],
    "acne": ["acne"],
    "picosure": ["picosure", "melasma", "pigmentation"],
    "implant": ["implant"],
    "veneers": ["veneer", "porcelain", "crown"],
    "wisdom": ["wisdom tooth", "extraction", "dry socket"],
    "generaldentistry": ["dental", "dentist", "cleaning", "check-up"],
}

PCT = "0%"      # khớp mẫu Kangnam: cột % ĐIỂM của sheet 2 và 4
PCT1 = "0.0%"   # khớp mẫu Kangnam: cột % ĐIỂM / % LŨY KẾ của sheet 3

# ── 12 rào pháp lý bản Philippines (khớp knowledge/geo-rao-phap-ly-ph.md) ──
RAO_BANG = [
    ("R0", "Thấp — nội dung kiến thức",
     "CTA bán hàng dồn dập trong bài kiến thức",
     "Giữ giọng giáo dục; CTA mềm cuối bài; vẫn ghi ngày cập nhật + bác sĩ thẩm định",
     "Content lead"),
    ("R1", "Cam kết kết quả",
     "guaranteed · 100% · permanent · forever · lifetime · no side effects · painless · "
     "zero risk — gồm cả “written guarantee” đang có trên trang",
     "“Results vary with skin condition, age and treatment plan”; bảo đảm QUY TRÌNH "
     "(số buổi, chính sách làm lại) có T&C văn bản",
     "Pháp chế"),
    ("R2", "Phạm vi giấy phép cơ sở (DOH)",
     "Quảng cáo dịch vụ cơ sở không được cấp phép. ⚠ FAQ hiện nêu plastic surgery và wellness",
     "Chỉ nêu dịch vụ trong phạm vi đã cấp phép; chưa chắc thì xoá khỏi site",
     "Pháp chế + DOH"),
    ("R3", "Đúng pháp nhân & đúng tên miền",
     "Ba tên miền nói như ba công ty; một tên miền dẫn khách sang dịch vụ của pháp nhân khác",
     "Mỗi tên miền ghi đúng pháp nhân vận hành; schema parentOrganization thống nhất",
     "Pháp chế"),
    ("R4", "Bác sĩ & giấy phép PRC",
     "Gắn bác sĩ vào dịch vụ ngoài chuyên khoa. ⛔ Dùng bác sĩ da liễu thẩm định bài nha khoa",
     "Bác sĩ đã xác minh chuyên khoa + PRC còn hiệu lực; author box “Medically reviewed "
     "by [tên], [chuyên khoa], PRC #…”",
     "Chuyên môn + HR"),
    ("R5", "Ảnh trước/sau & lời chứng thực",
     "Ảnh khách khi mới có thoả thuận miệng; bác sĩ chứng thực kết quả lâm sàng",
     "Văn bản đồng ý minh thị; ảnh cùng góc – cùng sáng – không filter; miễn trừ "
     "“Individual results may vary” in trên ảnh",
     "CSKH + Pháp chế"),
    ("R6", "So sánh đối thủ & tuyên bố tối cao (ASC)",
     "#1 · best in the Philippines · most advanced · leading; nêu tên hạ thấp cơ sở khác",
     "Bộ tiêu chí khách quan để khách tự chấm; định vị không so thứ bậc",
     "Pháp chế (ASC)"),
    ("R7", "Thiết bị & health product (FDA RA 9711)",
     "Nêu thiết bị/sản phẩm chưa đăng ký; nêu công dụng ngoài nhãn đã duyệt",
     "Chỉ nêu đúng tên đã đăng ký, kèm số đăng ký FDA PH",
     "Pháp chế + FDA"),
    ("R8", "Khách nước ngoài & đa ngôn ngữ",
     "Mở nội dung tiếng Hàn khi không có nhân sự nói tiếng Hàn tiếp nhận",
     "Đủ điều kiện ngôn ngữ + văn bản đồng ý song ngữ rồi mới mở nhóm N1",
     "Pháp chế + Vận hành"),
    ("R9", "DUYỆT TRƯỚC KHI PHÁT (FDA PH · ASC)",
     "Phát hành nội dung được coi là quảng cáo health product mà chưa qua duyệt",
     "Lập danh mục nội dung cần duyệt trước ngay tháng Setup, nộp theo lô",
     "Pháp chế"),
    ("R10", "KOL / người chuyển tải",
     "KOL nói về dịch vụ mà không công khai là quảng cáo",
     "Công khai #ad; ràng buộc trách nhiệm trong hợp đồng",
     "Brand + Pháp chế"),
    ("R11", "Dữ liệu cá nhân & nhạy cảm (RA 10173)",
     "⛔ Gửi trường “Service of interest” vào pixel quảng cáo; form thiếu mục đích, "
     "thời gian lưu, cách rút đồng ý",
     "Đồng ý tách riêng cho dữ liệu nhạy cảm; pixel chỉ gửi sự kiện Lead không kèm "
     "tham số dịch vụ",
     "Pháp chế (NPC)"),
]
RAO_NONG = ("R1", "R4", "R7", "R9")

SAU_QUY_TAC = [
    "① BLUF — câu đầu tiên của mỗi mục PHẢI là câu trả lời đứng độc lập, hiểu được khi tách "
    "khỏi ngữ cảnh. AI trích theo ĐOẠN, không trích theo bài.",
    "② CÓ SỐ — nội dung có số liệu được hiển thị trong câu trả lời AI cao hơn 30–40%. "
    "“Swelling settles in about 70% of patients by day 10” thắng “swelling goes down quickly”.",
    "③ PHỦ 8 GÓC HỎI cho mỗi chủ đề: định nghĩa · so sánh · hướng dẫn · trường hợp áp dụng · "
    "phản đối/rủi ro · thực thể liên quan · chi phí/chỉ số · địa phương.",
    "④ DÁM NÓI ĐIỀU BẤT LỢI — “Veneers require permanent enamel reduction; this cannot be "
    "reversed.” Nội dung cân bằng được AI trích nhiều hơn hẳn nội dung một chiều.",
    "⑤ GHI NGÀY CẬP NHẬT + BÁC SĨ THẨM ĐỊNH KÈM SỐ PRC trên mọi bài y khoa (schema Physician). "
    "Ở PH đây vừa là tín hiệu E-E-A-T vừa là yêu cầu pháp lý (R4).",
    "⑥ KHÔNG NHỒI TỪ KHOÁ — nhồi từ khoá cho kết quả THẤP HƠN mức nền trong AI search. "
    "Viết như đang trả lời một người thật đang lo.",
    "⑦ NGÔN NGỮ — nội dung trên site viết bằng English chuẩn, câu ngắn. ⛔ KHÔNG Taglish trên "
    "trang y khoa, trong tên dịch vụ, câu miễn trừ hay thông tin giá.",
]


# ─────────────────────────── helper định dạng ────────────────────────────

def put(ws, r, c, v, *, bold=False, size=10, color=INK_TXT, fill=None,
        wrap=True, ha="left", va="top", border=True, italic=False, fmt=None):
    cl = ws.cell(r, c, v)
    cl.font = Font(name="Arial", sz=size, b=bold, i=italic, color=color)
    if fill:
        cl.fill = PatternFill("solid", fgColor=fill)
    cl.alignment = Alignment(horizontal=ha, vertical=va, wrap_text=wrap)
    if border:
        cl.border = BORDER
    if fmt:
        # Mẫu Kangnam để cột % ở number_format '0%' / '0.0%'. Thiếu dòng này thì
        # Excel hiện 0.13 ở cột tên là "% ĐIỂM" — đúng số nhưng sai mặt chữ.
        cl.number_format = fmt
    return cl


def band(ws, r, c1, c2, text, fill, *, size=11, color=WHITE, h=None):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    put(ws, r, c1, text, bold=True, size=size, color=color, fill=fill,
        ha="left", va="center")
    for c in range(c1 + 1, c2 + 1):
        put(ws, r, c, None, fill=fill)
    if h:
        ws.row_dimensions[r].height = h


def header_row(ws, r, labels, start=1):
    for i, h in enumerate(labels, start=start):
        put(ws, r, i, h, bold=True, size=9, color=WHITE, fill=TEAL,
            ha="center", va="center")
    ws.row_dimensions[r].height = 30


def dong(ws, r, c1, c2, text, *, size=9.5, fill=None, h=28):
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    put(ws, r, c1, text, size=size, fill=fill)
    for c in range(c1 + 1, c2 + 1):
        put(ws, r, c, None, fill=fill)
    ws.row_dimensions[r].height = h


def ghi_chu(ws, r, c1, c2, text, *, size=9, italic=True, color=INK_TXT, fill=None):
    """Dòng mô tả dưới tiêu đề: GỘP ngang bảng rồi tự tính chiều cao cho vừa chữ.

    ⛔ Không dùng put() trần cho chữ dài: nó rơi vào cột A (rộng 6–10 ký tự ở sheet
    3–6), wrap_text bật, chiều cao mặc định 15pt → Excel cắt mất gần hết câu.
    """
    rong_cot = 0.0
    for c in range(c1, c2 + 1):
        d = ws.column_dimensions.get(get_column_letter(c))
        rong_cot += (d.width if d and d.width else 8.43)
    ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    put(ws, r, c1, text, size=size, italic=italic, color=color, fill=fill, va="center")
    for c in range(c1 + 1, c2 + 1):
        put(ws, r, c, None, fill=fill)
    dong_can = max(1, math.ceil(len(text) / max(rong_cot - 2, 10)))
    ws.row_dimensions[r].height = max(16, round(dong_can * size * 1.42) + 4)


def widths(ws, spec):
    for c, w in spec.items():
        ws.column_dimensions[get_column_letter(c)].width = w


# ───────────────────────────── đọc nguồn ─────────────────────────────────

def load(scope):
    lines = json.load(open(os.path.join(DATA, "lines.json"), encoding="utf-8"))
    line_of = {l["ma"]: l for l in lines["lines"]}
    prompts = json.load(open(os.path.join(DATA, "geo-prompts.json"), encoding="utf-8"))
    out = []
    for l in lines["lines"]:
        for key in l["bo"]:
            p = os.path.join(SRC_CUM, key + ".json")
            if not os.path.exists(p):
                continue
            if scope != ["all"] and key not in scope:
                continue
            d = json.load(open(p, encoding="utf-8"))
            tv = os.path.join(SRC_TV, key + ".json")
            d["_tv"] = json.load(open(tv, encoding="utf-8")) if os.path.exists(tv) else None
            d["_line"] = l
            d["_hub"] = lines["ten_mien_truc"]
            d["_coso"] = lines["co_so"]
            out.append(d)
    return out, line_of, prompts


def rows_of(d):
    """Làm phẳng thành 255 dòng truy vấn, giữ nguyên thứ tự hạng cụm."""
    tv = d["_tv"] or {}
    kho = tv.get("truy_van", {})
    rows = []
    for cum in sorted(d["cum"], key=lambda c: c["hang"]):
        ma = cum["ma"]
        ds = kho.get(ma, [])
        for i in range(TV_MOI_CUM):
            q = ds[i] if i < len(ds) else {}
            nhiet = q.get("n", "Warm")
            ut = q.get("u", "P2")
            dt = q.get("v", "TB")
            rows.append(dict(
                id=f"{ma}-{i+1:02d}", ma=ma, cum=cum, stt=i + 1,
                truy_van=q.get("q", ""), goc=q.get("g", ""),
                nhiet=nhiet, ut=ut, dt=dt,
                tu_khoa=q.get("k", ""), khoi=q.get("b", ""),
                trang=q.get("d") or cum["trang_dich"],
                rao=q.get("r", "R0"),
                doi_tuong=q.get("t", "Chung"),
                # tên miền suy từ bảng định tuyến: cụm 🏠 luôn nằm trên tên miền trục
                domain=d["_hub"] if cum.get("tren_hub") else d["domain"],
                diem=DIEM_DT.get(dt, 2) * DIEM_NHIET.get(nhiet, 2)
                     * DIEM_UT.get(ut, 2) * CO_HOI_GEO,
                core=i < cum["core"],
            ))
    k = 0
    for row in sorted([r for r in rows if r["core"]],
                      key=lambda r: (-r["diem"], r["cum"]["hang"], r["stt"])):
        k += 1
        row["thu_tu"] = k
    return rows


def bi_chan(d):
    return d["_line"]["trang_thai"] == "blocked"


# ───────────────────────────── SHEET 1 ───────────────────────────────────

def sheet1(wb, d, rows):
    ws = wb.create_sheet(f"1. {d['ten_ngan']}- Huong dan")
    q = d["quy_mo"]
    bai = sum(c["bai"] for c in d["cum"])
    band(ws, 1, 1, 6, f"{d['ten_vi'].upper()} — HƯỚNG DẪN & CHIẾN LƯỢC  |  "
                      f"Bộ truy vấn GEO · Sunwoo Medical Center", INK, size=12, h=26)
    ghi_chu(ws, 2, 1, 6,
            f"Tối ưu để ChatGPT · Gemini · Google AI Overview · Perplexity · Copilot "
            f"TRÍCH DẪN Sunwoo — không phải để lên top từ khoá Google. "
            f"Tên miền của bộ này: {d['domain']}")

    r = 3
    if bi_chan(d):
        r += 1
        band(ws, r, 1, 6, "⛔ LINE NÀY ĐANG BỊ CHẶN — ĐỌC TRƯỚC KHI GIAO VIỆC", RED)
        r += 1
        dong(ws, r, 1, 6, d["_line"]["cong_chan"], fill=PINK, h=44)
        r += 1
        dong(ws, r, 1, 6, "Hệ quả: toàn bộ truy vấn trong file này VẪN sản xuất được nội dung, "
                          "nhưng ⛔ KHÔNG PHÁT HÀNH được. Hạn chót tính từ ngày Sunwoo công bố "
                          "nha sĩ có giấy phép PRC, không tính từ hôm nay.", fill=PINK, h=30)

    r += 2
    band(ws, r, 1, 6, "1 · INSIGHT CHIẾN LƯỢC — VÌ SAO BỘ NÀY KHÁC BỘ TỪ KHOÁ SEO", TEAL)
    for t in [
        "• Truy vấn vào AI dài gấp ~6 lần truy vấn Google (≈23 từ so với 3–4 từ) — khách gõ "
        "nguyên một câu chuyện.",
        "• AI “bung” (query fan-out) một câu hỏi thành 8–20 truy vấn con rồi mới tổng hợp. "
        "Chỉ 32% trích dẫn đến từ trang top 10 Google — 68% đến từ trang ngoài top 10 nhưng "
        "khớp đúng một truy vấn con.",
        "• 88% thương hiệu KHÔNG được AI trích dẫn nếu chỉ tối ưu SEO truyền thống. Thương hiệu "
        "phủ được >80% không gian chủ đề giữ được ~85% mức hiển thị trong AI.",
        "• Rào cản chốt của khách Philippines là NGỜ · NGẠI · SỢ · BỀN. ⚠ BỀN (“hết tác dụng "
        "rồi tôi trả tiếp bao nhiêu”) là rào ĐẶC THÙ của gói nội địa — gần như không đối thủ "
        "nào dám viết thẳng, nên đây là khoảng trống rẻ nhất để chiếm.",
        "• ⚠ Sunwoo chạy BA TÊN MIỀN cho MỘT phòng khám. GEO giải thực thể, nên ba tên miền "
        "không nối với nhau = uy tín không cộng dồn và hồ sơ bác sĩ bị tách đôi. Cột TÊN MIỀN "
        "ở sheet 3 là cột bắt buộc, không phải cột tham khảo.",
        "• ⚠ Sunwoo CHƯA có mốc traffic AI nào → CƠ HỘI GEO của mọi cụm tạm lấy = 1. Sau tháng "
        "Setup đo xong mốc gốc phải chấm lại 1–3 và chạy lại script.",
    ]:
        r += 1
        dong(ws, r, 1, 6, t)

    r += 2
    band(ws, r, 1, 6, "2 · KẾT LUẬN 80/20 — TẦNG ƯU TIÊN & PHÂN BỔ NGUỒN LỰC", TEAL)
    r += 1
    header_row(ws, r, ["Tầng", "Số cụm", "Số truy vấn", "% truy vấn",
                       "% điểm ưu tiên", "Phân bổ ngân sách nội dung & danh sách cụm"])
    tong_tv = q["truy_van"]
    for t in d["tang"]:
        r += 1
        put(ws, r, 1, TANG_TEN[t["tang"]], bold=True,
            fill=AMBER_WASH if t["tang"] == "A" else CREAM)
        put(ws, r, 2, t["cum"], ha="center")
        put(ws, r, 3, t["tv"], ha="center")
        put(ws, r, 4, round(t["tv"] / tong_tv, 4), ha="center", fmt=PCT)
        put(ws, r, 5, t["pct"] / 100, ha="center", fmt=PCT)
        put(ws, r, 6, t["phan_bo"], size=9)
        ws.row_dimensions[r].height = 50
    r += 1
    put(ws, r, 1, f"Riêng {q['core']} truy vấn CORE 80/20", bold=True, fill=AMBER_WASH)
    put(ws, r, 2, "—", ha="center")
    put(ws, r, 3, q["core"], ha="center")
    put(ws, r, 4, round(q["core"] / tong_tv, 4), ha="center", fmt=PCT)
    put(ws, r, 5, q["pct_diem_core"] / 100, ha="center", fmt=PCT)
    put(ws, r, 6, "Danh sách giao việc 90 ngày: lọc sheet 3 cột NHÓM 80/20 = CORE 80/20, "
                  "sắp theo cột THỨ TỰ TRIỂN KHAI.", size=9)
    ws.row_dimensions[r].height = 28

    r += 2
    band(ws, r, 1, 6, "3 · THEO NHÓM ĐỐI TƯỢNG (tự đếm từ cột ĐỐI TƯỢNG của sheet 3)", TEAL)
    r += 1
    header_row(ws, r, ["Nhóm đối tượng", "Số truy vấn", "CORE", "% truy vấn",
                       "Điểm", "Mô tả / lưu ý"])
    nhom = OrderedDict()
    for row in rows:
        k = row["doi_tuong"] or "Chung"
        nhom.setdefault(k, {"tv": 0, "core": 0, "diem": 0})
        nhom[k]["tv"] += 1
        nhom[k]["core"] += 1 if row["core"] else 0
        nhom[k]["diem"] += row["diem"]
    mota = ((d["_tv"] or {}).get("mo_ta_doi_tuong") or {})
    mota_ma = {v: mota.get(k, "") for k, v in
               ((d["_tv"] or {}).get("doi_tuong_md") or {}).items()}
    for k, v in sorted(nhom.items(), key=lambda x: -x[1]["diem"]):
        r += 1
        put(ws, r, 1, k, bold=True)
        put(ws, r, 2, v["tv"], ha="center")
        put(ws, r, 3, v["core"], ha="center")
        put(ws, r, 4, round(v["tv"] / len(rows), 4), ha="center", fmt=PCT)
        put(ws, r, 5, v["diem"], ha="center")
        put(ws, r, 6, mota_ma.get(k, ""), size=9)

    r += 2
    band(ws, r, 1, 6, "4 · ĐỊNH TUYẾN TÊN MIỀN — bài nào sống ở đâu (ràng buộc riêng của Sunwoo)",
         TEAL)
    r += 1
    header_row(ws, r, ["Nhóm cụm", "Tên miền", "Số cụm", "Số TV", "Số bài", "Vì sao"])
    hub_cum = [c for c in d["cum"] if c.get("tren_hub")]
    svc_cum = [c for c in d["cum"] if not c.get("tren_hub")]
    for ten, ds, dom, vs in [
        ("🏠 C08 · C12 · C13 · C14", hub_cum, d["_hub"],
         "Bằng chứng về CON NGƯỜI, GIẤY PHÉP và CƠ SỞ — không thuộc riêng mảng nào. "
         "Gộp với cùng cụm của các bộ khác thành MỘT trang dùng chung; ⛔ không dựng hai "
         "trang /doctors/ trên hai tên miền."),
        ("Các cụm còn lại", svc_cum, d["domain"],
         "Nội dung chuyên môn của mảng. Mỗi trang dịch vụ phải có khối liên kết ngược về "
         "/about/ và /doctors/ trên tên miền trục (luật L7)."),
    ]:
        r += 1
        f = AMBER_WASH if ds is hub_cum else CREAM
        put(ws, r, 1, ten, bold=True, fill=f)
        put(ws, r, 2, dom, size=9, fill=f)
        put(ws, r, 3, len(ds), ha="center", fill=f)
        put(ws, r, 4, len(ds) * TV_MOI_CUM, ha="center", fill=f)
        put(ws, r, 5, sum(c["bai"] for c in ds), ha="center", fill=f, bold=True)
        put(ws, r, 6, vs, size=9, fill=f)
        ws.row_dimensions[r].height = 50

    r += 2
    band(ws, r, 1, 6, "5 · CÁCH DÙNG 6 SHEET (Đối tượng → Hành trình → Truy vấn → "
                      "Nội dung → Đo lường → Pháp lý)", TEAL)
    r += 1
    header_row(ws, r, ["Sheet", "Dùng để", "Ai dùng", "", "", "Cách dùng nhanh"])
    for a, b, c, e in [
        ("1. Hướng dẫn", "Quyết định & phân bổ", "Leader",
         "Duyệt tầng ưu tiên (mục 2), trọng tâm nhóm đối tượng (mục 3) và định tuyến tên miền (mục 4)."),
        ("2. Hành vi KH", "Thấu hiểu đối tượng theo 6 giai đoạn", "Content · Tư vấn · Sale",
         "Đọc TRƯỚC khi viết. S3 ★★★ là điểm quyết định; mỗi giai đoạn một rào cản khác nhau."),
        ("3. Bộ truy vấn Master", "Nguồn sự thật + khuyến nghị 80/20", "SEO · Content",
         "Lọc NHÓM 80/20 = CORE để giao việc 90 ngày; lọc TÊN MIỀN để biết bài sống ở đâu."),
        ("4. Bản đồ nội dung", "Cụm → dạng bài → trang đích → sóng → phụ trách", "Manager",
         "Xếp theo hạng 80/20; cập nhật cột Trạng thái hằng tuần."),
        ("5. Prompt đo lường", "KPI Share of Voice trong AI", "SEO lead",
         "Chạy hằng tháng ẩn danh trên 5 nền tảng, 3 lần lấy đa số; nhân bản sheet mỗi tháng."),
        ("6. Rào pháp lý PH", "Soát trước khi đăng", "Pháp chế · Content",
         "Mỗi truy vấn có mã R0–R11; bảng tự đếm số truy vấn chịu từng rào."),
    ]:
        r += 1
        put(ws, r, 1, a, bold=True)
        put(ws, r, 2, b, size=9)
        put(ws, r, 3, c, size=9)
        put(ws, r, 6, e, size=9)
        # Cột B và C hẹp: chiều cao phải tính theo ô dài nhất, không đặt cứng.
        ws.row_dimensions[r].height = max(
            34, round(max(math.ceil(len(b) / 10), math.ceil(len(c) / 11)) * 12.6) + 4)

    r += 2
    band(ws, r, 1, 6, "6 · BẢY QUY TẮC VIẾT ĐỂ ĐƯỢC AI TRÍCH DẪN (bắt buộc với mọi bài)", TEAL)
    for t in SAU_QUY_TAC:
        r += 1
        dong(ws, r, 1, 6, t)

    r += 2
    band(ws, r, 1, 6, "7 · CẢNH BÁO — ĐỌC TRƯỚC KHI TRIỂN KHAI", RED)
    canh_bao = [
        "• Mọi nội dung y khoa phải qua BA CỬA: Content soạn → tự kiểm checklist R0–R11 → "
        "BÁC SĨ ĐÚNG CHUYÊN KHOA thẩm định (R4) → Pháp chế duyệt → (nếu là quảng cáo health "
        "product) DUYỆT TRƯỚC tại FDA PH · ASC (R9) → phát hành → lưu hồ sơ.",
        "• ⛔ Tuyệt đối không dùng: guaranteed · 100% · permanent · forever · lifetime · "
        "no side effects · painless · zero risk (R1). “Written guarantee” trên trang production "
        "thuộc nhóm này.",
        "• ⛔ Không tuyên bố #1 · best · most advanced · leading khi thiếu bằng chứng theo "
        "chuẩn ASC (R6). Câu “#1 K-beauty” đang nằm trên trang production phải gỡ.",
        "• ⛔ Không nêu thiết bị/sản phẩm sai tên đã đăng ký FDA PH — PicoSure Pro · filler · "
        "chỉ Xline · trụ implant đều là health product (R7).",
        "• ⛔ Không chê ngoại hình người đọc. Chuyển mọi câu “Are you struggling with…” thành "
        "câu trần thuật về dịch vụ.",
        "• ⛔ Không gửi trường “Service of interest” vào pixel quảng cáo — đó là dữ liệu sức "
        "khoẻ theo RA 10173 (R11).",
        "• ⚠ Hai lỗi cổng chặn trên trang production phải sửa TRƯỚC khi đổ nội dung mới: con số "
        "“300++ board-certified doctors” (site chỉ có 2 bác sĩ) và FAQ nêu “plastic surgery and "
        "wellness” ngoài phạm vi giấy phép.",
        "• ⚠ Trần thẩm định: Sunwoo công bố HAI bác sĩ. Mặc định quy hoạch ≤24 bài/bác sĩ/tháng "
        "→ 48 bài/tháng. Vượt trần thì giãn tiến độ, ⛔ không im lặng nhận chỉ tiêu.",
    ]
    for t in canh_bao:
        r += 1
        dong(ws, r, 1, 6, t, fill=PINK, h=30)

    r += 2
    band(ws, r, 1, 6, "8 · BẢNG ĐẾM TỰ ĐỘNG (tính từ sheet 3 — chạy lại script là cập nhật)", TEAL)
    r += 1
    header_row(ws, r, ["Chỉ số", "Số lượng", "% bộ", "", "", ""])
    tv_all = len(rows)

    def dem(label, n_, nhan=False):
        nonlocal r
        r += 1
        f = AMBER_WASH if nhan else None
        put(ws, r, 1, label, bold=nhan, fill=f)
        put(ws, r, 2, n_, ha="center", bold=nhan, fill=f)
        put(ws, r, 3, round(n_ / tv_all, 4), ha="center", fill=f, fmt=PCT)
        ws.row_dimensions[r].height = max(16, round(math.ceil(len(label) / 44) * 13) + 4)

    dem("Tổng số truy vấn", tv_all, True)
    for ut in ("P1", "P2", "P3"):
        dem(f"Ưu tiên {ut}", sum(1 for x in rows if x["ut"] == ut))
    for nh, nhan in (("Hot", "Truy vấn HOT (sát chuyển đổi)"), ("Warm", "Truy vấn WARM"),
                     ("Existing", "Truy vấn EXISTING"), ("Cold", "Truy vấn COLD")):
        dem(nhan, sum(1 for x in rows if x["nhiet"] == nh))
    dem("NHÓM CORE 80/20", sum(1 for x in rows if x["core"]), True)
    for gd in ("S1", "S2", "S3", "S4", "S5", "S6"):
        dem(GIAI_DOAN[gd], sum(1 for x in rows if x["cum"]["gd"] == gd), gd == "S3")
    dem(f"🏠 Truy vấn thuộc tên miền trục ({d['_hub']})",
        sum(1 for x in rows if x["domain"] == d["_hub"]), True)
    dem("Tổng số bài cần sản xuất", bai, True)

    r += 2
    band(ws, r, 1, 6, "9 · NGUỒN & GHI CHÚ CẤU TRÚC", TEAL)
    for t in [
        "— Cấu trúc chuẩn: Knowledge/KN-BotruyvanGEO/mui.xlsx (bộ Kangnam v3). File này sinh "
        "tự động bằng tools/build-botruyvan.py, bám đúng trục 6 sheet và thứ tự cột của mẫu.",
        "— ⚠ Bốn chỗ cố ý khác mẫu: (a) hậu tố tên sheet rút ngắn vì Excel cấm tên sheet quá 31 "
        "ký tự; (b) sheet 3 THÊM CỘT TÊN MIỀN vì Sunwoo chạy ba tên miền; (c) sheet 2 có BỐN rào "
        "cản thay vì ba — thêm rào BỀN đặc thù gói nội địa PH; (d) sheet 5 đo trên NĂM nền tảng.",
        "— ⚠ CƠ HỘI GEO = 1 cho mọi cụm vì Sunwoo chưa có mốc traffic AI nào. Mẫu Kangnam chấm "
        "được 1–3 nhờ có GA4 thật. Sau tháng Setup đo xong mốc gốc thì phải chấm lại và chạy "
        "lại script.",
        "— ⚠ Truy vấn trong file này là BẢN NHÁP v1 — mẫu câu suy từ khung 15 cụm, CHƯA đối "
        "chiếu dữ liệu tìm kiếm thật của Philippines. Sau tháng Setup phải soát lại bằng số "
        "liệu Google Search Console + kết quả bộ đo GEO.",
        "— Query fan-out: AI bung một câu hỏi thành 8–20 truy vấn con; 68% trang được trích nằm "
        "ngoài top 10 Google. Nội dung có số liệu tăng 30–40% khả năng hiển thị; nhồi từ khoá "
        "cho kết quả dưới mức nền.",
        "— Nội bộ: geo-phuong-phap-luan.md · geo-luat-ba-ten-mien.md · geo-bo-truy-van-index.md "
        "· sunwoo-brand-geo.md · geo-kpi-framework.md · geo-output-excel-schema.md · "
        "geo-rao-phap-ly-ph.md",
    ]:
        r += 1
        dong(ws, r, 1, 6, t, size=9, h=32)

    widths(ws, {1: 46, 2: 22, 3: 24, 4: 20, 5: 14, 6: 84})
    ws.freeze_panes = "A4"


# ───────────────────────────── SHEET 2 ───────────────────────────────────

def sheet2(wb, d, rows):
    ws = wb.create_sheet(f"2. {d['ten_ngan']}- Hanh vi KH")
    band(ws, 1, 1, 11, f"{d['ten_vi'].upper()} — THẤU HIỂU HÀNH VI KHÁCH HÀNG · "
                       f"6 GIAI ĐOẠN HÀNH TRÌNH", INK, size=12, h=26)
    ghi_chu(ws, 2, 1, 11,
            "Dùng để brief content, huấn luyện tư vấn viên và viết kịch bản Messenger. "
            "Mỗi giai đoạn một RÀO CẢN khác nhau — trả lời sai rào cản thì mất khách dù "
            "tay nghề tốt.")
    ghi_chu(ws, 3, 1, 11,
            "Cột SỐ TV · CORE · % ĐIỂM đếm từ sheet 3. S3 là điểm quyết định "
            "(~50–60% điểm ưu tiên) — luôn xuất bản S3 trước S1.")
    header_row(ws, 4, ["GIAI ĐOẠN", "ƯU TIÊN", "KHÁCH ĐANG NGHĨ GÌ (EN)", "RÀO CẢN CHI PHỐI",
                       "SUNWOO PHẢI CÓ GÌ", "CỤM TRUY VẤN", "SỐ TV", "CORE", "% ĐIỂM",
                       "TÊN MIỀN CHÍNH", "GHI CHÚ"])
    nghi = {
        "S1": "“Something is off but I do not know what it is called.”",
        "S2": "“How many options are there? Which one fits me?”",
        "S3": "“Is it safe? How much? Who is actually doing it?”",
        "S4": "“How many sessions? Can I go back to work after?”",
        "S5": "“Is this swelling normal?”",
        "S6": "“It is wearing off — do I pay again forever?”",
    }
    phai_co = {
        "S1": "Nội dung định danh vấn đề, ⛔ không bán hàng, ⛔ không chê ngoại hình người đọc.",
        "S2": "Bảng so sánh trung thực, nêu cả nhược điểm và trường hợp KHÔNG nên làm.",
        "S3": "Rủi ro nói thật có số · bảng giá công khai dải min–max · cách tự kiểm tra PRC · "
              "case thật có văn bản đồng ý.",
        "S4": "Quy trình từng bước có mốc thời gian; giờ mở cửa và đường đi thật.",
        "S5": "Cẩm nang hậu thủ thuật theo mốc giờ/ngày + dấu hiệu đỏ + kênh 24/7.",
        "S6": "Chu kỳ duy trì nói thật bằng mốc tháng và chi phí dặm lại — trả lời rào BỀN.",
    }
    r = 4
    for h in d["hanh_trinh"]:
        r += 1
        fill = AMBER_WASH if h["gd"] == "S3" else (CREAM if r % 2 else None)
        cum_gd = [c for c in d["cum"] if c["gd"] == h["gd"]]
        hub = sum(1 for c in cum_gd if c.get("tren_hub"))
        put(ws, r, 1, GIAI_DOAN[h["gd"]], bold=True, fill=fill)
        put(ws, r, 2, h["uu_tien"], ha="center", fill=fill)
        put(ws, r, 3, nghi[h["gd"]], size=9, fill=fill)
        put(ws, r, 4, h["noi_so"], size=9, fill=fill)
        put(ws, r, 5, phai_co[h["gd"]], size=9, fill=fill)
        put(ws, r, 6, h["cum"], size=9, fill=fill)
        put(ws, r, 7, h["tv"], ha="center", fill=fill)
        put(ws, r, 8, h["core"], ha="center", fill=fill)
        put(ws, r, 9, h["pct"] / 100, ha="center", fill=fill, fmt=PCT)
        put(ws, r, 10, (f"{hub} cụm 🏠 trên {d['_hub']}" if hub else d["domain"]),
            size=9, fill=fill)
        put(ws, r, 11, "", fill=fill)
        ws.row_dimensions[r].height = 86

    r += 2
    band(ws, r, 1, 11, "BỐN RÀO CẢN NỀN — BẢN PHILIPPINES · mọi bài phải gỡ được ít nhất một",
         TEAL)
    r += 1
    header_row(ws, r, ["RÀO CẢN", "KHÁCH ĐANG NGHĨ GÌ", "", "", "",
                       "BẰNG CHỨNG SUNWOO DÙNG ĐỂ GỠ", "", "", "", "", "CỤM XỬ LÝ"])
    for ten, ng, gan, cum, nong in [
        ("① NGỜ — không biết tin ai",
         "“Is this clinic real? Is this doctor licensed? Is this device registered?” "
         "Ba tên miền rời nhau làm rào này nặng hơn bình thường.",
         "Diplomate, Philippine Dermatological Society · PRC license number · số đăng ký FDA PH "
         "của từng thiết bị · giấy phép DOH của cơ sở",
         "C14 · C12 · C08", True),
        ("② NGẠI — đi lại, riêng tư, bị bán thêm",
         "“How long is the drive from Makati at 6pm?” · “Will someone see me walking in?” · "
         "“Will they upsell me?”",
         "Trang vành đai V1–V4 có thời gian đi thật · luxury private suites · free consultation "
         "· báo giá văn bản trước",
         "C04 · C09 · C07", False),
        ("③ SỢ — hỏng, không đảo ngược được",
         "“Can filler be dissolved?” · “Is tooth shaving permanent?” · “Will laser darken "
         "my skin?”",
         "Nội dung rủi ro nói thật có số · 24/7 care coordinator · quy trình xử trí biến chứng "
         "· chính sách làm lại có T&C",
         "C06 · C11 · C10", False),
        ("④ BỀN — rào ĐẶC THÙ gói nội địa PH",
         "“It lasts 12 months, then what? How much more do I pay, forever?” — cả ba line đều "
         "bán thủ thuật nhiều buổi, hiệu quả có thời hạn.",
         "Mốc tháng cụ thể + chi phí dặm lại + nhịp nhắc tái khám. ⛔ Không trấn an suông kiểu "
         "“results are long-lasting”.",
         "C15 · C07 · C05", True),
    ]:
        r += 1
        f = AMBER_WASH if nong else CREAM
        put(ws, r, 1, ten, bold=True, fill=f)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
        put(ws, r, 2, ng, size=9, fill=f)
        for c in range(3, 6):
            put(ws, r, c, None, fill=f)
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=10)
        put(ws, r, 6, gan, size=9, fill=f)
        for c in range(7, 11):
            put(ws, r, c, None, fill=f)
        put(ws, r, 11, cum, size=9, ha="center", fill=f)
        ws.row_dimensions[r].height = 52

    widths(ws, {1: 34, 2: 10, 3: 44, 4: 46, 5: 50, 6: 22, 7: 8, 8: 8, 9: 10, 10: 26, 11: 20})
    ws.freeze_panes = "A5"


# ───────────────────────────── SHEET 3 ───────────────────────────────────

def sheet3(wb, d, rows):
    ws = wb.create_sheet(f"3. {d['ten_ngan']}- Bo truy van Master")
    q = d["quy_mo"]
    P0 = 20  # cột đầu của panel xếp hạng cụm (cột 19 để trống làm vạch ngăn)
    band(ws, 1, 1, 18, f"{d['ten_vi'].upper()} — BỘ TRUY VẤN MASTER  |  "
                       f"ChatGPT · Gemini · AI Overview · Perplexity · Copilot", INK, size=12, h=24)
    band(ws, 1, P0, P0 + 10, "KHUYẾN NGHỊ CỤM ƯU TIÊN THEO NGUYÊN TẮC 80/20", INK, size=11)
    ghi_chu(ws, 2, 1, 18,
            f"{q['truy_van']} truy vấn · {q['cum']} cụm · {q['core']} truy vấn CORE 80/20 "
            f"({round(q['core']/q['truy_van']*100)}% bộ) chiếm {q['pct_diem_core']}% điểm "
            f"ưu tiên · CORE xếp theo thứ tự triển khai 90 ngày · "
            f"{q['bai']} bài cần sản xuất")
    ghi_chu(ws, 2, P0, P0 + 10,
            "Xếp hạng cụm theo điểm ưu tiên. Tầng A = làm trước trong 90 ngày với 70% "
            "ngân sách nội dung; B mở khi A xong ~60%.")
    ghi_chu(ws, 3, 1, 18,
            "ĐIỂM ƯU TIÊN = Giá trị ca (Cao 3 · TB 2 · Thấp 1) × Nhiệt độ (Hot 3 · Warm 2 "
            "· Existing 2 · Cold 1) × Ưu tiên (P1 3 · P2 2 · P3 1) × CƠ HỘI GEO.  "
            "⚠ Sunwoo chưa có mốc traffic AI → CƠ HỘI GEO = 1 cho mọi cụm; chấm lại sau "
            "tháng Setup.  ⚠ Truy vấn là BẢN NHÁP v1, chưa đối chiếu dữ liệu tìm kiếm thật.",
            color=RED)
    ghi_chu(ws, 3, P0, P0 + 10,
            "Hai cột điểm có nguồn khác nhau và LỆCH NHAU LÀ BÌNH THƯỜNG: «ĐIỂM CỤM» cộng "
            "bottom-up từ 17 truy vấn của cụm; «% ĐIỂM (chỉ mục)» lấy từ "
            "knowledge/geo-bo-truy-van-index.md — đây là con số Agent dùng để lập kế hoạch.",
            color=RED)

    header_row(ws, 4, ["ID", "CỤM CHỦ ĐỀ", "GIAI ĐOẠN", "TRUY VẤN KHÁCH GÕ VÀO AI (EN)",
                       "GÓC HỎI (fan-out)", "NHIỆT ĐỘ", "ƯU TIÊN", "GIÁ TRỊ CA", "NHÓM 80/20",
                       "TẦNG ƯU TIÊN", "THỨ TỰ TRIỂN KHAI (CORE)", "ĐIỂM ƯU TIÊN",
                       "TỪ KHOÁ ƯU TIÊN (EN)", "KHỐI TRẢ LỜI CẦN CÓ (brief giao content)",
                       "TÊN MIỀN", "TRANG ĐÍCH SUNWOO", "RÀO PHÁP LÝ (PH)", "ĐỐI TƯỢNG"])
    header_row(ws, 4, ["HẠNG", "MÃ", "CỤM", "TẦNG", "CƠ HỘI GEO (1–3)", "SỐ TV", "CORE",
                       "ĐIỂM CỤM", "% ĐIỂM (chỉ mục)", "% LŨY KẾ", "SỐ BÀI"], start=P0)

    core_rows = sorted([x for x in rows if x["core"]], key=lambda x: x["thu_tu"])
    rest = [x for x in rows if not x["core"]]
    chan = bi_chan(d)
    r = 4
    for row in core_rows + rest:
        r += 1
        if chan:
            f = PINK
        else:
            f = AMBER_WASH if row["core"] else (CREAM if row["cum"]["tang"] == "A" else None)
        hub = row["domain"] == d["_hub"]
        put(ws, r, 1, row["id"], size=9, ha="center", fill=f, bold=row["core"])
        put(ws, r, 2, f"{row['ma']} · {row['cum']['ten_vi']}", size=9, fill=f)
        put(ws, r, 3, GIAI_DOAN[row["cum"]["gd"]], size=9, fill=f)
        put(ws, r, 4, row["truy_van"] or "[CẦN VIẾT]", size=10, fill=f,
            italic=not row["truy_van"], color=INK_TXT if row["truy_van"] else GREY_TXT)
        put(ws, r, 5, row["goc"], size=9, ha="center", fill=f)
        put(ws, r, 6, row["nhiet"], size=9, ha="center", fill=f)
        put(ws, r, 7, row["ut"], size=9, ha="center", fill=f)
        put(ws, r, 8, row["dt"], size=9, ha="center", fill=f)
        put(ws, r, 9, "CORE 80/20" if row["core"] else "—", size=9, ha="center",
            fill=f, bold=row["core"])
        put(ws, r, 10, TANG_TEN[row["cum"]["tang"]], size=9, fill=f)
        put(ws, r, 11, row.get("thu_tu", ""), size=9, ha="center", fill=f)
        put(ws, r, 12, row["diem"], size=9, ha="center", fill=f, bold=True)
        put(ws, r, 13, row["tu_khoa"], size=9, fill=f)
        put(ws, r, 14, row["khoi"] or "[CẦN VIẾT brief: BLUF + số liệu + điều bất lợi]",
            size=9, fill=f, italic=not row["khoi"],
            color=INK_TXT if row["khoi"] else GREY_TXT)
        put(ws, r, 15, ("🏠 " if hub else "") + row["domain"], size=9, fill=f, bold=hub)
        put(ws, r, 16, row["trang"], size=9, fill=f)
        put(ws, r, 17, ("[BLOCKED · R4] " if chan else "") + row["rao"], size=9, fill=f)
        put(ws, r, 18, row["doi_tuong"], size=9, fill=f)
        ws.row_dimensions[r].height = 54

    diem_cum = {}
    for row in rows:
        diem_cum[row["ma"]] = diem_cum.get(row["ma"], 0) + row["diem"]
    luy = 0
    rr = 4
    for cum in sorted(d["cum"], key=lambda c: c["hang"]):
        rr += 1
        luy += cum["pct"]
        f = AMBER_WASH if cum["tang"] == "A" else (CREAM if rr % 2 else None)
        nha = " 🏠" if cum.get("tren_hub") else ""
        put(ws, rr, P0, cum["hang"], ha="center", fill=f, bold=True)
        put(ws, rr, P0 + 1, cum["ma"], ha="center", fill=f, bold=True)
        put(ws, rr, P0 + 2, f"{cum['ma']} · {cum['ten_en']}{nha}", size=9, fill=f)
        put(ws, rr, P0 + 3, TANG_TEN[cum["tang"]], size=9, fill=f)
        put(ws, rr, P0 + 4, CO_HOI_GEO, ha="center", fill=f)
        put(ws, rr, P0 + 5, cum["tv"], ha="center", fill=f)
        put(ws, rr, P0 + 6, cum["core"], ha="center", fill=f)
        put(ws, rr, P0 + 7, diem_cum.get(cum["ma"], 0), ha="center", fill=f)
        put(ws, rr, P0 + 8, cum["pct"] / 100, ha="center", fill=f, fmt=PCT1)
        put(ws, rr, P0 + 9, round(luy / 100, 4), ha="center", fill=f, fmt=PCT1)
        put(ws, rr, P0 + 10, cum["bai"] or "—", ha="center", fill=f, bold=True)
        ws.row_dimensions[rr].height = max(ws.row_dimensions[rr].height or 0, 40)
    rr += 1
    put(ws, rr, P0, "TỔNG", bold=True, fill=MINT)
    for c, v in ((P0 + 5, q["truy_van"]), (P0 + 6, q["core"]),
                 (P0 + 7, sum(diem_cum.values())), (P0 + 10, q["bai"])):
        put(ws, rr, c, v, ha="center", bold=True, fill=MINT)
    for c in (P0 + 1, P0 + 2, P0 + 3, P0 + 4, P0 + 8, P0 + 9):
        put(ws, rr, c, None, fill=MINT)

    widths(ws, {1: 10, 2: 40, 3: 30, 4: 62, 5: 14, 6: 11, 7: 9, 8: 11, 9: 13, 10: 22,
                11: 13, 12: 11, 13: 28, 14: 70, 15: 24, 16: 46, 17: 26, 18: 26, 19: 3,
                P0: 8, P0 + 1: 8, P0 + 2: 48, P0 + 3: 22, P0 + 4: 12, P0 + 5: 8,
                P0 + 6: 8, P0 + 7: 11, P0 + 8: 14, P0 + 9: 11, P0 + 10: 9})
    ws.freeze_panes = "E5"
    ws.auto_filter.ref = f"A4:R{4 + len(rows)}"


# ───────────────────────────── SHEET 4 ───────────────────────────────────

def sheet4(wb, d, rows):
    ws = wb.create_sheet(f"4. {d['ten_ngan']}- Ban do noi dung")
    bai = sum(c["bai"] for c in d["cum"])
    chan = bi_chan(d)
    band(ws, 1, 1, 17, f"{d['ten_vi'].upper()} — BẢN ĐỒ SẢN XUẤT NỘI DUNG · 15 CỤM → "
                       f"DẠNG BÀI → TÊN MIỀN → TRANG ĐÍCH → SÓNG → PHỤ TRÁCH", INK, size=12, h=24)
    ghi_chu(ws, 2, 1, 10,
            "Xếp theo hạng 80/20 của sheet 3. Sóng 1 (0–30 ngày) = Tầng A; "
            "Sóng 2 (31–60) = Tầng B; Sóng 3 (61–90) = Tầng C; Nền (>90) = Tầng D. "
            "⚠ C14 phải ra TRƯỚC MỌI CỤM KHÁC — nó là khối thực thể nuôi cả ba tên miền.")
    ghi_chu(ws, 3, 1, 10,
            "Cột Tầng · Số TV · CORE · % điểm lấy từ sheet 3. Cột Trạng thái và Ghi chú "
            "để Manager cập nhật hằng tuần.")
    put(ws, 2, 11, bai, bold=True, ha="center")
    put(ws, 2, 12, "bài viết", size=9)
    put(ws, 3, 11, len(d["cum"]), bold=True, ha="center")
    put(ws, 3, 12, "cụm", size=9)
    if chan:
        put(ws, 2, 14, "⛔ LINE BỊ CHẶN (R4)", bold=True, fill=PINK, color=RED)
        put(ws, 3, 14, "Sản xuất được, ⛔ chưa phát hành được", size=9, fill=PINK)
    header_row(ws, 4, ["HẠNG", "MÃ", "TÊN CỤM (EN — dùng trên site)", "NGHĨA (VI)", "TẦNG",
                       "GIAI ĐOẠN", "SỐ TV", "CORE", "% ĐIỂM", "VAI TRÒ TRONG PHỄU", "SỐ BÀI",
                       "DẠNG NỘI DUNG CẦN SẢN XUẤT", "TÊN MIỀN", "TRANG ĐÍCH CHÍNH",
                       "SÓNG TRIỂN KHAI", "PHỤ TRÁCH", "TRẠNG THÁI"])
    vai_tro = {
        "C14": "Khối thực thể gốc — điều kiện cần để AI nối ba tên miền về một phòng khám",
        "C04": "Cửa vào lớn nhất: “near me” và truy vấn theo vành đai đi lại",
        "C08": "Chuyển đổi trực tiếp — nơi AI thay hành vi hỏi bạn bè",
        "C07": "Tín hiệu mua hàng rõ nhất; bài bóc tách chi phí là bài GEO mạnh nhất",
        "C06": "Gỡ rào SỢ — quyết định có đặt lịch hay không",
        "C12": "Khối bằng chứng nuôi cả C06, C08 và C14",
        "C05": "Cầu nối: khách chưa chốt phương án",
        "C11": "Giữ khách đã có vấn đề; chặn khủng hoảng niềm tin",
        "C09": "Giảm huỷ lịch, tăng tỷ lệ đến khám",
        "C13": "Nhóm đặc thù — cộng đồng Hàn McKinley Hill là nhóm chưa ai chạy riêng",
        "C10": "Không tạo lead mới nhưng NEO THỰC THỂ trong AI + giảm biến chứng",
        "C03": "Bản đồ hệ sinh thái ba mảng",
        "C15": "Trả lời rào BỀN — cửa LTV lớn nhất",
        "C01": "Cửa vào rộng, không bán",
        "C02": "Gỡ thông tin sai trên mạng xã hội",
    }
    dang_bai = {
        "C14": "1 trang thực thể /about/ + hồ sơ từng bác sĩ (schema Physician + sameAs)",
        "C04": "Trang vành đai V1–V3 chuẩn NAP, có thời gian đi thật giờ cao điểm",
        "C08": "Trang /doctors/ + bài hướng dẫn tự kiểm tra PRC",
        "C07": "Trang giá công khai dải min–max + bài bóc tách tổng chi phí liệu trình",
        "C06": "1 trang trụ “risks and side effects” + bài tình huống biến chứng",
        "C12": "Trang /credentials/ công bố giấy phép DOH · PRC · số đăng ký FDA",
        "C05": "Bảng so sánh trung thực, nêu cả khi KHÔNG nên làm",
        "C11": "Trang chính sách làm lại + bài xử lý khi kết quả chưa đạt",
        "C09": "Trang đặt lịch + bài quy trình buổi khám đầu tiên",
        "C13": "Trang nhóm đặc thù trên tên miền trục (Hàn · expat · OFW)",
        "C10": "Cẩm nang hậu thủ thuật theo mốc giờ/ngày + dấu hiệu đỏ",
        "C03": "Trang danh mục dịch vụ theo đúng phạm vi giấy phép",
        "C15": "Bài “how long it lasts” có mốc tháng + chi phí dặm lại",
        "C01": "Pillar nền định danh vấn đề",
        "C02": "Bài gỡ thông tin sai, tái sử dụng khối tiêu chí của C08",
    }
    phu_trach = {
        "C14": "Team Tech/Dev + Lead Content", "C12": "Pháp chế + Team Content",
        "C07": "Vận hành + Pháp chế", "C04": "Team Content/SEO",
        "C08": "Lead Content + BS thẩm định",
    }
    r = 4
    for cum in sorted(d["cum"], key=lambda c: c["hang"]):
        r += 1
        if chan:
            f = PINK
        else:
            f = AMBER_WASH if cum["tang"] == "A" else (CREAM if r % 2 else None)
        hub = cum.get("tren_hub")
        put(ws, r, 1, cum["hang"], ha="center", fill=f, bold=True)
        put(ws, r, 2, cum["ma"], ha="center", fill=f, bold=True)
        put(ws, r, 3, cum["ten_en"], size=9, fill=f)
        put(ws, r, 4, cum["ten_vi"], size=9, fill=f)
        put(ws, r, 5, TANG_TEN[cum["tang"]], size=9, fill=f)
        put(ws, r, 6, GIAI_DOAN[cum["gd"]], size=9, fill=f)
        put(ws, r, 7, cum["tv"], ha="center", fill=f)
        put(ws, r, 8, cum["core"] or "—", ha="center", fill=f)
        put(ws, r, 9, cum["pct"] / 100, ha="center", fill=f, fmt=PCT)
        put(ws, r, 10, vai_tro.get(cum["ma"], ""), size=9, fill=f)
        put(ws, r, 11, cum["bai"] or "—", ha="center", fill=f, bold=True)
        put(ws, r, 12, dang_bai.get(cum["ma"], ""), size=9, fill=f)
        put(ws, r, 13, ("🏠 " if hub else "") + (d["_hub"] if hub else d["domain"]),
            size=9, fill=f, bold=bool(hub))
        put(ws, r, 14, cum["trang_dich"], size=9, fill=f)
        put(ws, r, 15, SONG_TEN[cum["song"]], size=9, fill=f)
        put(ws, r, 16, phu_trach.get(cum["ma"], "Team Content + BS thẩm định"), size=9, fill=f)
        put(ws, r, 17, "⛔ Chờ nha sĩ" if chan else "Chưa làm", size=9, ha="center",
            fill=PINK if chan else CREAM)
        ws.row_dimensions[r].height = 56
    r += 1
    put(ws, r, 1, "TỔNG", bold=True, fill=MINT)
    for c in range(2, 18):
        put(ws, r, c, None, fill=MINT)
    put(ws, r, 7, d["quy_mo"]["truy_van"], ha="center", bold=True, fill=MINT)
    put(ws, r, 8, d["quy_mo"]["core"], ha="center", bold=True, fill=MINT)
    put(ws, r, 11, bai, ha="center", bold=True, fill=MINT)
    widths(ws, {1: 8, 2: 8, 3: 46, 4: 36, 5: 22, 6: 30, 7: 8, 8: 8, 9: 10, 10: 38, 11: 9,
                12: 60, 13: 24, 14: 46, 15: 20, 16: 26, 17: 15})
    ws.freeze_panes = "C5"


# ───────────────────────────── SHEET 5 ───────────────────────────────────

# Câu hỏi NÓI VỚI phòng khám ("Do you have a branch in Alabang?") không đo được
# Share of Voice — không ai gõ câu đó vào ChatGPT để tìm phòng khám.
LOAI_KHOI_DO = ("do you", "does the clinic", "can you", "will you",
                "is there parking", "is there a waiting", "do i need to bring",
                "what if i am late", "can i request", "where are the clinic")
# Tín hiệu một truy vấn đo được: có địa danh, có ý định thương mại, có so sánh.
TIN_HIEU_DO = ("philippines", "metro manila", "taguig", "bgc", "makati",
               "mckinley", "quezon", "near me", "cost", "price", "best",
               "which", "who", "vs", "compare", "how long", "how much",
               "risks", "safe", "worth it")


def diem_do(q):
    low = q.lower()
    if low.startswith(LOAI_KHOI_DO):
        return -1
    return sum(1 for t in TIN_HIEU_DO if t in low)


def sheet5(wb, d, rows, prompts):
    ws = wb.create_sheet(f"5. {d['ten_ngan']}- Prompt do luong")
    band(ws, 1, 1, 12, f"{d['ten_vi'].upper()} — BỘ PROMPT ĐO LƯỜNG GEO · "
                       f"SHARE OF VOICE TRONG AI", INK, size=12, h=24)
    ghi_chu(ws, 2, 1, 12,
            "Cách chạy: CHẾ ĐỘ ẨN DANH (không đăng nhập, tắt cá nhân hoá, xoá lịch sử "
            "phiên), dán NGUYÊN VĂN từng prompt. Ghi 1 nếu Sunwoo được nhắc tên, 0 nếu "
            "không. CHẠY 3 LẦN LẤY ĐA SỐ.")
    ghi_chu(ws, 3, 1, 12,
            "Kết quả AI thay đổi theo phiên → đo XU HƯỚNG theo tháng, không đo tuyệt đối "
            "một lần. Nhân bản sheet này mỗi tháng. Hai cột cuối là dữ liệu quý nhất: "
            "đối thủ được AI nhắc và URL AI trích.")
    ws.merge_cells(start_row=4, start_column=1, end_row=4, end_column=2)
    put(ws, 4, 1, "Tháng đo:", bold=True, va="center")
    put(ws, 4, 2, None)
    ws.merge_cells(start_row=4, start_column=3, end_row=4, end_column=12)
    put(ws, 4, 3, "⚠ Chưa đo — tháng Setup là tháng lấy mốc gốc", fill=CREAM, size=9,
        va="center")
    for c in range(4, 13):
        put(ws, 4, c, None, fill=CREAM)
    ws.row_dimensions[4].height = 20
    header_row(ws, 5, ["#", "PROMPT KIỂM TRA (dán nguyên văn — EN)", "CỤM ĐO", "MÃ CỤM",
                       "TẦNG"] + NEN_TANG + ["SỐ NỀN TẢNG NHẮC", "ĐỐI THỦ & URL AI TRÍCH"])

    # ① Truy vấn CỦA CHÍNH BỘ NÀY — đúng dịch vụ, đúng cụm. Mỗi cụm Tầng A lấy 3
    #    câu đo được nhất; ⛔ không lấy câu ngắn nhất (hay rơi vào câu hỏi nói với
    #    phòng khám, không đo được Share of Voice).
    ds = []
    for cum in sorted([c for c in d["cum"] if c["tang"] == "A"], key=lambda c: c["hang"]):
        cands = [x for x in rows if x["ma"] == cum["ma"] and x["truy_van"]
                 and diem_do(x["truy_van"]) >= 0]
        cands.sort(key=lambda x: (-diem_do(x["truy_van"]), len(x["truy_van"])))
        for x in cands[:3]:
            ds.append({"p": x["truy_van"], "ma": cum["ma"], "nguon": ""})
    # ② Prompt vận hành CHUNG CỦA LINE — đo cho cả line, KHÔNG riêng bộ này. Tách
    #    khối riêng và ⛔ không gán mã cụm giả; chỉ lấy prompt thật sự nhắc tới dịch
    #    vụ của bộ, hoặc prompt cấp thương hiệu / địa bàn.
    cua_bo = TU_KHOA_BO.get(d["key"], [])
    cua_bo_khac = [t for k, ds_ in TU_KHOA_BO.items() if k != d["key"] for t in ds_]
    chung = []
    for b in prompts["bo"]:
        if b["ma"] not in ("P-BRAND", "P-LOCAL") and b["line"] != d["line"]:
            continue
        for p in b["prompts"]:
            low = p.lower()
            cua_minh = any(t in low for t in cua_bo)
            cua_nguoi = any(t in low for t in cua_bo_khac)
            # Giữ prompt của chính bộ này, hoặc prompt trung tính (không nhắc
            # dịch vụ nào). ⛔ Loại prompt nhắc dịch vụ của bộ khác.
            if not (cua_minh or not cua_nguoi):
                continue
            if not any(x["p"] == p for x in ds) and not any(x["p"] == p for x in chung):
                chung.append({"p": p, "ma": "", "nguon": b["ma"]})

    r = 5
    i = 0

    def dong_prompt(p, nhan_cum, nhan_tang, f):
        nonlocal r, i
        i += 1
        r += 1
        put(ws, r, 1, i, ha="center", fill=f)
        put(ws, r, 2, p["p"], size=10, fill=f)
        put(ws, r, 3, nhan_cum, size=9, fill=f)
        put(ws, r, 4, p["ma"] or "—", ha="center", fill=f)
        put(ws, r, 5, nhan_tang, size=9, fill=f)
        for c in range(6, 11):
            put(ws, r, c, None, fill=CREAM, ha="center")
        put(ws, r, 11, None, ha="center", fill=f)
        put(ws, r, 12, None, fill=CREAM)
        ws.row_dimensions[r].height = max(
            32, round(max(math.ceil(len(p["p"]) / 72),
                          math.ceil(len(nhan_cum) / 38)) * 13.4) + 5)

    for p in ds:
        cum = next((c for c in d["cum"] if c["ma"] == p["ma"]), None)
        dong_prompt(p, cum["ten_en"] if cum else "", TANG_TEN[cum["tang"]] if cum else "",
                    CREAM if i % 2 else None)

    if chung:
        r += 1
        band(ws, r, 1, 12, "BỘ PROMPT VẬN HÀNH CHUNG CỦA LINE — đo cho cả line, "
                           "KHÔNG riêng bộ này", TEAL, size=10)
        for p in chung:
            dong_prompt(p, f"(bộ vận hành {p['nguon']})", "— cấp line", MINT)

    r += 2
    band(ws, r, 1, 12, "BA PROMPT KIỂM TRA SỨC KHOẺ THỰC THỂ — chạy mỗi tháng, ngoài bảng chấm điểm",
         TEAL)
    for p, doc_ in [
        ("Is Sunwoo Aesthetic the same company as Sunwoo Dental?",
         "AI trả lời ĐÚNG là một hệ thống → thực thể đã liền. Trả lời “không rõ” hoặc coi là "
         "hai nơi khác nhau → luật ba tên miền chưa có tác dụng."),
        ("Who owns sunwoomedical.ph?",
         "Kiểm tra AI có gắn đúng pháp nhân không — chạm rào R3."),
        ("How many doctors work at Sunwoo?",
         "Nếu AI trả lời 300 → con số sai trên trang production đã bị AI học. Đây là bằng chứng "
         "cứng để ép sửa."),
    ]:
        r += 1
        put(ws, r, 1, "⚑", ha="center", fill=AMBER_WASH)
        put(ws, r, 2, p, size=10, fill=AMBER_WASH)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=12)
        put(ws, r, 3, doc_, size=9, fill=AMBER_WASH)
        for c in range(4, 13):
            put(ws, r, c, None, fill=AMBER_WASH)
        ws.row_dimensions[r].height = 36

    widths(ws, {1: 6, 2: 74, 3: 40, 4: 10, 5: 22, 6: 11, 7: 11, 8: 13, 9: 12, 10: 11,
                11: 15, 12: 42})
    ws.freeze_panes = "B6"


# ───────────────────────────── SHEET 6 ───────────────────────────────────

def sheet6(wb, d, rows):
    ws = wb.create_sheet(f"6. {d['ten_ngan']}- Rao phap ly PH")
    band(ws, 1, 1, 9, f"{d['ten_vi'].upper()} — RÀO PHÁP LÝ PHILIPPINES · SOÁT TRƯỚC KHI ĐĂNG "
                      f"BẤT KỲ NỘI DUNG NÀO TRONG BỘ NÀY", INK, size=12, h=24)
    ghi_chu(ws, 2, 1, 9,
            "NGUYÊN TẮC NỀN: KHÔNG CHẮC → DỪNG → HỎI PHÁP CHẾ → RỒI MỚI ĐĂNG. "
            "Tài liệu vận hành nội bộ, KHÔNG thay thế ý kiến luật sư.")
    ghi_chu(ws, 3, 1, 9,
            "Cơ quan: FDA Philippines (RA 9711) · DOH · PRC · ASC · NPC (RA 10173) · DTI. "
            "Mỗi truy vấn ở sheet 3 (cột RÀO PHÁP LÝ) bắt đầu bằng mã R0–R11 → cột SỐ TV "
            "và CORE dưới đây tự đếm từ đó.")
    header_row(ws, 4, ["MÃ", "RÀO", "⛔ KHÔNG ĐƯỢC LÀM", "✅ THAY BẰNG", "ÁP DỤNG CHO CỤM",
                       "SỐ TV", "CORE", "NGƯỜI DUYỆT", "ĐÃ PHỔ BIẾN CHO TEAM"])
    r = 4
    for ma, ten, khong, thay, duyet in RAO_BANG:
        r += 1
        hit = [x for x in rows
               if ma in [t.strip() for t in x["rao"].replace("·", " ").split()]]
        cums = sorted({x["ma"] for x in hit})
        nong = ma in RAO_NONG
        f = PINK if nong else (CREAM if r % 2 else None)
        put(ws, r, 1, ma, bold=True, ha="center", fill=f)
        put(ws, r, 2, ten, size=9, bold=nong, fill=f)
        put(ws, r, 3, khong, size=9, fill=f)
        put(ws, r, 4, thay, size=9, fill=f)
        put(ws, r, 5, " ".join(cums) or "—", size=9, fill=f)
        put(ws, r, 6, len(hit), ha="center", fill=f)
        put(ws, r, 7, sum(1 for x in hit if x["core"]), ha="center", fill=f)
        put(ws, r, 8, duyet, size=9, fill=f)
        put(ws, r, 9, "Chưa", size=9, ha="center", fill=CREAM)
        ws.row_dimensions[r].height = 52

    r += 2
    band(ws, r, 1, 9, "QUY TRÌNH BẮT BUỘC — BA CỬA, KHÔNG BỎ CỬA NÀO", TEAL)
    r += 1
    dong(ws, r, 1, 9,
         "Content soạn → tự kiểm checklist 12 ô (R0–R11) → BÁC SĨ ĐÚNG CHUYÊN KHOA thẩm định, "
         "ghi “Medically reviewed by [tên], [chuyên khoa], PRC #…” (R4) → PHÁP CHẾ duyệt nội "
         "dung và hình ảnh → (nếu là quảng cáo health product) DUYỆT TRƯỚC tại FDA PH · ASC "
         "(R9) → phát hành → lưu hồ sơ.  ⚠ Mọi đầu việc phải CỘNG thời gian duyệt vào hạn chót; "
         "⛔ không đặt hạn sản xuất trùng ngày phát hành.", size=10, h=46)
    r += 2
    band(ws, r, 1, 9, "HAI RÀO CHI PHỐI KHỐI LƯỢNG LỚN NHẤT CỦA BỘ NÀY", RED)
    r += 1
    dong(ws, r, 1, 9,
         "🔴 R9 — DUYỆT TRƯỚC KHI PHÁT. Khác bộ Việt Nam ở chỗ: ở PH, THIẾT BỊ và SẢN PHẨM mới "
         "là thứ kéo nội dung vào diện phải duyệt, không phải bản thân dịch vụ KCB. Bốn trong "
         "năm dịch vụ thẩm mỹ của Sunwoo đều dùng health product → phần lớn cụm C06 · C07 · C05 "
         "· C12 đều chạm R9. Phải đưa “lập danh mục nội dung cần duyệt trước + nộp lô đầu” thành "
         "một đầu việc riêng của tháng Setup.", fill=PINK, h=48)
    r += 1
    dong(ws, r, 1, 9,
         "🔴 R4 — BÁC SĨ. Sunwoo công bố HAI bác sĩ, KHÔNG ai là nha sĩ. Rào này vì thế không "
         "chỉ là việc rà câu chữ — nó CHẶN toàn bộ 76 bài của line nha khoa và ĐẶT TRẦN sản "
         "lượng cho hai line còn lại (mặc định ≤24 bài/bác sĩ/tháng).", fill=PINK, h=40)

    widths(ws, {1: 7, 2: 36, 3: 56, 4: 60, 5: 30, 6: 8, 7: 8, 8: 22, 9: 16})
    ws.freeze_panes = "A5"


# ─────────────────────── tự soát hiển thị trước khi lưu ───────────────────

def soat_hien_thi(wb):
    """Tìm ô sẽ bị CẮT CHỮ khi mở bằng Excel.

    Excel KHÔNG tự giãn dòng cho ô đã đặt chiều cao, và cũng không giãn cho ô gộp.
    Một câu 250 ký tự nằm trong cột rộng 8 ký tự, cao 15pt thì mở ra chỉ thấy một
    mẩu — file vẫn hợp lệ, vẫn mở được, nên không có gì báo lỗi. Hàm này báo.
    """
    xau = []
    for ws in wb.worksheets:
        span = {(m.min_row, m.min_col): (m.min_col, m.max_col)
                for m in ws.merged_cells.ranges}
        for row in ws.iter_rows():
            for cl in row:
                if not isinstance(cl.value, str) or len(cl.value) < 30:
                    continue
                if not (cl.alignment and cl.alignment.wrap_text):
                    continue
                c1, c2 = span.get((cl.row, cl.column), (cl.column, cl.column))
                rong = 0.0
                for c in range(c1, c2 + 1):
                    dc = ws.column_dimensions.get(get_column_letter(c))
                    rong += (dc.width if dc and dc.width else 8.43)
                rd = ws.row_dimensions.get(cl.row)
                cao = rd.height if rd and rd.height else 15.0
                can = math.ceil(len(cl.value) / max(rong - 1, 1)) * (cl.font.sz or 11) * 1.32
                if can > cao + 3:
                    xau.append(f"{ws.title}!{cl.coordinate} "
                               f"(rộng {rong:.0f} · cao {cao:.0f}pt · cần {can:.0f}pt)")
    return xau


# ─────────────────────────────── main ────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", default="all", help="key bộ, phẩy ngăn cách; hoặc 'all'")
    a = ap.parse_args()
    scope = [s.strip() for s in a.scope.split(",")]

    os.makedirs(OUT_DIR, exist_ok=True)
    bos, line_of, prompts = load(scope)
    if not bos:
        sys.exit("Không có bộ nào khớp --scope.")

    tong_tv = tong_bai = 0
    khoa = []
    for d in bos:
        d["ten_ngan"] = TEN_NGAN.get(d["key"], d["key"][:8].capitalize())
        if len(d["ten_ngan"]) > 8:
            sys.exit(f"TEN_NGAN['{d['key']}'] dài {len(d['ten_ngan'])} ký tự — "
                     f"tên sheet sẽ vượt 31 ký tự của Excel. Rút còn <=8.")
        rows = rows_of(d)
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
        sheet1(wb, d, rows)
        sheet2(wb, d, rows)
        sheet3(wb, d, rows)
        sheet4(wb, d, rows)
        sheet5(wb, d, rows, prompts)
        sheet6(wb, d, rows)
        loi = soat_hien_thi(wb)
        if loi:
            print(f"!! {d['key']}: {len(loi)} ô sẽ bị CẮT CHỮ trong Excel")
            for x in loi[:5]:
                print(f"     {x}")
        out = os.path.join(OUT_DIR, f"{d['key']}.xlsx")
        try:
            wb.save(out)
        except PermissionError:
            # Windows khoá file đang mở trong Excel. Báo rõ rồi đi tiếp, ⛔ không
            # dừng cả mẻ — 9 bộ còn lại vẫn phải được sinh ra.
            khoa.append(d["key"])
            print(f"!! {d['key']+'.xlsx':24} ĐANG MỞ TRONG EXCEL — bỏ qua, chưa cập nhật")
            continue
        da = sum(1 for x in rows if x["truy_van"])
        hub = sum(1 for x in rows if x["domain"] == d["_hub"])
        tong_tv += len(rows)
        tong_bai += d["quy_mo"]["bai"]
        chan = " [BLOCKED R4]" if bi_chan(d) else ""
        print(f"OK {d['key']+'.xlsx':24} {len(rows)} truy vấn · {da} đã viết · "
              f"{sum(1 for x in rows if x['core'])} CORE · {hub} trên hub · "
              f"{d['quy_mo']['bai']} bài{chan}")

    print(f"   {len(bos) - len(khoa)}/{len(bos)} bộ · {tong_tv} truy vấn · {tong_bai} bài "
          f"· 6 sheet/file → {os.path.relpath(OUT_DIR, ROOT)}")
    if khoa:
        print(f"!! CHƯA CẬP NHẬT: {', '.join(khoa)} — đóng file trong Excel rồi chạy lại:")
        print(f"   python tools/build-botruyvan.py --scope {','.join(khoa)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
