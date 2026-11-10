# KHUNG KPI GEO SUNWOO — 5 TRỤ CỘT & CÁCH ĐẶT CHỈ TIÊU

Version 1.0 · Cập nhật 2026-11-10 · Agent dùng file này để **đặt số** cho TAB KPI.
Nguyên tắc xuyên suốt: **tính được thì đưa số · không tính được thì đề xuất mức tăng trưởng % · ⛔ tuyệt đối không bịa số tuyệt đối.**

---

# 1. NĂM TRỤ CỘT & TRỌNG SỐ

| # | Trụ cột KPI | Bản chất đo | Trọng số | Nguồn số |
|---|---|---|---|---|
| 1 | **Hạ tầng 3 tên miền & Thực thể** | Schema thực thể nối ba tên miền · NAP · GBP · tải trang <2s | **0,10** | Team Tech/Dev |
| 2 | **Sản lượng bài viết** | Số bài **phát hành** / tháng theo từng line | **0,20** | ✅ Tính được từ `geo-bo-truy-van-index.md` |
| 3 | **SEO & GEO AI Search** | Top 3/5/10 `google.com.ph` + tỷ lệ được nhắc trên 5 nền tảng AI | **0,40** | Rank tracker + 36 prompt đo GEO |
| 4 | **Traffic** | Organic `google.com.ph` + **Traffic AI** (referral từ LLM) | **0,15** | GA4 (cross-domain) |
| 5 | **Lead & Booking** | Form → trả lời Messenger → đặt lịch → **đến khám** | **0,15** | CRM / sổ lịch hẹn |
| | **Tổng** | | **1,00** | |

Trọng số điều chỉnh được theo mục tiêu kỳ. Đổi trọng số → giữ tổng = 1,00 và ghi chú lý do.

**Trọng số đánh giá theo tháng** (chu kỳ 4 tháng): Setup **20%** · Tăng tốc **25%** · Đột phá **30%** · Về đích **25%**. Chu kỳ khác số tháng → chia lại theo cùng logic: tháng đầu thấp nhất, tháng áp chót cao nhất.

> ⚠️ **Bốn khác biệt so với bộ Kangnam** — đây là lý do không copy nguyên bảng KPI cũ:
> ① Trụ cột 1 đổi từ *"Hạ tầng Web & Hub"* sang **"Hạ tầng 3 tên miền & Thực thể"**, vì bài toán của Sunwoo là **nối thực thể**, không phải dựng hub.
> ② Trụ cột 2 đếm theo **bài PHÁT HÀNH**, không đếm bài viết xong — vì cổng duyệt bác sĩ có thật và có thể chặn.
> ③ Trụ cột 4 đo `google.com.ph`, không phải `google.com.vn`.
> ④ Trụ cột 5 có thêm mắt xích **Messenger** — ở Philippines đây là đường chốt chính, không phải tổng đài.

---

# 2. TRỤ CỘT 1 — HẠ TẦNG 3 TÊN MIỀN & THỰC THỂ *(0,10)*

Trụ cột trọng số nhỏ nhất nhưng là **điều kiện cần** của bốn trụ cột còn lại. Sáu hạng mục, chấm đạt/không đạt:

| Hạng mục | Đạt khi |
|---|---|
| Schema `Organization` + `parentOrganization` + `sameAs` trên cả ba tên miền | ✅ |
| NAP khớp từng ký tự trên ba tên miền + Google Business Profile | ✅ |
| Mỗi bác sĩ có **đúng một** URL hồ sơ trong toàn hệ thống | ✅ |
| GA4 cross-domain tracking ba tên miền + tách được kênh LLM | ✅ |
| Tải trang < 2s trên 3G mô phỏng (phần lớn khách PH vào bằng điện thoại) | ✅ |
| Prompt *"Is Sunwoo Aesthetic the same company as Sunwoo Dental?"* → AI trả lời đúng | ✅ |

Ô cuối là **thước đo thật** của trụ cột này. Năm ô trên là việc; ô cuối là kết quả.

---

# 3. TRỤ CỘT 2 — SẢN LƯỢNG BÀI VIẾT *(0,20)* — trụ cột duy nhất được đưa số tuyệt đối tự tính

## 3.1 Nguồn khối lượng
`knowledge/geo-bo-truy-van-index.md` → cột **Bài** của từng cụm. Tổng kho: **204 bài** trên 150 cụm của 10 bộ.

## 3.2 Quy trình quy đổi khối lượng → chỉ tiêu tháng

```
Bước 1  Lọc phạm vi        → người dùng chọn line / bộ nào vào kế hoạch
Bước 2  Lọc tầng           → mặc định A + B trong chu kỳ; C chạy nền; D đẩy backlog
Bước 3  Gộp cụm 🏠         → C08·C12·C13·C14 của nhiều bộ dùng chung trang trên hub,
                             ⛔ KHÔNG cộng dồn thành nhiều trang
Bước 4  Cộng số bài        → ra tổng khối lượng chu kỳ
Bước 5  Rải sóng → tháng   → §6.1 của geo-phuong-phap-luan.md
Bước 6  ⛔ ÁP TRẦN BÁC SĨ   → ≤24 bài/bác sĩ/tháng; vượt trần thì GIÃN, không ép
Bước 7  Cân bằng           → chênh lệch tháng cao/thấp ≤25% (trừ tháng Setup)
Bước 8  Gộp theo line      → SWM · SWA · SWD để lên dòng KPI
```

⚠️ **Bước 3 và bước 6 là hai bước bộ Kangnam không có.** Bỏ bước 3 → đếm trùng khối lượng hub. Bỏ bước 6 → ra một kế hoạch đẹp mà không ai thực hiện được.

## 3.3 Hệ số quy đổi nhân lực

| Nhóm | Loại bài | Độ dài | Hệ số |
|---|---|---|---|
| A1 | Bài trụ / pillar / trang dịch vụ chính | 2.000–2.750 từ | **1,5** |
| A2 | Bài thường / tình huống / FAQ dài | 1.400–1.750 từ | **1,0** |
| A3 | Trang vành đai / FAQ ngắn / khối nhúng | <1.400 từ | **0,5** |

**Điểm quy đổi tháng** = Σ(số bài × hệ số). Vượt năng lực đã biết → **cảnh báo và đề xuất giãn tiến độ**, ⛔ không im lặng nhận chỉ tiêu không khả thi.

## 3.4 Hai cột khác nhau — đừng gộp

| Cột | Nghĩa | Ai chặn |
|---|---|---|
| **Đã sản xuất** | Bài viết xong, chờ duyệt | Đội content |
| **Đã phát hành** ★ | Bài đã qua bác sĩ + pháp chế và đang online | Cổng R4 · R9 |

**KPI tính theo cột "Đã phát hành".** Line SWD có thể sản xuất đầy đủ mà phát hành bằng 0 — bảng phải nhìn ra điều đó ngay, không giấu.

---

# 4. TRỤ CỘT 3 — SEO & GEO AI SEARCH *(0,40 — cao nhất)*

## 4.1 Hai nhánh đo song song

**Nhánh A — Google truyền thống:** số từ khoá ở Top 3 / Top 5 / Top 10 trên `google.com.ph`, tách theo từng tên miền.

**Nhánh B — GEO AI Search (nhánh chiến lược):** số truy vấn mà Sunwoo **được nhắc tên** trên **ChatGPT · Gemini · Google AI Overview · Perplexity · Copilot**.

⚠️ Thêm **Perplexity** và **Copilot** so với bộ Kangnam. Lý do: thị trường Philippines dùng tiếng Anh, và nội dung tiếng Anh được các công cụ này phủ rộng hơn hẳn so với nội dung tiếng Việt — bỏ hai nền tảng này là bỏ phần đo rẻ nhất.

## 4.2 Giao thức đo
Xem `geo-prompt-do-luong.md`. Tóm tắt: ẩn danh · dán nguyên văn · ghi 1/0 · **3 lần lấy đa số** · ghi thêm đối thủ AI nhắc · ghi URL AI trích · nhân bản sheet mỗi tháng · **khoá bộ đo từ tháng Setup**.

## 4.3 Đặt chỉ tiêu
Cần **số hiện tại** làm mốc. Chưa có → cột *"Hiện tại"* ghi `⚠ Cần Sunwoo xác nhận`, cột chỉ tiêu ghi **% tăng trưởng**. Tháng đầu của mọi chu kỳ là **tháng lấy mốc gốc**, ⛔ không đặt chỉ tiêu tăng trưởng.

## 4.4 Ba chỉ số phụ đáng theo hơn cả điểm chính

| Chỉ số | Vì sao quan trọng |
|---|---|
| **Đối thủ được AI nhắc** | Cho biết AI đang coi ai là nguồn cho thị trường Taguig — quý hơn điểm của chính mình |
| **URL được AI trích** | AI trích trang nào của Sunwoo → biết loại nội dung nào đang ăn, nhân bản hướng đó |
| **AI trích trang NGOÀI Sunwoo cho câu hỏi VỀ Sunwoo** | Lỗ hổng thực thể. Xử lý ở cụm C14, không xử lý bằng viết thêm bài dịch vụ |

---

# 5. TRỤ CỘT 4 — TRAFFIC *(0,15)*

Hai dòng cho **mỗi tên miền** (không gộp ba tên miền thành một dòng — gộp là mất chính thông tin cần nhất):

- **`google.com.ph`** — organic truyền thống.
- **Traffic AI** — phiên đến từ ChatGPT · Gemini · Claude · Perplexity · Copilot.

**Mốc nền:** `⚠ Cần Sunwoo xác nhận` — chưa có GA4 tách kênh LLM trên cả ba tên miền. Đây là việc của tháng Setup.

**Chỉ tiêu phụ:** Time-on-site > 2,5 phút · tỷ lệ truy cập từ điện thoại (PH rất cao, ảnh hưởng tới quyết định tải trang).

**Cách đặt chỉ tiêu:** dựa trên tốc độ tăng của chính Sunwoo sau khi có mốc gốc, ⛔ không lấy benchmark của Kangnam hay thị trường Việt Nam — khác ngôn ngữ, khác nền tảng AI, khác quy mô.

---

# 6. TRỤ CỘT 5 — LEAD & BOOKING *(0,15)*

Chuỗi đo của Philippines có **năm** mắt xích, không phải bốn:

```
Form / Messenger  →  Phòng khám trả lời  →  Đặt lịch  →  ĐẾN KHÁM  →  Điều trị
```

| Mắt xích | Ghi chú |
|---|---|
| **Form / Messenger** | Ở PH Messenger thường nhiều hơn form. Phải đếm **cả hai**, tách nguồn |
| **Phòng khám trả lời** | ⚠ Mắt xích hay rơi nhất và không ai đo. Đề xuất đo **thời gian phản hồi trung vị** |
| **Đặt lịch** | — |
| **ĐẾN KHÁM** ★ | **Đơn vị đo thật của gói này.** ⛔ Không tối ưu theo CPL — lead rẻ ở vành đai V4 là lead không bao giờ đến |
| **Điều trị** | `⚠ Cần Sunwoo xác nhận` |

⛔ **Rào R11:** ⛔ không gửi trường *"Service of interest"* vào pixel quảng cáo — đó là dữ liệu sức khoẻ.

⚠️ **Đề xuất kỹ thuật bắt buộc:** trường `Your area` trên form phải đổi từ ô text tự do sang **dropdown V1/V2/V3/V4 + Other**. Không có việc này thì không cắt được báo cáo theo vành đai, và cụm C04 không có cách nào chứng minh hiệu quả.

---

# 7. BỐN GIAI ĐOẠN CỦA MỘT CHU KỲ

| Giai đoạn | Trọng số | Việc đặc trưng |
|---|---|---|
| **Setup** | 20% | Khoá 36 prompt lấy mốc gốc · GA4 cross-domain · **dựng khối thực thể C14** · sửa 2 lỗi cổng chặn trên trang production · chuẩn hoá NAP + chốt 1 GBP · ban hành checklist từ cấm · nộp lô duyệt trước (R9) |
| **Tăng tốc** | 25% | Chạy hết Tầng A · dựng trang vành đai V1–V2 · liên kết ngược về hub 100% trang mới |
| **Đột phá** | 30% | Mở Tầng B · trang vành đai V3 cho dịch vụ giá trị ca cao · schema bác sĩ đầy đủ · tối ưu bài đã đăng theo kết quả đo GEO |
| **Về đích** | 25% | Tầng C chạy nền · hoàn thiện cross-sell ba mảng · **chấm lại Cơ hội GEO và chạy lại build-index** · chốt backlog kỳ sau |

---

# 8. DANH SÁCH ĐẦU VIỆC NỀN — luôn có trong mọi kế hoạch

| Mã | Trụ cột | Hạng mục | Xuất hiện ở |
|---|---|---|---|
| KPI-01 | Hạ tầng | Schema thực thể nối ba tên miền | Setup, rồi duy trì |
| KPI-02 | Hạ tầng | NAP · Google Business Profile · tải trang | Mọi tháng |
| KPI-03 | Tuyến nội dung | Quy chuẩn loại bài + checklist từ cấm (R1 · R6) | Setup, rồi duy trì |
| KPI-04 | Tuyến nội dung | Gắn thẻ tagging theo hành trình S1–S6 × line | Setup, rồi 100% bài mới |
| KPI-05…07 | Sản lượng | Theo từng line SWM · SWA · SWD | Mọi tháng |
| KPI-08 | Sản lượng | Trang vành đai V1–V3 | Mọi tháng |
| KPI-09 | Sản lượng | **Duyệt 2 lớp: bác sĩ đúng chuyên khoa + pháp chế (R4)** | Mọi tháng |
| KPI-10 | SEO & GEO | Top từ khoá `google.com.ph` | Mọi tháng |
| KPI-11 | SEO & GEO | Đo GEO — 36 prompt × 5 nền tảng | Mọi tháng |
| KPI-12 | Traffic | Traffic & Time-on-site theo từng tên miền | Mọi tháng |
| KPI-13 | Lead | Chuỗi Form/Messenger → trả lời → đặt lịch → **đến khám** | Mọi tháng |
| KPI-14 | Pháp lý | **Duyệt trước khi phát (FDA PH · ASC — R9)** | Setup, rồi theo lô |
| KPI-15 | Pháp lý | **Xác minh & công bố nha sĩ có PRC** — mở khoá line SWD | Setup, tới khi xong |

Agent được thêm mã KPI-16+ khi phạm vi mở rộng, ⛔ **không được bỏ** 15 mã nền này.
