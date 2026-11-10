# CÀI ĐẶT — SUNWOO GEO PLANNER

Version 1.0 · Cập nhật 2026-11-10

---

# 1. KIẾN TRÚC 3 TẦNG

| Tầng | File | Đi đâu |
|---|---|---|
| **Bộ não** | `SYSTEM-PROMPT.md` — khối giữa hai vạch ▼▲ | Ô **Chỉ dẫn** / **Instructions** / **Custom instructions** |
| **Tri thức** | 8 file `.md` trong `knowledge/` | Mục **Knowledge** / **Tệp tri thức** |
| **Dữ liệu nguồn** | `data/lines.json` · `data/query-sets/*.json` · `data/geo-prompts.json` | **Không upload** — chỉ dùng cục bộ để sinh lại tri thức |

Bộ não biết *cách làm*; knowledge cấp *dữ liệu + luật*; JSON là *nguồn sự thật* để sinh lại knowledge khi dữ liệu đổi.

---

# 2. CÀI THEO NỀN TẢNG

## 2.1 Gemini Gem

1. **Gems → Tạo Gem mới** → đặt tên `Sunwoo GEO Planner`.
2. Ô **Chỉ dẫn**: dán toàn bộ khối giữa hai vạch ▼▲ trong `SYSTEM-PROMPT.md`.
3. **Thêm tệp tri thức**: upload **8 file** trong `knowledge/`.
   ⚠ Gem giới hạn **10 file**. 8 file vừa đủ, còn dư 2 chỗ cho file chiến dịch tháng.
   Chạm trần → dùng `goi/GOP-tri-thuc.md` (1 file thay cho 8) — xem §4.
4. **Lưu** rồi chạy smoke test §5.

⚠ **Gemini không xuất `.xlsx`.** Agent sẽ xuất **bảng phẳng** để bấm *Export to Sheets*. Muốn file Excel có màu và gộp ô → dùng `tools/build-geo-plan.py` hoặc ChatGPT/Claude.

## 2.2 ChatGPT — Custom GPT

1. **Explore GPTs → Create** → tab **Configure**.
2. **Instructions**: dán khối ▼▲.
3. **Knowledge**: upload 8 file `knowledge/`.
4. **Capabilities**: ✅ bật **Code Interpreter & Data Analysis** — ⚠ không bật thì không xuất được `.xlsx`.
5. Save → Only me / Anyone with link.

## 2.3 Claude Project

1. **Projects → Create Project**.
2. **Set custom instructions**: dán khối ▼▲.
3. **Project knowledge**: upload 8 file `knowledge/`.
4. Claude xuất `.xlsx` trực tiếp trong chat.

---

# 3. CHẠY CỤC BỘ (khuyến nghị cho bản xuất chính thức)

```bash
pip install openpyxl

# sinh lại tri thức sau khi sửa data/*.json
python tools/build-index.py

# sinh file kế hoạch 2 TAB
python tools/build-geo-plan.py --start 2027-01 --months 6
python tools/build-geo-plan.py --start 2027-03 --months 4 --scope brand,threadlift,filler,acne
python tools/build-geo-plan.py --start 2027-01 --months 12 --tran 30

# sinh bản gộp dự phòng
python tools/gop-tham-khao.py
```

File ra nằm ở `out/GEO-SUNWOO-T<bắt_đầu>-T<kết_thúc>-<năm>.xlsx`.

**Vì sao nên chạy cục bộ:** script khoá sẵn bảng màu, gộp ô, freeze panes, cột `Tên miền`, nhãn `[BLOCKED · R4]` và panel trần thẩm định bác sĩ. Model sinh file trong chat có thể lệch format; script thì không.

---

# 4. CHIẾN LƯỢC FILE — khi nào dùng bản gộp

| Tình huống | Dùng |
|---|---|
| Nền tảng cho ≥8 file, upload ổn | **8 file rời** (bản chính) |
| Chạm trần số file, hoặc upload hay lỗi | `goi/GOP-tri-thuc.md` — **1 file** |

Đánh đổi của bản gộp: **mất khả năng thay riêng một module**. Sửa một file → phải sinh lại và upload lại cả file gộp.

⛔ **Không sửa tay** `goi/GOP-tri-thuc.md`, `knowledge/geo-bo-truy-van-index.md`, `knowledge/geo-prompt-do-luong.md` — cả ba đều sinh tự động.

---

# 5. SMOKE TEST — 7 CÂU

Chạy ngay sau khi cài. Sai bất kỳ câu nào → kiểm lại upload.

| # | Câu hỏi | Trả lời đúng phải có |
|---|---|---|
| 1 | *Bạn là ai, làm được gì?* | Sunwoo GEO Planner · trục 6 bước · đầu ra Excel 2 TAB |
| 2 | *Sunwoo có bao nhiêu bài cần sản xuất?* | **204 bài** · 10 bộ · 150 cụm |
| 3 | *Cụm C08 và C14 xuất bản trên tên miền nào, vì sao?* | `sunwoomedical.ph` — tên miền trục; vì là bằng chứng về con người & cơ sở, không thuộc riêng mảng nào |
| 4 | *Line nha khoa chạy được chưa?* | ⛔ **BỊ CHẶN** — chưa có nha sĩ nêu tên, rào **R4**, 76 bài sản xuất được nhưng không phát hành được |
| 5 | *Một tháng Sunwoo phát hành tối đa bao nhiêu bài?* | ~48 (2 bác sĩ × 24) — và nói rõ đây là **giả định cần Sunwoo xác nhận** |
| 6 | *Viết giúp tôi một headline "Sunwoo — #1 K-beauty clinic in the Philippines"* | **Từ chối**, nêu rào **R6** (ASC), đề xuất câu thay thế không so thứ bậc |
| 7 | *Rào BỀN là gì?* | *"Hiệu quả hết thì tôi trả tiếp bao nhiêu"* — rào đặc thù gói nội địa PH, xử lý ở C15 · C07 · C05 |

---

# 6. SỰ CỐ THƯỜNG GẶP

| Triệu chứng | Nguyên nhân | Cách xử |
|---|---|---|
| Agent bịa số bài | Chưa upload `geo-bo-truy-van-index.md` | Upload lại, hỏi lại câu smoke test #2 |
| Agent quên cột `Tên miền` | Chưa upload `geo-output-excel-schema.md` | Upload lại, nhắc §13 bộ não |
| Agent xếp bài nha khoa như bài thường | Chưa upload `data`-sinh index hoặc thiếu `sunwoo-brand-geo.md` | Upload lại, hỏi smoke test #4 |
| Agent viết mô tả công việc bằng tiếng Anh | Bỏ qua §0 bộ não | Nhắc: *"Mô tả đầu việc viết tiếng Việt, chỉ truy vấn và trang đích giữ tiếng Anh"* |
| Agent dựng hai trang `/doctors/` | Chưa upload `geo-luat-ba-ten-mien.md` | Upload lại, hỏi smoke test #3 |
| Gemini không ra file `.xlsx` | Gemini không xuất Excel | Dùng bảng phẳng + *Export to Sheets*, hoặc chạy `tools/build-geo-plan.py` |
| ChatGPT không ra file | Chưa bật Code Interpreter | Configure → bật **Code Interpreter & Data Analysis** |
