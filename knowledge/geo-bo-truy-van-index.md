# GEO SUNWOO — CHỈ MỤC BỘ TRUY VẤN & BẢN ĐỒ NỘI DUNG

> Sinh tự động từ `data/query-sets/*.json` + `data/lines.json` bằng `tools/build-index.py`.
> **Không sửa tay file này** — sửa JSON nguồn rồi chạy lại script.
> Đây là **nguồn sự thật duy nhất về khối lượng công việc**: cột `Bài` của mỗi cụm là con số
> duy nhất được phép dùng để tính chỉ tiêu sản lượng.

**Tổng kho:** 10 bộ dịch vụ · 150 cụm chủ đề · 2550 truy vấn · **204 bài viết** cần sản xuất.

> 🔶 **TRẠNG THÁI DỮ LIỆU — BẢN NHÁP v1.** Toàn bộ số liệu dưới đây suy ra từ mind map Sunwoo
> ngày 2026-11-10 và hồ sơ thương hiệu đọc ngày 2026-10-23. **Sunwoo chưa có mốc traffic AI nào**,
> nên *Cơ hội GEO* của mọi cụm đang bằng **1** và điểm ưu tiên mới chỉ phản ánh giá trị doanh thu ×
> nhiệt độ × ưu tiên. Sau tháng Setup, khi đã khoá bộ đo và dựng xong GA4, **phải chấm lại Cơ hội GEO**
> **và chạy lại script này**. Trước bước đó, mọi thứ hạng cụm là giả định có căn cứ, không phải bằng chứng.

---

## Quy ước đọc bảng

| Ký hiệu | Nghĩa |
|---|---|
| Tầng A | CORE 80/20 — làm trong 90 ngày, **70% ngân sách nội dung** |
| Tầng B | Đòn bẩy chuyển đổi — mở khi A xong ~60%, **20%** |
| Tầng C | Uy tín & giữ chân — chạy nền, **10%** |
| Tầng D | Cửa vào rộng — **0% ngân sách mới**, chỉ pillar nền / tái sử dụng |
| S1…S6 | Giai đoạn hành trình khách — xem `geo-phuong-phap-luan.md` §2 |
| Sóng | S1 0–30 ngày · S2 31–60 ngày · S3 61–90 ngày · Nền sau 90 ngày |
| TV / CORE | Số truy vấn của cụm / trong đó bao nhiêu thuộc CORE 80/20 |
| Bài | Số bài cần sản xuất (`0` = tái sử dụng nội dung, không tính sản lượng mới) |
| 🏠 | Cụm **bắt buộc xuất bản trên tên miền trục** `sunwoomedical.ph` — xem `geo-luat-ba-ten-mien.md` |

## Ba line & trạng thái cổng chặn

| Mã | Line | Tên miền | Bộ | Bác sĩ thẩm định | Trạng thái |
|---|---|---|---|---|---|
| **SWM** | Sunwoo Medical Center — Thương hiệu tổng & trục thực thể | `sunwoomedical.ph` | 1 bộ | Dr. Emanuel F. Gatdula<br>Dr. Sharmaine Esquilona | ✅ chạy được |
| **SWA** | Sunwoo Aesthetic — Thẩm mỹ nội khoa & da liễu | `sunwooaesthetic.ph` | 5 bộ | Dr. Emanuel F. Gatdula — Diplomate, Philippine Dermatological Society<br>Dr. Sharmaine Esquilona — Certificate in Aesthetic Medicine (Level I), AMI Philippines | ✅ chạy được |
| **SWD** | Sunwoo Dental — Nha khoa | `sunwoodental.ph` | 4 bộ | ⛔ **chưa có** | ⛔ **BỊ CHẶN** |

> ⛔ **CỔNG CHẶN LINE SWD:** ⛔ CHƯA CÓ NHA SĨ ĐƯỢC NÊU TÊN. Hai bác sĩ đã công bố là bác sĩ da liễu và bác sĩ thẩm mỹ nội khoa — không ai thẩm định được nội dung nha khoa. Rào R4 (PRC) chặn toàn bộ bài y khoa của line này cho tới khi Sunwoo cung cấp tên + số giấy phép PRC của ít nhất một nha sĩ.

## Bảng tổng hợp khối lượng theo bộ

| # | Bộ dịch vụ | Line | Tên miền | Cụm | TV | Bài cần SX |
|---|---|---|---|---|---|---|
| 1 | Sunwoo Medical Center — brand & local | SWM | `sunwoomedical.ph` | 15 | 255 | **26** |
| 2 | Meso Hair Therapy — hair loss & scalp mesotherapy | SWA | `sunwooaesthetic.ph` | 15 | 255 | **20** |
| 3 | Filler & HA collagen booster — skin rejuvenation | SWA | `sunwooaesthetic.ph` | 15 | 255 | **20** |
| 4 | Xline Thread Lift — non-surgical lifting | SWA | `sunwooaesthetic.ph` | 15 | 255 | **22** |
| 5 | Advanced Acne Treatment — active acne & scarring | SWA | `sunwooaesthetic.ph` | 15 | 255 | **20** |
| 6 | PicoSure Pro — melasma, pigmentation & tone | SWA | `sunwooaesthetic.ph` | 15 | 255 | **20** |
| 7 | Smart Bio Implant — dental implants | SWD | `sunwoodental.ph` | 15 | 255 | **22** |
| 8 | Porcelain crowns & veneers — smile design | SWD | `sunwoodental.ph` | 15 | 255 | **20** |
| 9 | Wisdom tooth extraction — impacted third molars | SWD | `sunwoodental.ph` | 15 | 255 | **16** |
| 10 | General dentistry — check-up, cleaning & fillings | SWD | `sunwoodental.ph` | 15 | 255 | **18** |
| | **TỔNG** | | | **150** | **2550** | **204** |

**Khối lượng theo line:**

| Line | Bộ | Bài | % tổng |
|---|---|---|---|
| SWM · Thương hiệu tổng & trục thực thể | 1 | **26** | 13% |
| SWA · Thẩm mỹ nội khoa & da liễu | 5 | **102** | 50% |
| SWD · Nha khoa | 4 | **76** | 37% |

---

## 1. Thương hiệu tổng Sunwoo Medical Center

`brand.json` · **SWM** · `sunwoomedical.ph` · **26 bài cần sản xuất**

**Tên dùng trên site (EN):** Sunwoo Medical Center — brand & local

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Thương hiệu + Local) · hồ sơ thương hiệu đọc 2026-10-23

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 65% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① NGỜ — “Sunwoo là ba website khác nhau hay một phòng khám?” Khách tra ba tên miền ra ba thực thể rời, không biết ai đứng sau → cụm xử lý **C14 + C12 + C03** (51 truy vấn, 38 CORE)
- ② NGẠI — “McKinley Hill cách tôi bao xa, giờ tan tầm có kịp không, có chỗ đậu xe không” → cụm xử lý **C04 + C09 + C13** (51 truy vấn, 13 CORE)
- ③ NGỜ — “Bác sĩ trên quảng cáo có thật, có giấy phép PRC, có phải người trực tiếp khám không” → cụm xử lý **C08 + C12 + C14** (51 truy vấn, 40 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Sợ không phân biệt được beauty clinic không có bác sĩ với phòng khám có bác sĩ được PRC cấp phép. | C01 · C02 · C13 | 51 | 0 | 6% |
| S2 | ★★★ Quyết định đồng hạng | Sợ gõ “clinic near me” ra một nơi quá xa, hoặc đến nơi mới biết cơ sở không làm dịch vụ mình cần. | C03 · C04 · C05 · C12 | 68 | 25 | 31% |
| S3 | ★★★ Quyết định | NGỜ LÀ NỖI SỢ LỚN NHẤT của bộ này: ba tên miền, hai bác sĩ công bố, con số “300++ doctors” trên trang — khách đọc xong mất tin cả hệ thống. | C06 · C07 · C08 · C11 · C14 | 85 | 40 | 56% |
| S4 | ★★ | Sợ nhắn Messenger không ai trả lời, hoặc đến nơi phải chờ rồi phải quay lại lần nữa. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ làm xong thì không còn ai theo dõi; không biết liên hệ ai khi có vấn đề. | C10 | 17 | 0 | 2% |
| S6 | ★ Nền | Sợ bị bán chồng dịch vụ giữa ba mảng thẩm mỹ – nha – mảng mới. | C15 | 17 | 0 | 1% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 65% | 24 | 70% ngân sách nội dung · làm trong 90 ngày. C14 Thực thể ba tên miền · C04 Local vành đai Metro Manila · C08 Chọn phòng khám & bác sĩ · C12 Giấy phép PRC/FDA/DOH · C07 Phí tư vấn & bảng giá tổng. ⚠ C14 phải ra TRƯỚC MỌI CỤM KHÁC của mọi bộ — nó là khối thực thể nuôi cả ba tên miền. |
| B | 5 | 85 | 27% | 2 | 20% · mở khi Tầng A xong ~60%. C05 So sánh loại hình cơ sở · C11 Khiếu nại & chính sách làm lại · C09 Đặt lịch & tiếp nhận · C06 An toàn chung · C13 Cộng đồng Hàn · expat · OFW. Riêng C13 chỉ mở khi phòng khám xác nhận có nhân sự nói tiếng Hàn. |
| C | 3 | 51 | 6% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 Hệ sinh thái dịch vụ · C10 Theo dõi sau điều trị · C15 Cross-sell giữa ba mảng. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 15 | 18% | 6 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 2 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Sunwoo Medical Center) ⭐⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 14 | 15% | 8 | S1 (0–30n) | MỚI: sunwoomedical.ph/areas/ (hub) + 7 trang vành đai |
| 3 | C07 | Price, packages & payment terms (Sunwoo Medical Center) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 13 | 12% | 3 | S1 (0–30n) | MỚI: sunwoomedical.ph/pricing/clinic/ |
| 4 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 12 | 12% | 4 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 5 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice ⭐⭐ 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | A | S2 | 17 | 11 | 8% | 3 | S1 (0–30n) | MỚI: sunwoomedical.ph/credentials/ |
| 6 | C06 | Safety, risks & side effects (Sunwoo Medical Center) | An toàn, rủi ro & tác dụng phụ | B | S3 | 17 | 0 | 7% | 1 | S2 (31–60n) | MỚI: sunwoomedical.ph/guide/clinic-risks-and-side-effects/ |
| 7 | C11 | When results fall short — revision, correction & complaints (Sunwoo Medical Center) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 7% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/guide/clinic-revision/ |
| 8 | C05 | Comparison — methods, devices & alternatives (Sunwoo Medical Center) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/guide/clinic-vs-alternatives/ |
| 9 | C09 | Booking, consultation & the first visit (Sunwoo Medical Center) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/book-a-consultation/ |
| 10 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 4% | 1 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 11 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwoomedical.ph/services/ |
| 12 | C10 | Aftercare, downtime & recovery timeline (Sunwoo Medical Center) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoomedical.ph/guide/clinic-aftercare/ |
| 13 | C01 | Problem awareness — naming the condition (Sunwoo Medical Center) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoomedical.ph/guide/clinic-basics/ |
| 14 | C02 | Myths, home remedies & social-media beliefs (Sunwoo Medical Center) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoomedical.ph/guide/clinic-myths/ |
| 15 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Sunwoo Medical Center) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 1% | 0 | S3 (61–90n) | MỚI: sunwoomedical.ph/guide/clinic-how-long-it-lasts/ |

---

## 2. Meso Hair Therapy — rụng tóc & mesotherapy da đầu

`mesohair.json` · **SWA** · `sunwooaesthetic.ph` · **20 bài cần sản xuất**

**Tên dùng trên site (EN):** Meso Hair Therapy — hair loss & scalp mesotherapy

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ thẩm mỹ) · form đặt lịch sunwooaesthetic.ph

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 62% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① BỀN — “Ngưng là rụng lại phải không? Tôi phải trả tiền này đến bao giờ” → cụm xử lý **C15 + C07 + C05** (51 truy vấn, 23 CORE)
- ② NGẠI — Rụng tóc là chuyện riêng tư; sợ bị nhìn thấy khi bước vào phòng khám → cụm xử lý **C09 + C01 + C13** (51 truy vấn, 0 CORE)
- ③ NGỜ — “Tiêm vào da đầu có hại không, chất tiêm là gì, có đăng ký FDA PH không” → cụm xử lý **C06 + C12 + C08** (51 truy vấn, 37 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa gọi đúng tên tình trạng: rụng tóc nội tiết, telogen effluvium hay chỉ là stress. | C01 · C02 · C13 | 51 | 0 | 6% |
| S2 | ★★ | Sợ chọn sai hướng: mesotherapy, PRP, thuốc uống hay cấy tóc — mỗi nơi nói một kiểu. | C03 · C04 · C05 · C12 | 68 | 11 | 22% |
| S3 | ★★★ Quyết định | Sợ tiêm vào da đầu, sợ chất tiêm không rõ nguồn, sợ tổng chi phí cả liệu trình vượt dự tính. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 61% |
| S4 | ★★ | Sợ phải nghỉ làm, sợ đau trong buổi tiêm. | C09 | 17 | 0 | 5% |
| S5 | ★★ | Sợ rụng nhiều hơn trong 2–4 tuần đầu mà không biết đó là bình thường hay thất bại. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Sợ ngưng là rụng lại — đây là rào BỀN, rào đặc thù của gói nội địa Philippines. | C15 | 17 | 0 | 4% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 62% | 15 | 70% ngân sách nội dung · làm trong 90 ngày. C14 Thực thể · C04 Local · C08 Chọn bác sĩ (Diplomate PDS là bằng chứng mạnh nhất ở cụm này) · C07 Giá trọn liệu trình · C06 An toàn mũi tiêm. |
| B | 5 | 85 | 27% | 4 | 20% · mở khi Tầng A xong ~60%. C05 Meso vs PRP vs thuốc vs cấy tóc · C11 Không đáp ứng sau N buổi thì sao · C09 Đặt lịch & riêng tư · C12 Giấy phép · C13 Nhóm đặc thù. |
| C | 3 | 51 | 9% | 1 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 · C15 — riêng C15 là cụm trả lời rào BỀN, phải có ít nhất 1 bài dù ở Tầng C. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Safety, risks & side effects (Meso Hair Therapy) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 15 | 14% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-risks-and-side-effects/ |
| 2 | C07 | Price, packages & payment terms (Meso Hair Therapy) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 14 | 13% | 4 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/pricing/meso-hair-therapy/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 13% | 3 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Meso Hair Therapy) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 9% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/areas/ |
| 6 | C11 | When results fall short — revision, correction & complaints (Meso Hair Therapy) ⭐⭐ | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 8% | 1 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-revision/ |
| 7 | C05 | Comparison — methods, devices & alternatives (Meso Hair Therapy) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-vs-alternatives/ |
| 8 | C09 | Booking, consultation & the first visit (Meso Hair Therapy) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 5% | 1 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/book-a-consultation/ |
| 9 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 10 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 4% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 11 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Meso Hair Therapy) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 4% | 1 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-how-long-it-lasts/ |
| 12 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/services/ |
| 13 | C10 | Aftercare, downtime & recovery timeline (Meso Hair Therapy) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-aftercare/ |
| 14 | C01 | Problem awareness — naming the condition (Meso Hair Therapy) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-basics/ |
| 15 | C02 | Myths, home remedies & social-media beliefs (Meso Hair Therapy) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/meso-hair-therapy-myths/ |

---

## 3. Filler & HA collagen booster — trẻ hoá da

`filler.json` · **SWA** · `sunwooaesthetic.ph` · **20 bài cần sản xuất**

**Tên dùng trên site (EN):** Filler & HA collagen booster — skin rejuvenation

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ thẩm mỹ) · hồ sơ thương hiệu §2

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 66% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① SỢ — “Tiêm hỏng thì có tháo ra được không, tắc mạch có thật không” → cụm xử lý **C06 + C11 + C08** (51 truy vấn, 39 CORE)
- ② NGỜ — “Filler là hàng gì, có số đăng ký FDA PH không, có phải hàng xách tay” → cụm xử lý **C12 + C06 + C14** (51 truy vấn, 26 CORE)
- ③ BỀN — “6 tháng hay 18 tháng? Tan hết rồi mặt có xấu hơn trước không” → cụm xử lý **C15 + C07 + C05** (51 truy vấn, 12 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa phân biệt được filler, botox, booster và skin rejuvenation nói chung. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | Sợ chọn sai loại và sai vùng tiêm; sợ bị tư vấn theo hướng đắt tiền. | C03 · C04 · C05 · C12 | 68 | 11 | 22% |
| S3 | ★★★ Quyết định | SỢ BIẾN CHỨNG MẠCH MÁU là nỗi sợ chi phối. Kế đó là sợ hàng không rõ nguồn gốc. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 64% |
| S4 | ★★ | Sợ sưng bầm đúng dịp có sự kiện; cần mốc downtime thật. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ cục, sợ không đều, không biết khi nào là bất thường phải quay lại. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Sợ tan hết rồi phải tiêm lại mãi; cần nói thật chu kỳ dặm lại. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 66% | 15 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 · C08 · C07 · C06 — riêng C06 phải dẫn đầu về số bài vì biến chứng mạch máu là nỗi sợ số một của cụm filler. |
| B | 5 | 85 | 24% | 5 | 20% · mở khi Tầng A xong ~60%. C05 Filler vs booster vs thread · C11 Tiêm tan & xử lý biến chứng · C09 · C12 Số đăng ký FDA PH của từng sản phẩm · C13. |
| C | 3 | 51 | 8% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 · C15. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Safety, risks & side effects (Filler & HA collagen booster) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 15 | 18% | 4 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/guide/filler-risks-and-side-effects/ |
| 2 | C07 | Price, packages & payment terms (Filler & HA collagen booster) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 14 | 13% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/pricing/filler/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 13% | 3 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Filler & HA collagen booster) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 9% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/areas/ |
| 6 | C11 | When results fall short — revision, correction & complaints (Filler & HA collagen booster) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 7% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/filler-revision/ |
| 7 | C05 | Comparison — methods, devices & alternatives (Filler & HA collagen booster) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/filler-vs-alternatives/ |
| 8 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 9 | C09 | Booking, consultation & the first visit (Filler & HA collagen booster) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 1 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/book-a-consultation/ |
| 10 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/services/ |
| 11 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 3% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 12 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Filler & HA collagen booster) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/filler-how-long-it-lasts/ |
| 13 | C10 | Aftercare, downtime & recovery timeline (Filler & HA collagen booster) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/filler-aftercare/ |
| 14 | C01 | Problem awareness — naming the condition (Filler & HA collagen booster) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/filler-basics/ |
| 15 | C02 | Myths, home remedies & social-media beliefs (Filler & HA collagen booster) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/filler-myths/ |

---

## 4. Xline Thread Lift — nâng cơ không phẫu thuật

`threadlift.json` · **SWA** · `sunwooaesthetic.ph` · **22 bài cần sản xuất**

**Tên dùng trên site (EN):** Xline Thread Lift — non-surgical lifting

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ thẩm mỹ) · giá trị ca cao nhất trong gói

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 65% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① SỢ — “Chỉ có bị lộ, bị gồ, bị đứt không? Mặt có bị lệch không” → cụm xử lý **C06 + C11 + C10** (51 truy vấn, 26 CORE)
- ② NGẠI — “Giá trị ca cao nhất trong bảng giá; tôi trả một lần hay trả góp được” → cụm xử lý **C07 + C09 + C04** (51 truy vấn, 28 CORE)
- ③ BỀN — “12 tháng rồi chảy lại thì tôi đã trả tiền cho cái gì” → cụm xử lý **C15 + C05 + C07** (51 truy vấn, 13 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa biết gọi tên vấn đề: chảy xệ, mất đường viền hàm hay chỉ là tăng cân. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | So sánh chỉ nâng với HIFU, filler và phẫu thuật căng da — mỗi nơi nói một kiểu. | C03 · C04 · C05 · C12 | 68 | 11 | 23% |
| S3 | ★★★ Quyết định | Sợ lộ chỉ, sợ mất tự nhiên, và sợ số tiền lớn nhất trong bảng giá mà hiệu quả có hạn. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 64% |
| S4 | ★★ | Sợ downtime ảnh hưởng công việc — nhóm expat BGC nhạy với điều này hơn là nhạy giá. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ sưng không đều, sợ cảm giác căng kéo kéo dài. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Chu kỳ dặm lại là câu hỏi quyết định — phải trả lời bằng mốc tháng, không bằng tính từ. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 65% | 17 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 (vành đai V3 chỉ mở cho dịch vụ giá trị ca cao như cụm này) · C08 · C07 · C06. |
| B | 5 | 85 | 26% | 5 | 20% · mở khi Tầng A xong ~60%. C05 Thread vs HIFU vs filler vs phẫu thuật · C11 Xử lý khi lộ chỉ/lệch · C09 · C12 Số đăng ký chỉ Xline · C13 Expat BGC. |
| C | 3 | 51 | 7% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 · C15. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C07 | Price, packages & payment terms (Xline Thread Lift) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 15 | 17% | 4 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/pricing/xline-thread-lift/ |
| 2 | C06 | Safety, risks & side effects (Xline Thread Lift) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 14 | 16% | 4 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-risks-and-side-effects/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 12% | 3 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 12% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Xline Thread Lift) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 8% | 4 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/areas/ |
| 6 | C05 | Comparison — methods, devices & alternatives (Xline Thread Lift) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 7% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-vs-alternatives/ |
| 7 | C11 | When results fall short — revision, correction & complaints (Xline Thread Lift) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 7% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-revision/ |
| 8 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 9 | C09 | Booking, consultation & the first visit (Xline Thread Lift) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 1 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/book-a-consultation/ |
| 10 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/services/ |
| 11 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 3% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 12 | C10 | Aftercare, downtime & recovery timeline (Xline Thread Lift) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-aftercare/ |
| 13 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Xline Thread Lift) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-how-long-it-lasts/ |
| 14 | C01 | Problem awareness — naming the condition (Xline Thread Lift) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-basics/ |
| 15 | C02 | Myths, home remedies & social-media beliefs (Xline Thread Lift) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/xline-thread-lift-myths/ |

---

## 5. Advanced Acne Treatment — mụn viêm & sẹo mụn

`acne.json` · **SWA** · `sunwooaesthetic.ph` · **20 bài cần sản xuất**

**Tên dùng trên site (EN):** Advanced Acne Treatment — active acne & scarring

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ thẩm mỹ) · nhóm khách trẻ nhất trong gói

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 60% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① NGẠI — Nhóm khách trẻ nhất gói; ngại bị nhìn, ngại bị chê mặt, ngại bố mẹ biết chi phí → cụm xử lý **C01 + C09 + C07** (51 truy vấn, 12 CORE)
- ② NGỜ — “Đã thử skincare, thử thuốc, thử TikTok hack rồi; vì sao lần này khác” → cụm xử lý **C02 + C05 + C08** (51 truy vấn, 15 CORE)
- ③ BỀN — “Hết đợt này rồi mụn quay lại thì sao, phải duy trì cả đời à” → cụm xử lý **C15 + C10 + C06** (51 truy vấn, 11 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★★ (nâng hạng) | Nhóm khách trẻ tra cứu rất nhiều ở giai đoạn nhận biết — đây là bộ DUY NHẤT nâng C01/C02 lên Tầng B. | C01 · C02 · C13 | 51 | 0 | 13% |
| S2 | ★★ | Sợ chọn sai: laser, peel, thuốc hay chỉ cần đổi skincare. | C03 · C04 · C05 · C12 | 68 | 11 | 20% |
| S3 | ★★★ Quyết định | Sợ điều trị xong để lại sẹo và thâm nặng hơn mụn ban đầu. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 58% |
| S4 | ★★ | Sợ purging; sợ mặt xấu hơn ngay trước một sự kiện. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ không được dặn đúng cách chăm da sau thủ thuật, tự xử lý theo mạng. | C10 | 17 | 0 | 3% |
| S6 | ★★ BỀN | Sợ tái phát và phải duy trì vô thời hạn. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 60% | 13 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 · C08 (Diplomate PDS — ở cụm mụn đây là bằng chứng phân định giữa derm clinic và beauty clinic) · C07 · C06. |
| B | 6 | 102 | 32% | 7 | 20% · mở khi Tầng A xong ~60%. ⚠ Bộ DUY NHẤT đưa C01 và C02 vào Tầng B: khách mụn tra cứu rất mạnh ở S1 và đó là nơi họ gặp thông tin sai trên TikTok. C05 · C11 · C09 · C12. |
| C | 3 | 51 | 7% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C10 Chăm da sau thủ thuật · C15 Duy trì · C13. |
| D | 1 | 17 | 1% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. Riêng bộ này C03 xuống Tầng D vì đã được bộ brand phủ. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C07 | Price, packages & payment terms (Advanced Acne Treatment) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 15 | 13% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/pricing/acne-treatment/ |
| 2 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 14 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 3 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 13 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 4 | C06 | Safety, risks & side effects (Advanced Acne Treatment) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 12 | 12% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-risks-and-side-effects/ |
| 5 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Advanced Acne Treatment) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 9% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/areas/ |
| 6 | C11 | When results fall short — revision, correction & complaints (Advanced Acne Treatment) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 7% | 1 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-revision/ |
| 7 | C01 | Problem awareness — naming the condition (Advanced Acne Treatment) | Nhận biết vấn đề — gọi đúng tên tình trạng | B | S1 | 17 | 0 | 6% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-basics/ |
| 8 | C02 | Myths, home remedies & social-media beliefs (Advanced Acne Treatment) | Quan niệm dân gian & niềm tin trên mạng xã hội | B | S1 | 17 | 0 | 5% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-myths/ |
| 9 | C05 | Comparison — methods, devices & alternatives (Advanced Acne Treatment) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-vs-alternatives/ |
| 10 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 11 | C09 | Booking, consultation & the first visit (Advanced Acne Treatment) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 0 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/book-a-consultation/ |
| 12 | C10 | Aftercare, downtime & recovery timeline (Advanced Acne Treatment) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-aftercare/ |
| 13 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | C | S1 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 14 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Advanced Acne Treatment) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/acne-treatment-how-long-it-lasts/ |
| 15 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | D | S2 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/services/ |

---

## 6. PicoSure Pro — nám, sắc tố & đều màu da

`picosure.json` · **SWA** · `sunwooaesthetic.ph` · **20 bài cần sản xuất**

**Tên dùng trên site (EN):** PicoSure Pro — melasma, pigmentation & tone

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ thẩm mỹ) · thiết bị nêu đích danh trên site

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 63% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① NGỜ — “PicoSure Pro là máy thật hay tên thương mại gắn lên máy khác; có số đăng ký FDA PH không” → cụm xử lý **C12 + C14 + C08** (51 truy vấn, 29 CORE)
- ② SỢ — “Da Đông Nam Á bắn laser dễ bị tăng sắc tố sau viêm, đen hơn trước” → cụm xử lý **C06 + C10 + C05** (51 truy vấn, 24 CORE)
- ③ BỀN — “Nám là bệnh mạn tính; bao nhiêu buổi, rồi bao lâu quay lại” → cụm xử lý **C15 + C07 + C11** (51 truy vấn, 12 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa phân biệt được nám, tàn nhang, thâm sau mụn và đồi mồi. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | So sánh pico với laser toning, peel, thuốc bôi và uống. | C03 · C04 · C05 · C12 | 68 | 11 | 25% |
| S3 | ★★★ Quyết định | SỢ TĂNG SẮC TỐ SAU VIÊM trên nền da Fitzpatrick IV–V là nỗi sợ đặc thù của thị trường Philippines. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 61% |
| S4 | ★★ | Sợ đau, sợ đỏ mặt vài ngày, cần mốc downtime theo giờ. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ không được hướng dẫn chống nắng đúng cách nên công cốc. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Nám tái phát là bản chất bệnh — phải nói thật, đây chính là nội dung AI hay trích. | C15 | 17 | 0 | 3% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 63% | 14 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 · C08 · C07 (giá theo buổi và theo liệu trình) · C06 (PIH trên da Fitzpatrick IV–V). |
| B | 5 | 85 | 27% | 5 | 20% · mở khi Tầng A xong ~60%. ⚠ C12 ở bộ này quan trọng bất thường vì tên thiết bị PicoSure Pro là một claim phải chứng minh bằng số đăng ký FDA PH (R7). C05 · C11 · C09 · C13. |
| C | 3 | 51 | 8% | 1 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 Chống nắng sau thủ thuật · C15 Chu kỳ tái phát. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Safety, risks & side effects (PicoSure Pro — melasma & pigmentation) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 15 | 15% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-risks-and-side-effects/ |
| 2 | C07 | Price, packages & payment terms (PicoSure Pro — melasma & pigmentation) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 14 | 13% | 4 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/pricing/picosure-pro/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (PicoSure Pro — melasma & pigmentation) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 9% | 3 | S1 (0–30n) | MỚI: sunwooaesthetic.ph/areas/ |
| 6 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice ⭐⭐ 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 8% | 2 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 7 | C11 | When results fall short — revision, correction & complaints (PicoSure Pro — melasma & pigmentation) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 7% | 1 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-revision/ |
| 8 | C05 | Comparison — methods, devices & alternatives (PicoSure Pro — melasma & pigmentation) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 2 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-vs-alternatives/ |
| 9 | C09 | Booking, consultation & the first visit (PicoSure Pro — melasma & pigmentation) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 0 | S2 (31–60n) | MỚI: sunwooaesthetic.ph/book-a-consultation/ |
| 10 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/services/ |
| 11 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 3% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 12 | C15 | How long it lasts — maintenance, top-ups & cross-sell (PicoSure Pro — melasma & pigmentation) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 3% | 1 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-how-long-it-lasts/ |
| 13 | C10 | Aftercare, downtime & recovery timeline (PicoSure Pro — melasma & pigmentation) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-aftercare/ |
| 14 | C01 | Problem awareness — naming the condition (PicoSure Pro — melasma & pigmentation) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-basics/ |
| 15 | C02 | Myths, home remedies & social-media beliefs (PicoSure Pro — melasma & pigmentation) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwooaesthetic.ph/guide/picosure-pro-myths/ |

---

## 7. Smart Bio Implant — cấy ghép implant nha khoa

`implant.json` · **SWD** · `sunwoodental.ph` · **22 bài cần sản xuất**

**Tên dùng trên site (EN):** Smart Bio Implant — dental implants

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ nha khoa) · giá trị ca cao nhất mảng nha

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 65% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① NGẠI — Tổng chi phí lớn nhất trong cả ba mảng; sợ bị đội giá giữa lộ trình 4–8 tháng → cụm xử lý **C07 + C09 + C11** (51 truy vấn, 30 CORE)
- ② SỢ — “Trụ có đào thải không, ghép xương có đau không, thất bại thì mất cả tiền lẫn xương” → cụm xử lý **C06 + C11 + C10** (51 truy vấn, 28 CORE)
- ③ NGỜ — “Trụ hãng nào, bảo hành ai chịu, 10 năm nữa phòng khám còn không” → cụm xử lý **C12 + C14 + C08** (51 truy vấn, 26 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa biết mất răng lâu ngày dẫn tới tiêu xương, cầu răng hay implant. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | So sánh implant với cầu răng, hàm tháo lắp; so trụ hãng Hàn với hãng châu Âu. | C03 · C04 · C05 · C12 | 68 | 11 | 21% |
| S3 | ★★★ Quyết định | Sợ tổng chi phí thật (trụ + abutment + mão + ghép xương) khác xa giá quảng cáo một trụ. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 67% |
| S4 | ★★ | Sợ lộ trình 4–8 tháng, sợ số lần phải đến phòng khám. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ viêm quanh implant mà không nhận ra; cần lịch tái khám theo mốc. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Sợ tuổi thọ trụ và chi phí duy trì về sau. | C15 | 17 | 0 | 1% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 65% | 17 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 · C08 · C07 (bóc tách đủ cấu phần — đây là bài GEO mạnh nhất mảng nha) · C06. |
| B | 5 | 85 | 27% | 5 | 20% · mở khi Tầng A xong ~60%. C05 · C11 Thất bại & bảo hành · C09 Lộ trình & số buổi · C12 · C13. |
| C | 3 | 51 | 6% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 Vệ sinh quanh implant · C15 Tuổi thọ & duy trì. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C07 | Price, packages & payment terms (Smart Bio Implant) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 15 | 17% | 5 | S1 (0–30n) | MỚI: sunwoodental.ph/pricing/smart-bio-implant/ |
| 2 | C06 | Safety, risks & side effects (Smart Bio Implant) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 14 | 16% | 4 | S1 (0–30n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-risks-and-side-effects/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 12% | 3 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 12% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C11 | When results fall short — revision, correction & complaints (Smart Bio Implant) ⭐⭐ | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 10% | 2 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-revision/ |
| 6 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Smart Bio Implant) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 8% | 3 | S1 (0–30n) | MỚI: sunwoodental.ph/areas/ |
| 7 | C05 | Comparison — methods, devices & alternatives (Smart Bio Implant) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 2 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-vs-alternatives/ |
| 8 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 9 | C09 | Booking, consultation & the first visit (Smart Bio Implant) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 1 | S2 (31–60n) | MỚI: sunwoodental.ph/book-a-consultation/ |
| 10 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/services/ |
| 11 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 3% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 12 | C10 | Aftercare, downtime & recovery timeline (Smart Bio Implant) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-aftercare/ |
| 13 | C01 | Problem awareness — naming the condition (Smart Bio Implant) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-basics/ |
| 14 | C02 | Myths, home remedies & social-media beliefs (Smart Bio Implant) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-myths/ |
| 15 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Smart Bio Implant) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 1% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/smart-bio-implant-how-long-it-lasts/ |

---

## 8. Răng sứ & veneer — thiết kế nụ cười

`veneers.json` · **SWD** · `sunwoodental.ph` · **20 bài cần sản xuất**

**Tên dùng trên site (EN):** Porcelain crowns & veneers — smile design

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ nha khoa)

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 61% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① SỢ — “Mài răng là không quay lại được; mài nhiều quá thì sao” → cụm xử lý **C06 + C05 + C11** (51 truy vấn, 33 CORE)
- ② NGỜ — “Sứ loại nào, có phải sứ như quảng cáo không, ai bảo hành” → cụm xử lý **C12 + C07 + C14** (51 truy vấn, 24 CORE)
- ③ NGẠI — “Veneer trên mạng trông giả; tôi sợ cười ra ai cũng biết” → cụm xử lý **C02 + C01 + C15** (51 truy vấn, 0 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa phân biệt veneer, mão sứ, tẩy trắng và niềng. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | So sánh veneer không mài / mài tối thiểu / mão toàn sứ — khác nhau ở mức mài. | C03 · C04 · C05 · C12 | 68 | 11 | 25% |
| S3 | ★★★ Quyết định | MÀI RĂNG LÀ KHÔNG ĐẢO NGƯỢC — đây là nỗi sợ quyết định và là nội dung dám nói điều bất lợi mạnh nhất. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 62% |
| S4 | ★★ | Sợ số buổi, sợ giai đoạn đeo răng tạm. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ ê buốt, sợ viền lợi đen sau vài năm. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Tuổi thọ sứ và chi phí làm lại sau 10–15 năm. | C15 | 17 | 0 | 2% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 61% | 15 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 · C08 · C07 · C06 (mài răng không đảo ngược). |
| B | 5 | 85 | 30% | 5 | 20% · mở khi Tầng A xong ~60%. C05 Phân biệt theo mức mài men · C11 Làm lại & bảo hành · C09 · C12 · C13. |
| C | 3 | 51 | 7% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 · C15. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Safety, risks & side effects (Porcelain crowns & veneers) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 15 | 13% | 4 | S1 (0–30n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-risks-and-side-effects/ |
| 2 | C07 | Price, packages & payment terms (Porcelain crowns & veneers) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 14 | 13% | 4 | S1 (0–30n) | MỚI: sunwoodental.ph/pricing/porcelain-veneers/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 13% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C11 | When results fall short — revision, correction & complaints (Porcelain crowns & veneers) ⭐⭐ | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 10% | 2 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-revision/ |
| 6 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Porcelain crowns & veneers) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 9% | 3 | S1 (0–30n) | MỚI: sunwoodental.ph/areas/ |
| 7 | C05 | Comparison — methods, devices & alternatives (Porcelain crowns & veneers) ⭐⭐ | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 8% | 3 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-vs-alternatives/ |
| 8 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 9 | C09 | Booking, consultation & the first visit (Porcelain crowns & veneers) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 0 | S2 (31–60n) | MỚI: sunwoodental.ph/book-a-consultation/ |
| 10 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/services/ |
| 11 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 3% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 12 | C10 | Aftercare, downtime & recovery timeline (Porcelain crowns & veneers) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-aftercare/ |
| 13 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Porcelain crowns & veneers) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | C | S6 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-how-long-it-lasts/ |
| 14 | C01 | Problem awareness — naming the condition (Porcelain crowns & veneers) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-basics/ |
| 15 | C02 | Myths, home remedies & social-media beliefs (Porcelain crowns & veneers) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/porcelain-veneers-myths/ |

---

## 9. Nhổ răng khôn — răng số 8 mọc lệch, mọc ngầm

`wisdom.json` · **SWD** · `sunwoodental.ph` · **16 bài cần sản xuất**

**Tên dùng trên site (EN):** Wisdom tooth extraction — impacted third molars

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ nha khoa) · cụm có ý định cấp bách nhất

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 62% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① SỢ — “Đau cỡ nào, có phải rạch lợi, có tê hàm vĩnh viễn không” → cụm xử lý **C06 + C10 + C09** (51 truy vấn, 26 CORE)
- ② NGẠI — Đang đau cấp, cần biết GIÁ và CÓ NHẬN HÔM NAY KHÔNG, không cần đọc dài → cụm xử lý **C07 + C04 + C09** (51 truy vấn, 27 CORE)
- ③ SỢ — “Dry socket là gì, làm sao biết mình bị, nửa đêm thì gọi ai” → cụm xử lý **C10 + C11 + C06** (51 truy vấn, 13 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★★ (nâng hạng) | Khách đang đau, gõ tìm theo triệu chứng chứ không theo tên thủ thuật. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | Sợ không biết có phải nhổ hay chỉ cần uống kháng sinh. | C03 · C04 · C05 · C12 | 68 | 11 | 22% |
| S3 | ★★★ Quyết định | Sợ đau, sợ tổn thương dây thần kinh hàm dưới, sợ giá phát sinh khi răng mọc ngầm. | C06 · C07 · C08 · C11 · C14 | 85 | 54 | 60% |
| S4 | ★★ | Cấp bách: hôm nay có nhận không, mất bao lâu, ai đưa về. | C09 | 17 | 0 | 4% |
| S5 | ★★★ (nâng hạng) | ⚠ Bộ DUY NHẤT đưa C10 lên Tầng B: dry socket và chảy máu sau nhổ là truy vấn cấp cứu, AI được hỏi rất nhiều và trả lời rất hay nếu có nội dung theo mốc giờ. | C10 | 17 | 0 | 8% |
| S6 | ★ Nền | Gần như không có nhu cầu duy trì — C15 xuống Tầng D. | C15 | 17 | 0 | 1% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 62% | 11 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 · C08 · C07 (giá theo mức độ mọc lệch/ngầm) · C06 (đau & thần kinh). |
| B | 5 | 85 | 29% | 5 | 20% · mở khi Tầng A xong ~60%. ⚠ C10 được nâng lên Tầng B — dry socket, chảy máu, sưng theo mốc giờ là nhóm truy vấn cấp cứu có giá trị GEO cao nhất bộ này. C05 · C11 · C09 · C12. |
| C | 3 | 51 | 7% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C02 · C13. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. Bộ này C15 xuống Tầng D vì nhổ răng khôn không có chu kỳ duy trì. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C06 | Safety, risks & side effects (Wisdom tooth extraction) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 15 | 17% | 3 | S1 (0–30n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-risks-and-side-effects/ |
| 2 | C07 | Price, packages & payment terms (Wisdom tooth extraction) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 14 | 12% | 3 | S1 (0–30n) | MỚI: sunwoodental.ph/pricing/wisdom-tooth-extraction/ |
| 3 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 13 | 12% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 4 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 12 | 12% | 1 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 5 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (Wisdom tooth extraction) ⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 11 | 9% | 2 | S1 (0–30n) | MỚI: sunwoodental.ph/areas/ |
| 6 | C10 | Aftercare, downtime & recovery timeline (Wisdom tooth extraction) ⭐⭐ | Chăm sóc sau, downtime & mốc hồi phục | B | S5 | 17 | 0 | 8% | 2 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-aftercare/ |
| 7 | C11 | When results fall short — revision, correction & complaints (Wisdom tooth extraction) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | B | S3 | 17 | 0 | 7% | 1 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-revision/ |
| 8 | C05 | Comparison — methods, devices & alternatives (Wisdom tooth extraction) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 1 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-vs-alternatives/ |
| 9 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 10 | C09 | Booking, consultation & the first visit (Wisdom tooth extraction) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 1 | S2 (31–60n) | MỚI: sunwoodental.ph/book-a-consultation/ |
| 11 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/services/ |
| 12 | C02 | Myths, home remedies & social-media beliefs (Wisdom tooth extraction) | Quan niệm dân gian & niềm tin trên mạng xã hội | C | S1 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-myths/ |
| 13 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | C | S1 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 14 | C01 | Problem awareness — naming the condition (Wisdom tooth extraction) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-basics/ |
| 15 | C15 | How long it lasts — maintenance, top-ups & cross-sell (Wisdom tooth extraction) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | D | S6 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/wisdom-tooth-extraction-how-long-it-lasts/ |

---

## 10. Nha khoa tổng quát — khám, cạo vôi & trám răng

`generaldentistry.json` · **SWD** · `sunwoodental.ph` · **18 bài cần sản xuất**

**Tên dùng trên site (EN):** General dentistry — check-up, cleaning & fillings

**Nguồn:** Mind map Sunwoo 2026-11-10 (nhánh Dịch vụ nha khoa) · cửa vào rộng nhất mảng nha

**Quy mô bộ:** 255 truy vấn · 15 cụm · 65 truy vấn CORE 80/20 (25% bộ) chiếm 68% điểm ưu tiên

**Nỗi sợ quyết định** (mọi bài phải trả lời được ít nhất một):

- ① NGẠI — “Chỉ đi khám răng định kỳ thôi mà có bị tư vấn bán thêm không” → cụm xử lý **C07 + C09 + C05** (51 truy vấn, 27 CORE)
- ② NGẠI — “Chỗ nào gần, mở cửa cuối tuần, đi làm về vẫn kịp” → cụm xử lý **C04 + C09 + C13** (51 truy vấn, 13 CORE)
- ③ BỀN — “6 tháng một lần là thật hay chỉ là cách bán gói” → cụm xử lý **C15 + C01 + C06** (51 truy vấn, 11 CORE)

**Hành trình 6 giai đoạn:**

| GĐ | Ưu tiên | Nỗi sợ chi phối | Cụm | TV | CORE | % điểm |
|---|---|---|---|---|---|---|
| S1 | ★ Nền | Chưa biết đau ở đâu là sâu răng, là viêm lợi hay là răng khôn. | C01 · C02 · C13 | 51 | 0 | 5% |
| S2 | ★★ | Sợ bị vẽ thêm việc: cạo vôi thành trám, trám thành bọc sứ. | C03 · C04 · C05 · C12 | 68 | 14 | 28% |
| S3 | ★★★ Quyết định | Sợ giá niêm yết không phải giá cuối; cần bảng giá từng hạng mục công khai. | C06 · C07 · C08 · C11 · C14 | 85 | 51 | 57% |
| S4 | ★★ | Giờ mở cửa và cuối tuần là yếu tố quyết định với dân văn phòng BGC. | C09 | 17 | 0 | 4% |
| S5 | ★★ | Sợ ê buốt sau cạo vôi, không biết là bình thường hay bất thường. | C10 | 17 | 0 | 2% |
| S6 | ★★ BỀN | Nhịp khám định kỳ là cửa LTV lớn nhất của cả hệ thống — đây là bộ DUY NHẤT nâng C15 lên Tầng B. | C15 | 17 | 0 | 4% |

**Phân bổ 80/20:**

| Tầng | Cụm | TV | % điểm | Bài | Phân bổ & danh sách cụm |
|---|---|---|---|---|---|
| A | 5 | 85 | 68% | 12 | 70% ngân sách nội dung · làm trong 90 ngày. C14 · C04 (cụm “dentist near me / dental clinic BGC” có khối lượng lớn nhất mảng nha) · C08 · C07 · C06. |
| B | 5 | 85 | 21% | 6 | 20% · mở khi Tầng A xong ~60%. ⚠ C15 được nâng lên Tầng B — nhịp tái khám 6 tháng là cửa LTV và là cầu nối tự nhiên sang hai mảng còn lại. C05 · C09 · C12 · C13. |
| C | 3 | 51 | 9% | 0 | 10% · chạy nền, tái sử dụng nội dung CSKH/Messenger. C03 · C10 · C11. |
| D | 2 | 34 | 2% | 0 | 0% ngân sách mới · chỉ viết pillar nền một lần, dùng lại khối tiêu chí cho C08 và C12. |

**Bản đồ nội dung — 15 cụm:**

| Hạng | Mã | Cụm chủ đề (EN — dùng trên site) | Nghĩa (VI) | Tầng | GĐ | TV | CORE | % điểm | Bài | Sóng | Trang đích |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | C07 | Price, packages & payment terms (General dentistry) ⭐⭐⭐ | Giá, gói liệu trình & điều khoản thanh toán | A | S3 | 17 | 15 | 17% | 3 | S1 (0–30n) | MỚI: sunwoodental.ph/pricing/general-dentistry/ |
| 2 | C04 | LOCAL — Taguig · BGC · McKinley Hill & “near me” (General dentistry) ⭐⭐⭐ | LOCAL — Taguig · BGC · McKinley Hill & truy vấn “near me” | A | S2 | 17 | 14 | 15% | 4 | S1 (0–30n) | MỚI: sunwoodental.ph/areas/ |
| 3 | C06 | Safety, risks & side effects (General dentistry) ⭐⭐⭐ | An toàn, rủi ro & tác dụng phụ | A | S3 | 17 | 13 | 12% | 2 | S1 (0–30n) | MỚI: sunwoodental.ph/guide/general-dentistry-risks-and-side-effects/ |
| 4 | C08 | Choosing a clinic & a doctor — how to verify ⭐⭐⭐ 🏠 | Chọn phòng khám & bác sĩ — cách khách tự kiểm chứng | A | S3 | 17 | 12 | 12% | 2 | S1 (0–30n) | MỚI: sunwoomedical.ph/doctors/ |
| 5 | C14 | BRAND ENTITY — Sunwoo across three domains & doctor profiles ⭐⭐⭐ 🏠 | THỰC THỂ THƯƠNG HIỆU — Sunwoo trên ba tên miền & hồ sơ bác sĩ | A | S3 | 17 | 11 | 12% | 1 | S1 (0–30n) | MỚI: sunwoomedical.ph/about/ |
| 6 | C05 | Comparison — methods, devices & alternatives (General dentistry) | So sánh phương pháp, thiết bị & lựa chọn thay thế | B | S2 | 17 | 0 | 5% | 1 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/general-dentistry-vs-alternatives/ |
| 7 | C12 | Licences & credentials — PRC · FDA PH · DOH · scope of practice 🏠 | Giấy phép & chứng chỉ — PRC · FDA PH · DOH · phạm vi hành nghề | B | S2 | 17 | 0 | 5% | 1 | S2 (31–60n) | MỚI: sunwoomedical.ph/credentials/ |
| 8 | C09 | Booking, consultation & the first visit (General dentistry) | Đặt lịch, tư vấn & buổi khám đầu tiên | B | S4 | 17 | 0 | 4% | 2 | S2 (31–60n) | MỚI: sunwoodental.ph/book-a-consultation/ |
| 9 | C11 | When results fall short — revision, correction & complaints (General dentistry) | Khi kết quả không như mong đợi — sửa, làm lại & khiếu nại | C | S3 | 17 | 0 | 4% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/general-dentistry-revision/ |
| 10 | C15 | How long it lasts — maintenance, top-ups & cross-sell (General dentistry) | Hiệu quả kéo dài bao lâu — duy trì, dặm lại & cross-sell | B | S6 | 17 | 0 | 4% | 2 | S2 (31–60n) | MỚI: sunwoodental.ph/guide/general-dentistry-how-long-it-lasts/ |
| 11 | C03 | Service ecosystem — what the clinic actually offers | Hệ sinh thái dịch vụ — phòng khám thực sự làm gì | C | S2 | 17 | 0 | 3% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/services/ |
| 12 | C13 | Special audiences — Korean community · BGC expats · OFW 🏠 | Nhóm khách đặc thù — cộng đồng Hàn · expat BGC · OFW | B | S1 | 17 | 0 | 3% | 0 | S2 (31–60n) | MỚI: sunwoomedical.ph/korean-patients/ |
| 13 | C10 | Aftercare, downtime & recovery timeline (General dentistry) | Chăm sóc sau, downtime & mốc hồi phục | C | S5 | 17 | 0 | 2% | 0 | S3 (61–90n) | MỚI: sunwoodental.ph/guide/general-dentistry-aftercare/ |
| 14 | C01 | Problem awareness — naming the condition (General dentistry) | Nhận biết vấn đề — gọi đúng tên tình trạng | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/general-dentistry-basics/ |
| 15 | C02 | Myths, home remedies & social-media beliefs (General dentistry) | Quan niệm dân gian & niềm tin trên mạng xã hội | D | S1 | 17 | 0 | 1% | 0 | Nền (>90n) | MỚI: sunwoodental.ph/guide/general-dentistry-myths/ |

---

## Tổng hợp cụm 🏠 — khối lượng dồn về tên miền trục

Bốn cụm `C08 · C12 · C13 · C14` của **mọi bộ** đều xuất bản trên `sunwoomedical.ph`. Đây là nơi khối lượng dễ bị đếm trùng nhất khi lập kế hoạch.

| Bộ | C08 | C12 | C13 | C14 | Cộng về hub |
|---|---|---|---|---|---|
| brand | 4 | 3 | 1 | 6 | **14** |
| mesohair | 3 | 0 | 0 | 2 | **5** |
| filler | 3 | 0 | 0 | 2 | **5** |
| threadlift | 3 | 0 | 0 | 2 | **5** |
| acne | 2 | 0 | 0 | 2 | **4** |
| picosure | 2 | 2 | 0 | 2 | **6** |
| implant | 3 | 0 | 0 | 2 | **5** |
| veneers | 2 | 0 | 0 | 2 | **4** |
| wisdom | 2 | 0 | 0 | 1 | **3** |
| generaldentistry | 2 | 1 | 0 | 1 | **4** |
| **TỔNG** | **26** | **6** | **1** | **22** | **55** |

> ⚠ **55 bài** trong tổng 204 bài nằm trên tên miền trục. Khi giao việc, gộp các cụm 🏠 của nhiều bộ thành **một trang dùng chung** nếu nội dung trùng — ⛔ không dựng hai trang `/doctors/` cho hai line.

