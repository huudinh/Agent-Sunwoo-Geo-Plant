# CÂU LỆNH — SUNWOO GEO PLANNER

Version 1.0 · Cập nhật 2026-11-10

---

# 1. CÔNG THỨC RA LỆNH

```
[PHẠM VI]  +  [SỐ THÁNG]  +  [THÁNG BẮT ĐẦU]  +  [đầu ra muốn gì]
```

Thiếu **phạm vi** hoặc **số tháng** → Agent sẽ hỏi lại. Thiếu giá, downtime, mốc traffic → Agent vẫn làm và ghi `⚠ Cần Sunwoo xác nhận`.

---

# 2. 12 PROMPT MẪU

### Nhóm A — tra dữ liệu

```
1. Sunwoo có bao nhiêu bộ truy vấn, bao nhiêu cụm, bao nhiêu bài cần sản xuất?
   Cắt theo từng line.

2. Trong bộ Xline Thread Lift, năm cụm Tầng A là những cụm nào, vì sao cụm đó
   lên Tầng A, và mỗi cụm cần bao nhiêu bài?

3. Những cụm nào bắt buộc xuất bản trên sunwoomedical.ph? Tổng cộng bao nhiêu
   bài dồn về tên miền trục?

4. Rào BỀN là gì, bộ nào chịu rào này nặng nhất, và trả lời nó bằng nội dung
   kiểu gì?
```

### Nhóm B — lập kế hoạch

```
5. Lập kế hoạch GEO toàn hệ thống Sunwoo trong 6 tháng, bắt đầu từ tháng
   01/2027. Xuất file 2 TAB theo mẫu.

6. Lập kế hoạch 4 tháng từ 03/2027, chỉ hai line SWM và SWA (tạm bỏ nha khoa
   vì chưa có nha sĩ). Nêu rõ trần thẩm định bác sĩ.

7. Lập kế hoạch 3 tháng chỉ cho bộ Smart Bio Implant và Porcelain veneers.
   Tôi biết line này đang bị chặn — tôi cần thấy quy mô việc để đi tuyển nha sĩ.

8. Kế hoạch 12 tháng từ 01/2027, có mở thêm một mảng wellness ở quý 4.
   Nêu rõ nên mở bằng subfolder hay tên miền thứ tư, vì sao.
```

### Nhóm C — vận hành & kiểm soát

```
9. Tháng Setup phải làm đủ những việc gì? Việc nào là cổng chặn, nếu bỏ thì
   hỏng ở đâu?

10. Viết giúp tôi mô tả công việc chi tiết cho cụm C06 của bộ PicoSure Pro,
    đúng chuẩn cột "Công việc chi tiết" — ghi rõ cụm, tầng, giai đoạn, trang
    đích và rào pháp lý.

11. Rà bản kế hoạch này theo checklist §14 và chỉ ra chỗ nào chưa đạt.

12. Liệt kê toàn bộ claim trong kế hoạch cần pháp chế duyệt, theo mẫu
    CLAIMS PENDING LEGAL REVIEW.
```

---

# 3. MẸO RA LỆNH

| Muốn gì | Nói thế nào |
|---|---|
| Đổi trần sản lượng | *"Giả định mỗi bác sĩ duyệt được 30 bài/tháng, lập lại kế hoạch"* |
| Chỉ Tầng A | *"Chỉ đưa Tầng A vào chu kỳ, Tầng B–C đẩy backlog"* |
| Thấy quy mô line bị chặn | *"Vẫn lập đủ cho line nha khoa, đánh dấu BLOCKED"* |
| Bảng phẳng để dán Sheets | *"Xuất thêm bảng phẳng, mỗi ô một giá trị, không gộp ô"* |
| Chỉ sửa một phần | *"Giữ nguyên các tháng khác, chỉ lập lại tháng 3"* |

---

# 4. AGENT SẼ TỪ CHỐI — VÀ ĐỀ XUẤT CÁCH KHÁC

| Bạn yêu cầu | Agent làm gì |
|---|---|
| *"Viết headline #1 K-beauty clinic in the Philippines"* | **Từ chối** — rào **R6** (ASC). Đề xuất định vị không so thứ bậc |
| *"Thêm câu guaranteed results cho mạnh"* | **Từ chối** — rào **R1**. Đề xuất bảo đảm **quy trình** có T&C |
| *"Điền tạm giá 15.000 PHP cho thread lift"* | **Từ chối** — ⛔ không tự tạo giá. Ghi `⚠ Cần Sunwoo xác nhận` |
| *"Cho bác sĩ da liễu thẩm định bài implant cho nhanh"* | **Từ chối** — rào **R4**. Đề xuất giữ `[BLOCKED]` và đẩy việc tuyển nha sĩ lên tháng Setup |
| *"Copy bài filler sang cả ba tên miền cho phủ rộng"* | **Từ chối** — vi phạm **L6** luật ba tên miền. Đề xuất viết một lần + liên kết |
| *"Dùng con số 300++ doctors cho ấn tượng"* | **Từ chối** — con số sai, và đưa việc sửa vào tháng Setup |
| *"Chạy trang vành đai cho Cebu và Davao"* | **Cảnh báo** — V4 ngoài Metro, mặc định không làm khi chưa có bằng chứng ca thật |

Agent **nêu đánh đổi rồi mới làm theo** nếu bạn vẫn quyết. Quyết định cuối thuộc về bạn — nhưng nó sẽ không im lặng làm.

---

# 5. CÂU LỆNH CHO SCRIPT

```bash
# sửa dữ liệu rồi sinh lại tri thức
python tools/build-index.py

# sinh 10 bộ truy vấn 6 sheet — bám mẫu mui.xlsx của Kangnam
python tools/build-botruyvan.py
python tools/build-botruyvan.py --scope threadlift,implant

# kế hoạch 6 tháng toàn hệ thống
python tools/build-geo-plan.py --start 2027-01 --months 6

# chỉ hai line đang chạy được
python tools/build-geo-plan.py --start 2027-01 --months 6 \
  --scope brand,mesohair,filler,threadlift,acne,picosure

# nới trần thẩm định sau khi Sunwoo xác nhận năng lực thật
python tools/build-geo-plan.py --start 2027-01 --months 6 --tran 30

# chỉ Tầng A
python tools/build-geo-plan.py --start 2027-01 --months 3 --tiers A
```
