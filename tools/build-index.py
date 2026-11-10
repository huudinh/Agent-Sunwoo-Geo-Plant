# -*- coding: utf-8 -*-
"""
build-index.py — Sinh hai file tri thức từ `data/`:

    knowledge/geo-bo-truy-van-index.md   <- data/query-sets/*.json + data/lines.json
    knowledge/geo-prompt-do-luong.md     <- data/geo-prompts.json

    python tools/build-index.py

KHÔNG sửa tay hai file knowledge nói trên — sửa JSON trong `data/` rồi chạy lại.

Quy ước ngôn ngữ (xem SYSTEM-PROMPT §0):
  · Tên cụm · trang đích · prompt đo lường -> TIẾNG ANH (lớp khách Philippines gõ).
  · Khung bảng · nỗi sợ · ghi chú vận hành -> TIẾNG VIỆT (lớp đội HCI điều hành).
"""
import json
import os
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETS = os.path.join(ROOT, "data", "query-sets")
KNOW = os.path.join(ROOT, "knowledge")

SONG_TEN = {1: "S1 (0–30n)", 2: "S2 (31–60n)", 3: "S3 (61–90n)", 4: "Nền (>90n)"}


def load():
    lines = json.load(open(os.path.join(ROOT, "data", "lines.json"), encoding="utf-8"))
    order = [l["ma"] for l in lines["lines"]]
    sets = []
    for l in lines["lines"]:
        for key in l["bo"]:
            p = os.path.join(SETS, key + ".json")
            if not os.path.exists(p):
                print(f"  ! thiếu {p} — bỏ qua")
                continue
            sets.append(json.load(open(p, encoding="utf-8")))
    return lines, order, sets


def build_index(lines, order, sets):
    L = []
    w = L.append
    tong_bai = sum(s["quy_mo"]["bai"] for s in sets)
    tong_cum = sum(s["quy_mo"]["cum"] for s in sets)
    tong_tv = sum(s["quy_mo"]["truy_van"] for s in sets)
    line_of = {l["ma"]: l for l in lines["lines"]}
    hub = lines["ten_mien_truc"]

    w("# GEO SUNWOO — CHỈ MỤC BỘ TRUY VẤN & BẢN ĐỒ NỘI DUNG")
    w("")
    w("> Sinh tự động từ `data/query-sets/*.json` + `data/lines.json` bằng `tools/build-index.py`.")
    w("> **Không sửa tay file này** — sửa JSON nguồn rồi chạy lại script.")
    w("> Đây là **nguồn sự thật duy nhất về khối lượng công việc**: cột `Bài` của mỗi cụm là con số")
    w("> duy nhất được phép dùng để tính chỉ tiêu sản lượng.")
    w("")
    w(f"**Tổng kho:** {len(sets)} bộ dịch vụ · {tong_cum} cụm chủ đề · {tong_tv} truy vấn · "
      f"**{tong_bai} bài viết** cần sản xuất.")
    w("")
    w("> 🔶 **TRẠNG THÁI DỮ LIỆU — BẢN NHÁP v1.** Toàn bộ số liệu dưới đây suy ra từ mind map Sunwoo")
    w("> ngày 2026-11-10 và hồ sơ thương hiệu đọc ngày 2026-10-23. **Sunwoo chưa có mốc traffic AI nào**,")
    w("> nên *Cơ hội GEO* của mọi cụm đang bằng **1** và điểm ưu tiên mới chỉ phản ánh giá trị doanh thu ×")
    w("> nhiệt độ × ưu tiên. Sau tháng Setup, khi đã khoá bộ đo và dựng xong GA4, **phải chấm lại Cơ hội GEO**")
    w("> **và chạy lại script này**. Trước bước đó, mọi thứ hạng cụm là giả định có căn cứ, không phải bằng chứng.")
    w("")
    w("---")
    w("")
    w("## Quy ước đọc bảng")
    w("")
    w("| Ký hiệu | Nghĩa |")
    w("|---|---|")
    w("| Tầng A | CORE 80/20 — làm trong 90 ngày, **70% ngân sách nội dung** |")
    w("| Tầng B | Đòn bẩy chuyển đổi — mở khi A xong ~60%, **20%** |")
    w("| Tầng C | Uy tín & giữ chân — chạy nền, **10%** |")
    w("| Tầng D | Cửa vào rộng — **0% ngân sách mới**, chỉ pillar nền / tái sử dụng |")
    w("| S1…S6 | Giai đoạn hành trình khách — xem `geo-phuong-phap-luan.md` §2 |")
    w("| Sóng | S1 0–30 ngày · S2 31–60 ngày · S3 61–90 ngày · Nền sau 90 ngày |")
    w("| TV / CORE | Số truy vấn của cụm / trong đó bao nhiêu thuộc CORE 80/20 |")
    w("| Bài | Số bài cần sản xuất (`0` = tái sử dụng nội dung, không tính sản lượng mới) |")
    w(f"| 🏠 | Cụm **bắt buộc xuất bản trên tên miền trục** `{hub}` — xem `geo-luat-ba-ten-mien.md` |")
    w("")
    w("## Ba line & trạng thái cổng chặn")
    w("")
    w("| Mã | Line | Tên miền | Bộ | Bác sĩ thẩm định | Trạng thái |")
    w("|---|---|---|---|---|---|")
    for ma in order:
        l = line_of[ma]
        bs = "<br>".join(l["bac_si_tham_dinh"]) if l["bac_si_tham_dinh"] else "⛔ **chưa có**"
        tt = {"active": "✅ chạy được", "blocked": "⛔ **BỊ CHẶN**",
              "draft": "🔶 nháp"}.get(l["trang_thai"], l["trang_thai"])
        w(f"| **{ma}** | {l['ten_en']} — {l['ten_vi']} | `{l['domain']}` | "
          f"{len(l['bo'])} bộ | {bs} | {tt} |")
    w("")
    for ma in order:
        l = line_of[ma]
        if l.get("cong_chan"):
            w(f"> ⛔ **CỔNG CHẶN LINE {ma}:** {l['cong_chan']}")
            w("")
    w("## Bảng tổng hợp khối lượng theo bộ")
    w("")
    w("| # | Bộ dịch vụ | Line | Tên miền | Cụm | TV | Bài cần SX |")
    w("|---|---|---|---|---|---|---|")
    for i, s in enumerate(sets, 1):
        w(f"| {i} | {s['ten_en']} | {s['line']} | `{s['domain']}` | {s['quy_mo']['cum']} | "
          f"{s['quy_mo']['truy_van']} | **{s['quy_mo']['bai']}** |")
    w(f"| | **TỔNG** | | | **{tong_cum}** | **{tong_tv}** | **{tong_bai}** |")
    w("")
    w("**Khối lượng theo line:**")
    w("")
    w("| Line | Bộ | Bài | % tổng |")
    w("|---|---|---|---|")
    for ma in order:
        bs = [s for s in sets if s["line"] == ma]
        b = sum(s["quy_mo"]["bai"] for s in bs)
        w(f"| {ma} · {line_of[ma]['ten_vi']} | {len(bs)} | **{b}** | {round(b / tong_bai * 100)}% |")
    w("")
    w("---")
    w("")

    for i, s in enumerate(sets, 1):
        w(f"## {i}. {s['ten_vi']}")
        w("")
        w(f"`{s['key']}.json` · **{s['line']}** · `{s['domain']}` · "
          f"**{s['quy_mo']['bai']} bài cần sản xuất**")
        w("")
        w(f"**Tên dùng trên site (EN):** {s['ten_en']}")
        w("")
        w(f"**Nguồn:** {s['nguon']}")
        w("")
        w(f"**Quy mô bộ:** {s['quy_mo']['truy_van']} truy vấn · {s['quy_mo']['cum']} cụm · "
          f"{s['quy_mo']['core']} truy vấn CORE 80/20 "
          f"({round(s['quy_mo']['core'] / s['quy_mo']['truy_van'] * 100)}% bộ) "
          f"chiếm {s['quy_mo']['pct_diem_core']}% điểm ưu tiên")
        w("")
        w("**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):")
        w("")
        for n in s["noi_so"]:
            w(f"- {n['ma']} {n['ten']} → cụm xử lý **{n['cum']}** "
              f"({n['tv']} truy vấn, {n['core']} CORE)")
        w("")
        w("**Hành trình 6 giai đoạn:**")
        w("")
        w("| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |")
        w("|---|---|---|---|---|---|---|")
        for h in s["hanh_trinh"]:
            w(f"| {h['gd']} | {h['uu_tien']} | {h['noi_so']} | {h['cum']} | {h['tv']} | "
              f"{h['core']} | {h['pct']}% |")
        w("")
        w("**Phân bổ 80/20:**")
        w("")
        w("| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |")
        w("|---|---|---|---|---|---|")
        for t in s["tang"]:
            w(f"| {t['tang']} | {t['cum']} | {t['tv']} | {t['pct']}% | {t['bai']} | {t['phan_bo']} |")
        w("")
        w("**Bản đồ nội dung — 15 cụm:**")
        w("")
        w("| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | "
          "% điểm | Bài | Sóng | Trang đích |")
        w("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for c in s["cum"]:
            nha = " 🏠" if c.get("tren_hub") else ""
            w(f"| {c['hang']} | {c['ma']} | {c['ten_en']}{nha} | {c['ten_vi']} | {c['tang']} | "
              f"{c['gd']} | {c['tv']} | {c['core']} | {c['pct']}% | {c['bai']} | "
              f"{SONG_TEN[c['song']]} | {c['trang_dich']} |")
        w("")
        w("---")
        w("")

    w("## Tổng hợp cụm 🏠 — khối lượng dồn về tên miền trục")
    w("")
    w(f"Bốn cụm `C08 · C12 · C13 · C14` của **mọi bộ** đều xuất bản trên `{hub}`. "
      "Đây là nơi khối lượng dễ bị đếm trùng nhất khi lập kế hoạch.")
    w("")
    w("| Bộ | C08 | C12 | C13 | C14 | Cộng về hub |")
    w("|---|---|---|---|---|---|")
    tot = OrderedDict((k, 0) for k in ("C08", "C12", "C13", "C14"))
    for s in sets:
        d = {c["ma"]: c["bai"] for c in s["cum"]}
        row = [d.get(k, 0) for k in tot]
        for k, v in zip(tot, row):
            tot[k] += v
        w(f"| {s['key']} | {row[0]} | {row[1]} | {row[2]} | {row[3]} | **{sum(row)}** |")
    w(f"| **TỔNG** | **{tot['C08']}** | **{tot['C12']}** | **{tot['C13']}** | "
      f"**{tot['C14']}** | **{sum(tot.values())}** |")
    w("")
    w(f"> ⚠ **{sum(tot.values())} bài** trong tổng {tong_bai} bài nằm trên tên miền trục. Khi giao việc, "
      "gộp các cụm 🏠 của nhiều bộ thành **một trang dùng chung** nếu nội dung trùng — "
      "⛔ không dựng hai trang `/doctors/` cho hai line.")
    w("")
    return "\n".join(L) + "\n"


def build_prompts():
    p = json.load(open(os.path.join(ROOT, "data", "geo-prompts.json"), encoding="utf-8"))
    L = []
    w = L.append
    n = sum(len(b["prompts"]) for b in p["bo"])
    w("# BỘ PROMPT ĐO GEO — SUNWOO (TIẾNG ANH)")
    w("")
    w("> Sinh tự động từ `data/geo-prompts.json` bằng `tools/build-index.py`. **Không sửa tay.**")
    w("")
    w(f"**{len(p['bo'])} bộ · {n} prompt.** Đây là thước đo của trụ cột KPI số 3 (trọng số 0,40).")
    w("")
    w(f"**Ngôn ngữ:** {p['ngon_ngu']}")
    w("")
    w(f"**Nền tảng đo:** {' · '.join(p['nen_tang'])}")
    w("")
    w(f"**Giao thức:** {p['giao_thuc']}")
    w("")
    w("> ⚠ Kết quả AI thay đổi theo phiên. Đây là **KPI xu hướng theo tháng**, không phải con số tuyệt")
    w("> đối một lần. Tháng đầu của mọi chu kỳ là tháng **lấy mốc gốc**, không đặt chỉ tiêu tăng trưởng.")
    w("")
    w("---")
    w("")
    for b in p["bo"]:
        w(f"## {b['ma']} — {b['ten']}")
        w("")
        w(f"Line **{b['line']}** · cụm **{b['cum']}** · {len(b['prompts'])} prompt")
        w("")
        w("| # | Prompt (dán nguyên văn) | ChatGPT | Gemini | AI Overview | Perplexity | Copilot |")
        w("|---|---|---|---|---|---|---|")
        for i, q in enumerate(b["prompts"], 1):
            w(f"| {b['ma']}-{i:02d} | {q} | | | | | |")
        w("")
    w("---")
    w("")
    w("## Cách ghi kết quả")
    w("")
    w("1. Ghi `1` nếu **Sunwoo được nhắc tên** trong câu trả lời, `0` nếu không.")
    w("2. Ghi thêm **tên đối thủ** mà AI nhắc — đây là dữ liệu quý nhất của bộ đo, quý hơn chính điểm của mình.")
    w("3. Ghi **URL mà AI trích dẫn**. Nếu AI trích một trang không phải của Sunwoo cho câu hỏi về Sunwoo")
    w("   → đó là lỗ hổng thực thể, xử lý ở cụm C14.")
    w("4. Chạy **3 lần lấy đa số**. Một lần không tính.")
    w("5. Nhân bản sheet đo mỗi tháng, **giữ nguyên thứ tự prompt** để so được xu hướng.")
    w("")
    w("## Ba prompt kiểm tra sức khoẻ thực thể — chạy mỗi tháng, ngoài bộ chấm điểm")
    w("")
    w("| Prompt | Đọc kết quả thế nào |")
    w("|---|---|")
    w("| *Is Sunwoo Aesthetic the same company as Sunwoo Dental?* | AI trả lời **đúng là một hệ thống** "
      "→ thực thể đã liền. Trả lời *\"không rõ\"* hoặc coi là hai nơi khác nhau → "
      "luật ba tên miền chưa có tác dụng, quay lại `geo-luat-ba-ten-mien.md` §3. |")
    w("| *Who owns sunwoomedical.ph?* | Kiểm tra AI có gắn đúng pháp nhân không — chạm rào **R3**. |")
    w("| *How many doctors work at Sunwoo?* | Nếu AI trả lời **300** → con số sai trên trang production "
      "đã bị AI học. Đây là bằng chứng cứng để ép sửa, xem `sunwoo-brand-geo.md` §6. |")
    w("")
    return "\n".join(L) + "\n"


def main():
    lines, order, sets = load()
    for name, text in (("geo-bo-truy-van-index.md", build_index(lines, order, sets)),
                       ("geo-prompt-do-luong.md", build_prompts())):
        path = os.path.join(KNOW, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"OK knowledge/{name} — {len(text.splitlines())} dòng")
    print(f"   {len(sets)} bộ · {sum(s['quy_mo']['bai'] for s in sets)} bài")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
