# CHANGELOG

---

## v1.0 — 2026-11-10 · Bản đầu tiên

**Dựng mới toàn bộ, tham khảo `Agent-KN-GEO-Plant` (Kangnam) và `Agent-PR-GEO-Plant` (Paris).**

### Giữ nguyên từ bộ gốc
- Trục 6 bước · 6 giai đoạn hành trình S1–S6 · 4 tầng 80/20 · 6 quy tắc viết để AI trích dẫn.
- Công thức điểm ưu tiên (Giá trị ca × Nhiệt độ × Ưu tiên × Cơ hội GEO).
- Khung 15 cụm C01–C15 · quy ước 17 truy vấn/cụm · ánh xạ sóng → tháng · 4 giai đoạn chu kỳ.
- Đầu ra 2 TAB Excel · giao thức đo GEO (ẩn danh · 3 lần lấy đa số · đo xu hướng).

### Đổi hẳn, không phải dịch lại
| Hạng mục | Bộ Kangnam | Bộ Sunwoo |
|---|---|---|
| **Bài toán hạ tầng** | Một tên miền, dựng Hub | **Ba tên miền, nối thực thể** — thêm `geo-luat-ba-ten-mien.md` với 7 luật L1–L7 + bảng định tuyến cụm |
| **Rào cản nền** | 3 nỗi sợ ngành thẩm mỹ VN | **4 rào cản PH: NGỜ · NGẠI · SỢ · BỀN** — rào BỀN là rào đặc thù gói nội địa |
| **Cụm LOCAL C04** | Trang chi nhánh (8 hub + 19 tỉnh) | **Trang vành đai đi lại V1–V4** — một cơ sở, đo bằng phút kẹt xe |
| **Rào pháp lý** | 12 rào VN, nút thắt là GXNNDQC | **12 rào PH** (FDA RA 9711 · DOH · PRC · ASC · NPC RA 10173 · DTI), nút thắt là **duyệt trước khi phát** |
| **Trụ cột KPI 1** | Hạ tầng Web & Hub | **Hạ tầng 3 tên miền & Thực thể** |
| **Trụ cột KPI 3** | 3 nền tảng AI | **5 nền tảng** (thêm Perplexity · Copilot — thị trường nói tiếng Anh) |
| **Trụ cột KPI 5** | Form → sđt → đến cửa | **Form/Messenger → phòng khám trả lời → đặt lịch → ĐẾN KHÁM** |
| **TAB 2** | 10 cột | **11 cột** — thêm cột `Tên miền` |
| **Nguồn dữ liệu** | 17 file Excel | **JSON** (`data/query-sets/*.json`) — sinh index bằng script |

### Thêm mới, bộ gốc không có
- **Cổng duyệt bác sĩ** (`geo-phuong-phap-luan.md` §6.4) — trần ≤24 bài/bác sĩ/tháng; line nào không có bác sĩ đúng chuyên khoa thì `[BLOCKED · R4]`.
- **Dòng hồng `#F7DDDD`** trong TAB 2 — việc đã sản xuất nhưng chưa được phép phát hành.
- **Hai cột tách bạch**: *đã sản xuất* vs *đã phát hành*. KPI tính theo cột sau.
- **Định tuyến tên miền tự động** trong `build-geo-plan.py` — cụm C08/C12/C13/C14 của mọi bộ về tên miền trục.
- **Khung mở line mới** — thêm mảng = 1 file JSON + 1 khối `lines.json`, không sửa bộ não.
- **Quy tắc ngôn ngữ hai lớp** (§0 bộ não) — truy vấn/trang đích tiếng Anh, vận hành tiếng Việt.

### Dữ liệu v1
- 10 bộ · 150 cụm · 2.550 truy vấn · **204 bài**.
- 36 prompt đo GEO tiếng Anh (P-BRAND 8 · P-LOCAL 8 · P-AES 10 · P-DEN 10) + 3 prompt kiểm tra sức khoẻ thực thể.
- Kế hoạch mẫu 6 tháng: `template/GEO-SUNWOO-MAU-6-THANG.xlsx`.

---

# ⚠ VIỆC CÒN TREO — xử theo thứ tự này

| # | Việc | Chặn gì | Ai |
|---|---|---|---|
| 1 | 🔴 **Chốt phạm vi giấy phép thật của cơ sở** (có gồm nha khoa không) | **Toàn bộ kế hoạch** — chưa có thì chỉ xuất bản nháp `[CHỜ PHÁP CHẾ DUYỆT]` | Pháp chế Sunwoo |
| 2 | 🔴 **Tên + số PRC của ít nhất một nha sĩ** | **Line SWD — 4 bộ, 76 bài** | HR + Pháp chế |
| 3 | 🔴 **Sửa 2 lỗi cổng chặn trên production** — "300++ doctors" và FAQ nêu dịch vụ ngoài phạm vi | Mọi nội dung mới | Pháp chế + Tech |
| 4 | ⚠ **Scar Treatment còn chạy không** — có trong form đặt lịch, không có trong mind map | Có thì phải bổ sung bộ truy vấn thứ 11 | Vận hành |
| 5 | ⚠ **Ba tên miền do một hay nhiều pháp nhân đứng tên** | Luật ba tên miền · rào R3 · quyết định 1 GBP hay 3 | Pháp chế |
| 6 | ⚠ **Số đăng ký FDA PH** của PicoSure Pro · filler · chỉ Xline · trụ implant | Mọi cụm C06 · C12 · rào R7 | Pháp chế |
| 7 | ⚠ **Hiện trạng thật của `sunwoomedical.ph` và `sunwoodental.ph`** — mới chỉ xác nhận được `sunwooaesthetic.ph` là one-page | Ước lượng công dựng trang | Tech |
| 8 | ⚠ **Năng lực thẩm định thật của bác sĩ** (bài/tháng) | Trần sản lượng toàn kế hoạch — hiện đang dùng giả định 24 | Vận hành |
| 9 | ⚠ **Bảng giá + số buổi + downtime từng dịch vụ** | Cụm C07 (32 bài) · C10 · C15 | Phòng khám |
| 10 | ⚠ **Có nhân sự nói tiếng Hàn không** | Nhóm N1 cộng đồng Hàn McKinley Hill · cụm C13 | Vận hành |
| 11 | 🔶 **Chấm lại Cơ hội GEO sau tháng Setup** rồi chạy lại `build-index.py` | Thứ hạng cụm hiện mới dựa trên 3/4 thừa số | Team SEO |
| 12 | 🔶 **Soạn lớp truy vấn chi tiết** (17 truy vấn EN/cụm) — hiện mới có cấp cụm | Bản đồ nội dung chi tiết cho đội content | Team SEO/Content |
