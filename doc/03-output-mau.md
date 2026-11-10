# OUTPUT MẪU — CÓ SỐ THẬT

Version 1.0 · Số liệu lấy từ `out/GEO-SUNWOO-T01-T06-2027.xlsx`, sinh bằng:

```bash
python tools/build-geo-plan.py --start 2027-01 --months 6
```

```
OK out/GEO-SUNWOO-T01-T06-2027.xlsx
   92 lát cụm · 204 bài · 6 tháng · 3 line · 3 tên miền
   Sản lượng theo tháng: Tháng 1=35(phát hành 25) · Tháng 2=34(phát hành 18)
                       · Tháng 3=34(phát hành 24) · Tháng 4=34(phát hành 23)
                       · Tháng 5=34(phát hành 18) · Tháng 6=33(phát hành 20)
   Trần thẩm định: 48 bài/tháng (2 bác sĩ × 24)  OK
```

---

# 1. ĐỌC HAI CON SỐ, KHÔNG PHẢI MỘT

| | Nghĩa | Tháng 1 |
|---|---|---|
| **Sản lượng** | Bài viết xong | **35** |
| **Phát hành** ★ | Bài đã qua bác sĩ + pháp chế và đang online | **25** |

Chênh lệch **10 bài** chính là line nha khoa — sản xuất được, ⛔ chưa phát hành được. **KPI tính theo cột phát hành.** Bảng phải nhìn ra điều này ngay ở dòng amber, không giấu xuống chú thích.

---

# 2. TAB 2 — KHỐI THÁNG 1/2027 (rút gọn)

```
════  THÁNG 1/2027  ·  giai đoạn SETUP  ·  hạn chót 31/01/2027  ════

KPI-01   1. Hạ tầng & Thực thể   Schema thực thể nối ba tên miền        cả ba              31/01/2027
KPI-02   1. Hạ tầng & Thực thể   NAP · GBP · tải trang                  cả ba              31/01/2027
KPI-03   2. Tuyến nội dung       Quy chuẩn loại bài & checklist từ cấm  cả ba              31/01/2027
KPI-04   2. Tuyến nội dung       Tagging hành trình S1–S6 × line        cả ba              31/01/2027

KPI-05.1 3. Sản lượng — SWM      🏠 Khối trên tên miền trục — bộ Acne   sunwoomedical.ph    2    2
KPI-05.2 3. Sản lượng — SWM      🏠 Khối trên tên miền trục — bộ Filler sunwoomedical.ph    2    2
KPI-05.3 3. Sản lượng — SWM      🏠 Khối trên tên miền trục — bộ Meso   sunwoomedical.ph    2    2
KPI-05.4 3. Sản lượng — SWM      🏠 Khối trên tên miền trục — bộ Brand  sunwoomedical.ph    6    6
KPI-05   3. Sản lượng — SWM      ▶ TỔNG SUNWOO MEDICAL CENTER          sunwoomedical.ph   12   12   ← mint

KPI-06.1 3. Sản lượng — SWA      Advanced Acne Treatment                sunwooaesthetic.ph  2    2
KPI-06.2 3. Sản lượng — SWA      Filler & HA collagen booster           sunwooaesthetic.ph  4    4
KPI-06.3 3. Sản lượng — SWA      Meso Hair Therapy                      sunwooaesthetic.ph  3    3
KPI-06.4 3. Sản lượng — SWA      Xline Thread Lift                      sunwooaesthetic.ph  4    4
KPI-06   3. Sản lượng — SWA      ▶ TỔNG SUNWOO AESTHETIC               sunwooaesthetic.ph 13   13   ← mint

KPI-07.1 3. Sản lượng — SWD      Nhổ răng khôn                          sunwoodental.ph     1    1   ← HỒNG
KPI-07.2 3. Sản lượng — SWD      Răng sứ & veneer                       sunwoodental.ph     4    4   ← HỒNG
KPI-07.3 3. Sản lượng — SWD      Smart Bio Implant                      sunwoodental.ph     5    5   ← HỒNG
KPI-07   3. Sản lượng — SWD      ▶ TỔNG SUNWOO DENTAL [BLOCKED · R4]   sunwoodental.ph    10   10   ← HỒNG
                                 hạn chót: ⛔ tính từ ngày có nha sĩ

KPI-TỔNG 3. Sản lượng bài viết   ★ TỔNG SẢN LƯỢNG THÁNG (toàn hệ thống) cả ba              35   35   ← amber
         → "Trong đó PHÁT HÀNH được: 25 bài · bị chặn bởi R4: 10 bài.
            Trần thẩm định bác sĩ tháng này: 48 bài"

KPI-08   Trang vành đai          Điều phối (không cộng sản lượng)       cả ba
KPI-09   Kiểm duyệt              Duyệt 2 lớp: BS đúng chuyên khoa + PC  cả ba
KPI-10   4. SEO & GEO            Top từ khoá google.com.ph              cả ba
KPI-11   4. SEO & GEO            Đo GEO — 36 prompt × 5 nền tảng        cả ba
KPI-12   5. Traffic              Traffic & Time-on-site theo tên miền   cả ba
KPI-13   5. Chuyển đổi           Form/Messenger → đặt lịch → ĐẾN KHÁM   cả ba
KPI-14   0. Pháp lý              Duyệt trước khi phát (FDA PH · ASC)    cả ba
KPI-00   0. Pháp lý              Sửa 2 lỗi cổng chặn trên production     cả ba
KPI-15   0. Pháp lý              ⛔ Xác minh & công bố nha sĩ PRC        sunwoodental.ph    ← HỒNG
```

---

# 3. CỘT `CÔNG VIỆC CHI TIẾT` — BA MẪU THẬT

**① Cụm trên tên miền trục (C14, tháng Setup):**
> Sản xuất theo bản đồ nội dung: **C14 BRAND ENTITY — Sunwoo across three domains & doctor profiles** (Tầng A · S3 · 6 bài → MỚI: `sunwoomedical.ph/about/`). Áp 6 quy tắc trích dẫn AI (BLUF · có số · phủ 8 góc hỏi · nói cả điều bất lợi · ngày cập nhật + BS thẩm định kèm PRC # · không nhồi từ khoá). Viết bằng English chuẩn, ⛔ không Taglish trên trang y khoa. Duyệt 2 lớp: BS đúng chuyên khoa (R4) + Pháp chế; nhóm chạm health product nộp duyệt trước (R9). 🏠 Cụm thuộc tên miền trục — gộp với cùng cụm của các bộ khác thành MỘT trang dùng chung, ⛔ không dựng trang trùng trên tên miền dịch vụ.

**② Cụm dịch vụ bình thường (C07 Thread Lift):**
> Sản xuất theo bản đồ nội dung: **C07 Price, packages & payment terms (Xline Thread Lift)** (Tầng A · S3 · 4 bài → MỚI: `sunwooaesthetic.ph/pricing/xline-thread-lift/`). Áp 6 quy tắc trích dẫn AI […]. Duyệt 2 lớp: BS đúng chuyên khoa (R4) + Pháp chế; nhóm chạm health product nộp duyệt trước (R9).

**③ Cụm bị chặn (C07 Implant):**
> **[BLOCKED · R4]** Sản xuất theo bản đồ nội dung: **C07 Price, packages & payment terms (Smart Bio Implant)** (Tầng A · S3 · 5 bài → MỚI: `sunwoodental.ph/pricing/smart-bio-implant/`). […] ⛔ **KHÔNG PHÁT HÀNH** cho tới khi Sunwoo công bố nha sĩ có giấy phép PRC.

---

# 4. PANEL PHẢI (cột M–N)

```
TỔNG SẢN LƯỢNG THEO THÁNG
  Tháng 1 (phát hành 25)        35
  Tháng 2 (phát hành 18)        34
  Tháng 3 (phát hành 24)        34
  Tháng 4 (phát hành 23)        34
  Tháng 5 (phát hành 18)        34
  Tháng 6 (phát hành 20)        33
  TỔNG CHU KỲ                  204

TRẦN THẨM ĐỊNH BÁC SĨ
  Trần phát hành / tháng        48
  Tháng cao nhất (đã phát hành) 25
  Còn dư                        23
  Trạng thái            ✅ trong trần

THỐNG KÊ TIẾN ĐỘ
  Tổng số đầu việc KPI         164
  Đã hoàn thành                  0
  Chưa hoàn thành              164
  Tiến độ chung                  0
```

---

# 5. DẤU HIỆU ĐÚNG / SAI

| ✅ Đúng | ❌ Sai — phải sửa trước khi gửi |
|---|---|
| Mọi dòng nội dung có **đúng một** tên miền | Dòng nội dung ghi *"cả ba"* |
| Cụm 🏠 chỉ xuất hiện trên `sunwoomedical.ph` | Có hai dòng dựng `/doctors/` trên hai tên miền |
| Dòng nha khoa **nền hồng**, hạn chót *"tính từ ngày có nha sĩ"* | Dòng nha khoa có hạn chót bình thường |
| `★ TỔNG` = Σ các dòng `▶ TỔNG` của tháng | Số tổng không cộng ra |
| Chênh lệch tháng cao/thấp ≤ 25% | Tháng 1 = 70 bài, tháng 6 = 12 bài |
| Phát hành/tháng ≤ trần thẩm định | 60 bài/tháng với 2 bác sĩ mà không có cảnh báo |
| Cột `Hiện tại` ghi `⚠ Cần Sunwoo xác nhận` | Cột `Hiện tại` có số tuyệt đối không ai cấp |
| Tháng Setup có đủ 7 việc + sửa 2 lỗi cổng chặn | Tháng Setup chỉ có việc viết bài |
| Mô tả công việc tiếng Việt, truy vấn/URL tiếng Anh | Mô tả công việc bằng tiếng Anh, hoặc truy vấn bị dịch sang tiếng Việt |

---

# 6. ĐỌC KẾ HOẠCH NÀY RA QUYẾT ĐỊNH GÌ

Ba con số đáng mang vào cuộc họp, không phải con số 204:

1. **25 / 35** — tỷ lệ phát hành được tháng đầu. Mỗi tháng có khoảng **10 bài nằm kho** vì thiếu một nha sĩ. Sáu tháng là **≈ 76 bài**. Đây là **chi phí thật của một vị trí tuyển dụng chưa làm**.
2. **48 bài/tháng** — trần thẩm định. Kế hoạch hiện dùng chưa tới một nửa. Nghĩa là nút thắt **không nằm ở bác sĩ**, mà ở việc dựng trang: ba tên miền đều gần như trống.
3. **2 lỗi cổng chặn** — con số *"300++ doctors"* và FAQ sai phạm vi. Hai việc sửa trong vài giờ, nhưng **chặn toàn bộ 204 bài phía sau**. Đây là việc rẻ nhất và phải làm trước nhất.
