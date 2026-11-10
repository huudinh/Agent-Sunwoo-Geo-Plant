# CHANGELOG

---

## v1.3 — 2026-11-10 · Sửa lỗi hiển thị thật: dòng mô tả không gộp ô

v1.2 sửa nhầm chỗ. Lỗi thật không nằm ở nội dung mà ở **hình học bảng**, và chỉ lòi ra khi **vẽ sheet thành ảnh** để nhìn — soát bằng mã thì mọi thứ đều "hợp lệ".

**Nguyên nhân.** Hai dòng mô tả dưới tiêu đề của mọi sheet được ghi bằng `put(ws, 2, 1, "<250 ký tự>")`. Ô đó rơi vào **cột A**, mà cột A ở sheet 3–6 chỉ rộng **6–10 ký tự** (cột `#`, `ID`, `HẠNG`, `MÃ`). Cộng thêm `wrap_text=True` và chiều cao mặc định **15pt**, Excel cắt câu 250 ký tự còn đúng một mẩu.

| Sheet | Cột A rộng | Cần | Có | Hiện ra |
|---|---|---|---|---|
| 3 · Bộ truy vấn Master | 10 | 404pt | 15pt | mất 96% câu |
| 5 · Prompt đo lường | 6 | 451pt | 15pt | mất 97% câu |
| 6 · Rào pháp lý | 7 | 368pt | 15pt | mất 96% câu |
| 4 · Bản đồ nội dung | 8 | 356pt | 15pt | mất 96% câu |
| 1 · Hướng dẫn | 46 | 71pt | 15pt | mất ~4 dòng |
| 2 · Hành vi KH | 34 | 59pt | 15pt | mất ~3 dòng |

Mẫu Kangnam không dính vì nó **gộp `A2:P2` và `A3:P3`**. Bản sinh tự động thì không gộp — đó là toàn bộ câu chuyện, và nó giải thích vì sao tab 3–6 nặng hơn tab 1–2.

**Sửa.** Thêm helper `ghi_chu()`: gộp dòng mô tả ngang hết bảng **và tự tính chiều cao theo độ dài chữ**, không đặt cứng. Áp cho cả 6 sheet, gồm cả hai dòng chú thích của panel bên phải sheet 3. Kèm theo:

- Bảng *"cách dùng 6 sheet"* ở sheet 1: cột B/C nới từ 11/13 lên 22/24, chiều cao tính theo ô dài nhất.
- Bảng đếm tự động ở sheet 1 và dòng prompt ở sheet 5: chiều cao tính theo nội dung.
- Dòng *"Tháng đo"* ở sheet 5: gộp `A4:B4` và `C4:L4`.

**Hàng rào để lỗi này không quay lại:** `build-botruyvan.py` chạy `soat_hien_thi()` trước khi lưu từng file — quét mọi ô có `wrap_text`, so chiều cao cần với chiều cao thật, và **in cảnh báo kèm toạ độ ô** nếu chữ sẽ bị cắt. Lỗi loại này im lặng: file vẫn mở được, vẫn hợp lệ, không có gì báo. Giờ thì có.

Kết quả: **0 ô bị cắt chữ** trên cả 10 file × 6 sheet.

---

## v1.2 — 2026-11-10 · Sửa ba lỗi hiển thị của bộ truy vấn 6 sheet

Đối chiếu lại với `Knowledge/KN-BotruyvanGEO/mui.xlsx` thì tab 3–6 lệch mẫu ở ba chỗ. File không hỏng (không có ô gộp chồng nhau, không có ký tự điều khiển) — lỗi nằm ở **cách trình bày và cách chọn dữ liệu**.

| # | Lỗi | Hiện ra thế nào | Sửa |
|---|---|---|---|
| ① | **Cột % không có `number_format`** | Cột tên là *% ĐIỂM* nhưng Excel hiện `0.13`, cột *% LŨY KẾ* hiện `1`. Chạm tab 1 · 2 · 3 · 4 | Gán `0%` (tab 2 · 4) và `0.0%` (tab 3) đúng như mẫu Kangnam → hiện `13%` và `100%` |
| ② | **Tab 5 lấy prompt theo LINE** | File `acne` chứa prompt của Thread Lift · Meso · PicoSure, và **cả 10 prompt bị gán chung một mã cụm `C06`**. Phần tự bù lấy câu *ngắn nhất* nên lọt những câu hỏi nói với phòng khám (*"Do you have a branch in Alabang?"*) — không đo được Share of Voice | Lấy truy vấn **của chính bộ đó**, chấm theo *độ đo được* (có địa danh · ý định thương mại · so sánh) và loại câu hỏi ngôi thứ hai. Prompt vận hành cấp line tách khối riêng, ⛔ không gán mã cụm giả |
| ③ | **Rào pháp lý gán theo CỤM** | Cả 17 truy vấn của một cụm mang cùng một mã rào → mọi con số ở tab 6 đều là bội của 17, và **R10 không có truy vấn nào**. Bảng mất hết giá trị chẩn đoán | Gán theo **từng truy vấn**: nền từ *góc hỏi*, phủ thêm theo *nội dung câu hỏi*, tối đa 3 mã. Giờ R10 = 4 TV / 2 CORE — một điểm nóng thật, đúng kiểu R3 của bộ Kangnam |

**Thêm một hàng rào vận hành:** `build-botruyvan.py` gặp file đang mở trong Excel thì **báo rõ rồi đi tiếp**, không dừng cả mẻ. Trước đó một file bị khoá là 9 bộ còn lại cũng không được sinh.

---

## v1.1 — 2026-11-10 · Bổ sung bộ truy vấn 6 sheet

**Thiếu sót của v1.0:** repo chỉ có dữ liệu **cấp cụm**, không có **cấp truy vấn**. Bộ Kangnam có 17 file Excel 6 sheet trong `doc/BotruyvanGEO/` làm bản đồ giao việc cho đội content; bộ Sunwoo chưa có tương đương.

- **`tools/build-botruyvan.py`** — sinh 10 bộ truy vấn theo đúng **MẪU CHUẨN 6 SHEET** của `Knowledge/KN-BotruyvanGEO/mui.xlsx`: *1 Hướng dẫn & Chiến lược → 2 Hành vi KH → 3 Bộ truy vấn Master → 4 Bản đồ nội dung → 5 Prompt đo lường → 6 Rào pháp lý*.
- **`data/truy-van/*.json`** — **2.550 truy vấn tiếng Anh** (17 dòng/cụm × 150 cụm), mỗi dòng có góc hỏi · nhiệt độ · ưu tiên · từ khoá · brief · trang đích · rào pháp lý · đối tượng.
- **`doc/BoTruyVanGEO-Sunwoo/*.xlsx`** — 10 file đầu ra, giao thẳng cho đội content.

**Bốn chỗ cố ý khác mẫu Kangnam, đều có lý do:**

| # | Khác gì | Vì sao |
|---|---|---|
| ① | Hậu tố tên sheet rút ngắn | Excel cấm tên sheet >31 ký tự; `"Mũi"` chỉ 3 ký tự còn `"PicoSure"` là 8 |
| ② | Sheet 3 **thêm cột `TÊN MIỀN`** | Sunwoo chạy ba tên miền cho một phòng khám — truy vấn không nói rõ trang đích ở tên miền nào là truy vấn chưa giao xong. Cụm 🏠 C08/C12/C13/C14 tự định tuyến về tên miền trục |
| ③ | Sheet 2 có **bốn** rào cản thay vì ba | Thêm rào **BỀN**, đặc thù gói nội địa Philippines |
| ④ | Sheet 5 đo trên **năm** nền tảng | Thêm Perplexity · Copilot — thị trường PH nói tiếng Anh |

**Thêm vào sheet 1 mà mẫu gốc không có:** mục 4 *Định tuyến tên miền*, cảnh báo **trần thẩm định bác sĩ**, và banner đỏ **⛔ LINE BỊ CHẶN** cho 4 bộ nha khoa (dòng sheet 3 và 4 nền hồng, cột rào ghi `[BLOCKED · R4]`).

⚠ **Truy vấn là bản nháp v1** — mẫu câu suy từ khung 15 cụm, **chưa đối chiếu dữ liệu tìm kiếm thật của Philippines**. Sau tháng Setup phải soát lại bằng Google Search Console + kết quả bộ đo GEO.

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

### Trang hướng dẫn
- `tools/trang-huong-dan.py` + `tools/huong-dan.json` — dùng chung khuôn với `Agent-KN-GEO-Plant`, đổi bảng màu sang **teal #0E4F57 + amber #C98A2E** để khớp đúng file Excel 2 TAB.
- Bốn mục: Cài đặt · Prompt mẫu · **Năm điều phải biết** · Ranh giới. Hai điều giữa là hai ràng buộc riêng của Sunwoo (ba tên miền · cổng duyệt bác sĩ).
- Thang `V1→V4` của khuôn dùng đúng mục đích gốc: **vành đai đi lại Metro Manila**, gần → xa = nóng dần.
- Bản đã xuất: https://claude.ai/artifact/Ru4WTBr3QQWUmsTt5YRQ6W

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
| 12 | 🔶 **Đối chiếu 2.550 truy vấn v1 với dữ liệu tìm kiếm thật** (GSC + bộ đo GEO) — hiện là mẫu câu suy từ khung cụm | Độ chính xác của bản đồ giao việc | Team SEO/Content |
