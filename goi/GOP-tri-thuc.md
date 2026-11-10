# TRI THỨC — Sunwoo GEO Planner
> File này gộp **8 module tri thức** từ `knowledge/`. Sinh tự động ngày 2026-11-10 bằng `python tools/gop-tham-khao.py`.
> ⛔ **Không sửa file này** — sửa ở bản rời trong thư mục nguồn rồi chạy lại lệnh trên.

**Cách đọc:** mỗi phần bắt đầu bằng dòng `===== tên file =====` và là **một đơn vị tri thức riêng**. Tham chiếu dạng `[[tên-file]]` trong văn bản trỏ tới **phần cùng tên ngay trong file này**, không phải file bên ngoài.

## MỤC LỤC

| # | File | Cỡ |
|---|---|---|
| 1 | `geo-bo-truy-van-index.md` | 72.9 KB |
| 2 | `geo-kpi-framework.md` | 11.8 KB |
| 3 | `geo-luat-ba-ten-mien.md` | 9.5 KB |
| 4 | `geo-output-excel-schema.md` | 11.7 KB |
| 5 | `geo-phuong-phap-luan.md` | 20.2 KB |
| 6 | `geo-prompt-do-luong.md` | 6.3 KB |
| 7 | `geo-rao-phap-ly-ph.md` | 11.9 KB |
| 8 | `sunwoo-brand-geo.md` | 17.7 KB |


===== geo-bo-truy-van-index.md =====

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


===== geo-kpi-framework.md =====

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


===== geo-luat-ba-ten-mien.md =====

# LUẬT BA TÊN MIỀN — VÀ KHUNG MỞ LINE MỚI

Version 1.0 · Cập nhật 2026-11-10 · **Đây là file làm nên sự khác biệt của bộ Sunwoo so với bộ Kangnam và bộ Paris.** Đọc trước khi giao bất kỳ bài viết nào.

---

# 1. VẤN ĐỀ — BA TÊN MIỀN LÀ BA THỰC THỂ

Sunwoo đang chạy **ba tên miền tách rời** cho **một phòng khám duy nhất** ở Ground floor, 20 Upper McKinley Hill, Taguig:

| Tên miền | Vai trò | Nội dung hiện có |
|---|---|---|
| `sunwoomedical.ph` | **Tên miền TRỤC (hub)** — thương hiệu tổng | ⚠ Cần Sunwoo xác nhận hiện trạng |
| `sunwooaesthetic.ph` | Thẩm mỹ nội khoa & da liễu | One-page WordPress |
| `sunwoodental.ph` | Nha khoa | ⚠ Cần Sunwoo xác nhận hiện trạng |

**Vì sao đây là vấn đề GEO chứ không phải vấn đề SEO:**

SEO truyền thống chịu được nhiều tên miền — mỗi tên miền tự xếp hạng theo từ khoá của nó. **GEO thì không.** Công cụ sinh ngôn ngữ trả lời bằng cách **giải thực thể** (entity resolution): nó phải quyết định *"Sunwoo"* là **một** tổ chức hay **ba** tổ chức khác nhau, rồi mới gom bằng chứng. Ba tên miền không nối với nhau cho ra ba hệ quả, cái nào cũng tốn tiền:

| Hệ quả | Biểu hiện thật |
|---|---|
| ① **Uy tín không cộng dồn** | 204 bài chia ba rổ. Không rổ nào đủ nặng để AI coi là nguồn đáng trích cho câu hỏi *"best clinic in Taguig"* |
| ② **AI trả lời "không chắc"** | Hỏi *"Is Sunwoo Aesthetic the same as Sunwoo Dental?"* mà AI không biết → mọi bằng chứng ở tên miền kia thành vô dụng |
| ③ **Hồ sơ bác sĩ bị tách đôi** | Dr. Gatdula xuất hiện trên hai tên miền với hai URL khác nhau → AI có thể coi là **hai người**. Đây là kiểu mất mát im lặng, không ai phát hiện ra bằng công cụ SEO |

> ⚠️ Hệ quả ③ là nghiêm trọng nhất, vì hồ sơ bác sĩ là **tài sản GEO mạnh nhất** của Sunwoo: *Diplomate, Philippine Dermatological Society* là tín hiệu mà khách Philippines thật sự biết và tra. Tách đôi nó là vứt đi lợi thế lớn nhất.

---

# 2. BẢY LUẬT BẮT BUỘC

| # | Luật | Làm gì cụ thể | Vi phạm thì sao |
|---|---|---|---|
| **L1** | **Một thực thể gốc** | `sunwoomedical.ph/about/` mang schema `Organization` gốc, liệt kê hai site kia bằng `subOrganization`. Hai site kia mang `Organization` với `parentOrganization` trỏ ngược về hub, cộng `sameAs` đủ ba tên miền | AI coi là ba tổ chức |
| **L2** | **NAP giống hệt nhau** | Một địa chỉ, một số điện thoại, một cách viết — **copy từng ký tự**, kể cả *"Ground floor"* viết hoa chữ G | Mỗi biến thể NAP là một thực thể địa điểm mới |
| **L3** | **Một Google Business Profile** | Một GBP duy nhất, trừ khi ba mảng là ba pháp nhân có giấy phép riêng. `⚠ Cần Sunwoo xác nhận` | Ba GBP cùng địa chỉ → Google có thể đình chỉ cả ba |
| **L4** | **Hồ sơ bác sĩ sống MỘT nơi** | Mọi hồ sơ bác sĩ nằm ở `sunwoomedical.ph/doctors/<slug>/`. Hai site kia **liên kết tới**, ⛔ không nhân bản nội dung | Thực thể người bị tách đôi |
| **L5** | **Giá sống ở tên miền dịch vụ** | `/pricing/` của mảng nào nằm ở tên miền mảng đó. Hub chỉ có trang *"how our pricing works"* + phí tư vấn, ⛔ không chép bảng giá | Hai bảng giá lệch nhau = tín hiệu không đáng tin |
| **L6** | **⛔ Tuyệt đối không trùng nội dung** | Một bài sống ở **đúng một** URL. Cần ở nơi khác → liên kết, hoặc viết lại từ góc khác với dữ liệu khác | Trùng nội dung chia nhỏ trích dẫn và kích hoạt lọc trùng |
| **L7** | **Mọi trang dịch vụ liên kết ngược về hub** | Mỗi trang dịch vụ có một khối *"Part of Sunwoo Medical Center"* trỏ về `/about/` và `/doctors/` | Trang mồ côi — AI không nối được về thực thể gốc |

---

# 3. BẢNG ĐỊNH TUYẾN — CỤM NÀO SỐNG Ở TÊN MIỀN NÀO

Đây là bảng Agent phải tra **mỗi lần** quy một cụm ra đầu việc. Cột *"Vì sao"* là lý do GEO, không phải quy ước tuỳ tiện.

| Cụm | Tên miền | Vì sao |
|---|---|---|
| **C08** Choosing a clinic & a doctor 🏠 | **Hub** | Bằng chứng về **con người và cơ sở**, không thuộc riêng mảng nào |
| **C12** Licences & credentials 🏠 | **Hub** | Giấy phép cấp cho **cơ sở**, không cấp cho tên miền |
| **C13** Special audiences 🏠 | **Hub** | Cộng đồng Hàn · expat BGC · OFW quan tâm **cả ba mảng** |
| **C14** Brand entity 🏠 | **Hub** | Đây **chính là** khối thực thể gốc |
| C01 · C02 Nhận biết & quan niệm | Tên miền dịch vụ | Gắn chặt với tình trạng cụ thể |
| C03 Hệ sinh thái dịch vụ | **Hub** + bản rút gọn ở mỗi site | Hub kể đủ ba mảng; mỗi site kể mảng của mình |
| C04 LOCAL — vành đai & "near me" | **Cả hai** — xem luật dưới bảng | Khách gõ *"dental clinic BGC"*, không gõ *"medical center BGC"* |
| C05 · C06 · C07 · C09 · C10 · C11 · C15 | Tên miền dịch vụ | Nội dung chuyên môn của mảng |

**Luật riêng cho C04 (cụm LOCAL) — cụm duy nhất được phép tồn tại trên nhiều tên miền:**

```
sunwoomedical.ph/areas/<area>/        ← trang vành đai TỔNG: đường đi, đỗ xe, giờ mở cửa,
                                        NAP, bản đồ, liệt kê CẢ BA mảng
sunwooaesthetic.ph/areas/<area>/      ← góc thẩm mỹ: dịch vụ nào, giá nào, ai làm
sunwoodental.ph/areas/<area>/         ← góc nha khoa: dịch vụ nào, giá nào, ai làm
```

⛔ **Ba trang này KHÔNG được dùng chung một đoạn văn nào.** Trang hub nói về **đi lại và nhận dạng cơ sở**; hai trang kia nói về **dịch vụ**. Trùng một khối "how to get here" trên cả ba là vi phạm **L6** — viết một lần trên hub rồi liên kết.

---

# 4. KIỂM TRA THỰC THỂ — 6 Ô, CHẠY MỖI THÁNG

| # | Ô kiểm | Đạt khi |
|---|---|---|
| ① | `sameAs` ba tên miền có mặt trên cả ba `Organization` | ✅ |
| ② | NAP khớp từng ký tự trên ba tên miền + GBP | ✅ |
| ③ | Mỗi bác sĩ có **đúng một** URL hồ sơ trong toàn hệ thống | ✅ |
| ④ | Prompt *"Is Sunwoo Aesthetic the same company as Sunwoo Dental?"* → AI trả lời **đúng là một hệ thống** | ✅ |
| ⑤ | Không có cặp URL nào trùng >30% nội dung giữa hai tên miền | ✅ |
| ⑥ | Mọi trang dịch vụ có khối liên kết ngược về `/about/` | ✅ |

Ô ④ là **thước đo thật** của cả file này. Ba ô đầu là việc kỹ thuật; ô ④ là kết quả.

---

# 5. KHUNG MỞ LINE MỚI — SUNWOO SẼ CÒN MỞ THÊM MẢNG

Sunwoo đã nói rõ sẽ phát triển thêm mảng dịch vụ ở thị trường Philippines. Bộ này được dựng để **thêm mảng mà không sửa bộ não**.

## 5.1 ⚠️ Câu hỏi phải trả lời TRƯỚC: tên miền thứ tư hay subfolder?

> **Khuyến nghị mặc định: subfolder của tên miền trục** — `sunwoomedical.ph/wellness/` — **không** mở tên miền thứ tư.

| | Tên miền riêng thứ tư | Subfolder của hub ★ |
|---|---|---|
| Uy tín thực thể | Bắt đầu lại từ 0 | Thừa hưởng ngay toàn bộ |
| Công kỹ thuật | Lặp lại cả 7 luật L1–L7 | Gần như bằng 0 |
| Thời gian để AI nối vào thực thể | Hàng tháng | Lập tức |
| Khi nào vẫn nên chọn | Mảng đó là **pháp nhân riêng** có giấy phép riêng, hoặc nhắm nhóm khách hoàn toàn khác | — |

⚠️ Ba tên miền hiện tại là **chi phí chìm** — đã lỡ rồi thì nối lại bằng L1–L7. Nhưng mở tên miền thứ tư là **tự nguyện trả lại cái giá đó một lần nữa**. Agent phải nêu đánh đổi này mỗi khi người dùng nói đến mảng mới.

## 5.2 Sáu bước onboard một line mới

```
① Chốt tên miền (subfolder hay tên miền riêng — §5.1)
② Thêm khối vào data/lines.json:  ma · ten_en · ten_vi · domain · vai_tro · trang_thai · bo
③ Xác minh bác sĩ đúng chuyên khoa + số PRC → điền bac_si_tham_dinh
   ⛔ Trống  →  trang_thai = "blocked",  cong_chan = lý do
④ Soạn data/query-sets/<key>.json theo đúng khung 15 cụm C01–C15
⑤ python tools/build-index.py        → sinh lại chỉ mục tri thức
⑥ python tools/build-geo-plan.py     → line mới tự vào kế hoạch
```

⛔ **Không sửa `SYSTEM-PROMPT.md`. Không sửa file nào trong `tools/`.** Nếu một mảng mới buộc phải sửa bộ não thì khung đã hỏng — báo lại thay vì vá tạm.

## 5.3 Khung 15 cụm là bất biến

Mọi line mới dùng **đúng** C01–C15 với đúng ý nghĩa ở `geo-bo-truy-van-index.md`. Được phép:

- ✅ **Đổi tầng** của một cụm, kèm lý do ghi trong `phan_bo` (bộ `acne` nâng C01/C02 lên B · bộ `wisdom` nâng C10 lên B · bộ `generaldentistry` nâng C15 lên B).
- ✅ **Đặt `bai: 0`** cho cụm không cần nội dung mới.
- ⛔ **Không thêm C16**, không bỏ cụm, không đổi nghĩa cụm. Cụm so được giữa các line là điều làm cho bảng KPI đọc được.


===== geo-output-excel-schema.md =====

# SCHEMA FILE OUTPUT — 2 TAB: KPI & CÔNG VIỆC TRIỂN KHAI

Version 1.0 · Cập nhật 2026-11-10 · **Khoá format khi xuất.** Tên file:
**`GEO-SUNWOO-<Tbắt_đầu>-<Tkết_thúc>-<Năm>.xlsx`** — ví dụ `GEO-SUNWOO-T01-T06-2027.xlsx`.

**Workbook chỉ có đúng 2 sheet, theo thứ tự:**
1. `BẢNG TỔNG QUAN KPI`
2. `CÔNG VIỆC TRIỂN KHAI`

---

# BẢNG MÀU & FONT (bắt buộc)

| Vai trò | Mã màu | Dùng ở |
|---|---|---|
| Teal đậm — header chính | `#0E4F57` | TAB 1: dòng tiêu đề + dòng header cột |
| Ink đậm — header điều hành | `#10323A` | TAB 2: dòng header + dải phân cách tháng |
| Mint nhạt — dòng tổng line | `#DCECEE` | TAB 2: dòng `▶ TỔNG …` |
| Amber — dòng tổng tháng | `#C98A2E` | TAB 2: dòng `★ TỔNG SẢN LƯỢNG THÁNG` + panel thống kê |
| Xám nhạt — ô trụ cột | `#F1F5F6` | TAB 1: ô gộp cột TRỤ CỘT KPI |
| Kem — dòng chi tiết | `#FFF9F0` | TAB 2: dòng chi tiết từng bộ |
| Hồng cảnh báo — dòng bị chặn | `#F7DDDD` | TAB 2: mọi dòng mang nhãn `[BLOCKED · R4]` |

**Font toàn file:** Arial. Header 9–12pt đậm chữ trắng. Dữ liệu 10pt. Wrap text ở mọi cột mô tả dài. Border mảnh toàn bảng.

> ⚠️ Màu hồng cảnh báo là thứ **bộ Kangnam không có**. Nó tồn tại để lãnh đạo mở file ra là thấy ngay **line nào đang bị chặn và vì sao** — không phải đọc hết 200 dòng mới biết.

---

# TAB 1 — `BẢNG TỔNG QUAN KPI`

## Bố cục dòng

| Dòng | Nội dung | Định dạng |
|---|---|---|
| 1 | *(trống)* | — |
| 2 | **Gộp A2:cuối** — `BẢNG TỔNG QUAN KPI & KẾ HOẠCH GEO/SEO SUNWOO (THÁNG X – THÁNG Y)` | Nền `#0E4F57`, Arial 12 đậm, chữ trắng, canh giữa |
| 3 | 4 banner mục tiêu: `TỔNG BÀI VIẾT MỤC TIÊU` · `HẠ TẦNG 3 TÊN MIỀN & THỰC THỂ` · `GEO / SEO AI SEARCH` · `TRAFFIC & LEAD` | Nền teal, chữ trắng đậm |
| 4 | Dòng mô tả đích của từng banner | Chữ nhỏ, nền xám nhạt |
| 5 | *(trống)* | — |
| 6 | **Dòng header cột** | Nền `#0E4F57`, Arial 9 đậm, chữ trắng, wrap |
| 7+ | Dữ liệu 5 trụ cột, gộp ô dọc theo khối | — |
| cuối +1 | `TRỌNG SỐ ĐÁNH GIÁ THÁNG` — tổng = 1,00 | |
| cuối +2 | `TỔNG TRỌNG SỐ DANH MỤC` — tổng 5 trụ cột = 1,00 | |

**Freeze panes:** `D7`.

## Cột

| Cột | Header | Nội dung | Rộng |
|---|---|---|---|
| A | `TRỤ CỘT KPI` | 5 trụ cột, **gộp ô dọc** theo khối | 24 |
| B | *(nhóm phụ)* | Phân nhóm trong trụ cột (`google.com.ph`, `Traffic AI`, `Top từ khoá`, `GEO AI Search`), gộp ô dọc | 22 |
| C | `HẠNG MỤC / CHỈ TIÊU TRỌNG TÂM` | Tên line / tên miền / hạng mục cụ thể | 44 |
| D | `Số lượng` | Tổng chỉ tiêu cả chu kỳ | 10 |
| E | *(mức)* | `Top 3` `Top 5` `Top 10` `ChatGPT` `Gemini` `AI-ov` `Perplexity` `Copilot` | 11 |
| F | `Hiện tại` | Mốc gốc. Chưa có → `⚠ Cần Sunwoo xác nhận` | 24 |
| G…G+n-1 | `THÁNG MM/YYYY` | **Một cột cho mỗi tháng** (n tháng → n cột) | 12 |
| +1 | `ĐÍCH ĐẾN CHU KỲ (TARGET)` | Mô tả đích bằng lời | 46 |
| +2 | `TRỌNG SỐ` | Trọng số dòng/nhóm nhỏ | 10 |
| +3 | `TRỌNG SỐ` | Trọng số **trụ cột** (gộp ô dọc cả khối), tổng 5 khối = 1,00 | 10 |

> **Số cột tháng co giãn theo yêu cầu.** 6 tháng → 6 cột; 12 tháng → 12 cột.

## Khối dữ liệu bắt buộc (đúng thứ tự)

```
1. Hạ tầng 3 tên miền & Thực thể
     — Schema thực thể nối ba tên miền (Organization · parentOrganization · sameAs)
     — NAP thống nhất · Google Business Profile duy nhất
     — GA4 cross-domain + tách kênh LLM · tải trang < 2s
2. Sản lượng bài viết           → mỗi LINE một dòng (SWM · SWA · SWD)
                                 + dòng "Trang vành đai V1–V3"
                                 ⚠ line bị chặn ghi rõ "[BLOCKED · R4]" ở cột HẠNG MỤC
3. SEO & GEO AI Search          ├ Top từ khoá google.com.ph → mỗi TÊN MIỀN × {Top 3, Top 5, Top 10}
                                └ GEO AI Search              → mỗi TÊN MIỀN × {ChatGPT, Gemini,
                                                                 AI-ov, Perplexity, Copilot}
4. Traffic                      ├ google.com.ph → mỗi TÊN MIỀN
                                └ Traffic AI    → mỗi TÊN MIỀN
5. Lead & Booking               — mỗi line một dòng
                                — chuỗi sau form: trả lời Messenger · đặt lịch · ĐẾN KHÁM
```

⚠️ **Trụ cột 3 và 4 cắt theo TÊN MIỀN, không cắt theo line.** Thứ hạng và traffic là thuộc tính của tên miền; sản lượng và lead là thuộc tính của line. Cắt lẫn là tự làm hỏng bảng.

---

# TAB 2 — `CÔNG VIỆC TRIỂN KHAI`

Bảng **giao việc điều hành**: mỗi dòng là một đầu việc có người phụ trách và hạn chót.

## Cột (A→K) — **11 cột**, nhiều hơn bộ Kangnam một cột

| Cột | Header | Nội dung | Rộng |
|---|---|---|---|
| A | `Mã KPI` | `KPI-01`, `KPI-06.2`, `KPI-TỔNG` — mã ổn định giữa các tháng | 11 |
| B | `Trụ cột KPI` | `1. Hạ tầng & Thực thể` · `2. Tuyến nội dung` · `3. Sản lượng — <Line>` · `4. SEO & GEO` · `5. Lead & Booking` · `0. Pháp lý` | 28 |
| C | `Hạng mục` | Tên bộ cụ thể. Dòng tổng dùng tiền tố `▶` (line) và `★` (toàn hệ thống) | 40 |
| **D** | **`Tên miền`** | ★ **Cột riêng của bộ Sunwoo.** `sunwoomedical.ph` · `sunwooaesthetic.ph` · `sunwoodental.ph` · `cả ba` | 20 |
| E | `Tháng` | `Tháng 9`, `Tháng 10`… | 10 |
| F | `CHỈ TIÊU (số bài)` | Số bài phải **phát hành**. Đầu việc không phải nội dung → để trống | 13 |
| G | `Trong đó CORE` | Số bài thuộc Tầng A | 12 |
| H | `Công việc chi tiết` | **Mô tả hành động cụ thể** — xem quy tắc bên dưới | 78 |
| I | `Người phụ trách` | `Team Content` · `Team SEO` · `Team Tech/Dev` · `Team Data` · `Lead Content/SEO` · `BS thẩm định` · `Pháp chế` · `Vận hành` | 18 |
| J | `Hạn chót` | Ngày cuối tháng, `DD/MM/YYYY`. ⚠ Dòng `[BLOCKED]` ghi `⛔ tính từ ngày có nha sĩ` | 22 |
| K | `Hoàn thành` | Boolean, mặc định `FALSE` | 12 |

> **Vì sao có cột `Tên miền`:** Sunwoo chạy ba website. Một đầu việc nội dung không nói rõ bài sống ở đâu là một đầu việc chưa giao xong — và là nguyên nhân số một của nội dung trùng giữa hai tên miền (vi phạm **L6** ở `geo-luat-ba-ten-mien.md`).

## Dải phân cách tháng

Trước mỗi khối tháng, một dòng **gộp A:K**:
```
════  THÁNG 9/2026  ·  giai đoạn SETUP  ·  hạn chót 30/09/2026  ════
```
Nền `#10323A`, chữ trắng đậm, canh giữa.

## Bốn cấp dòng trong mỗi khối tháng

| Cấp | Nhận dạng | Nền | Ý nghĩa |
|---|---|---|---|
| Chi tiết | `KPI-06.2`… | `#FFF9F0` kem | Từng bộ dịch vụ |
| **Bị chặn** | Cột H mở đầu bằng `[BLOCKED · R4]` | `#F7DDDD` hồng | Sản xuất được, **chưa phát hành được** |
| Tổng line | Cột C bắt đầu bằng `▶ TỔNG …` | `#DCECEE` mint | Cộng các dòng chi tiết của line |
| Tổng tháng | `KPI-TỔNG`, C = `★ TỔNG SẢN LƯỢNG THÁNG (toàn hệ thống)` | `#C98A2E` amber | **Con số lãnh đạo đọc** |

## Panel phụ bên phải (cột M–N)

| Vị trí | Nội dung |
|---|---|
| `M1:N1` | `TỔNG SẢN LƯỢNG THEO THÁNG` (nền amber) |
| `M2:N…` | Từng tháng → tổng số bài; dòng cuối `TỔNG CHU KỲ` |
| dưới đó | `TRẦN THẨM ĐỊNH BÁC SĨ` (nền ink) — trần/tháng · thực tế cao nhất · còn dư |
| dưới đó | `THỐNG KÊ TIẾN ĐỘ` — tổng đầu việc · đã hoàn thành · chưa hoàn thành · tiến độ |
| dòng chú giải | *"Dòng amber ★ là tổng của tháng. Dòng mint ▶ là tổng của từng line. Dòng kem là chi tiết. **Dòng hồng là việc đã sản xuất nhưng chưa được phép phát hành.**"* |

---

# QUY TẮC VIẾT CỘT `Công việc chi tiết` (H)

Đây là nơi **phương pháp luận biến thành hành động**. Mỗi ô phải trả lời được: *làm gì · cho cụm nào · trên tên miền nào · gỡ rào cản nào · chạm rào pháp lý nào.*

| ❌ Không chấp nhận | ✅ Bắt buộc |
|---|---|
| "Viết bài SEO cho Thread Lift" | "Sản xuất 4 bài cụm **C06 Safety, risks & side effects (Xline Thread Lift)** — Tầng A · S3 · rào SỢ: 1 trang trụ *thread lift risks* + 3 bài tình huống (lộ chỉ · lệch · đau kéo dài). BLUF, có số, nêu cả điều bất lợi. Nêu tên chỉ **đúng tên đã đăng ký FDA PH** (R7). BS thẩm định + PRC # trong author box (R4)." |
| "Tối ưu GEO" | "Chạy 36 prompt đã khoá ở chế độ ẩn danh trên ChatGPT · Gemini · AI Overview · Perplexity · Copilot, 3 lần lấy đa số, ghi 1/0 + đối thủ được nhắc + URL được trích. Tháng đầu lấy mốc gốc." |
| "Làm trang local" | "Dựng 2 trang vành đai **V1 BGC/Taguig** và **V2 Makati** trên `sunwoomedical.ph/areas/` — NAP chuẩn, thời gian đi thật giờ cao điểm & thấp điểm, hướng dẫn đỗ xe, liên kết sang cả ba mảng. ⛔ Không hứa kết quả điều trị trên trang vành đai." |
| "Viết bài nha khoa" | "**[BLOCKED · R4]** Sản xuất 5 bài cụm **C07 Price, packages & payment terms (Smart Bio Implant)** — bóc tách trụ + abutment + mão + ghép xương. ⛔ **Không phát hành** cho tới khi có nha sĩ PRC thẩm định. Hạn chót tính từ ngày có nha sĩ." |

Khi đầu việc gắn với một cụm → **luôn ghi mã cụm + tầng + giai đoạn**. Khi chạm rào pháp lý → ghi mã `R0`–`R11` trong ngoặc.

---

# QUY TẮC XUẤT FILE

1. **Xuất tự động, không hỏi.** Sau khi trình bảng kế hoạch trong chat và tự soát, Agent xuất thẳng `.xlsx`.
2. **Bảng phẳng khi cần dán:** nếu người dùng ở Gemini → xuất thêm bảng phẳng đúng số cột, **mỗi ô một giá trị, ⛔ không gộp ô**, lặp lại tên line ở mỗi dòng để bấm *Export to Sheets*.
3. **⛔ Không để ô trống** ở cột bắt buộc: Mã KPI · Trụ cột · Hạng mục · **Tên miền** · Tháng · Người phụ trách · Hạn chót. Thiếu dữ liệu → ghi `⚠ Cần Sunwoo xác nhận`.
4. **Kiểm tra trước khi xuất:**
   - [ ] Tổng trọng số 5 trụ cột = 1,00 · tổng trọng số tháng = 1,00
   - [ ] `★ TỔNG SẢN LƯỢNG THÁNG` = Σ các dòng `▶ TỔNG` của tháng đó
   - [ ] Panel `TỔNG SẢN LƯỢNG THEO THÁNG` khớp dòng `★` từng tháng
   - [ ] Mọi dòng có Hạn chót = ngày cuối tháng (trừ dòng `[BLOCKED]`)
   - [ ] Chênh lệch sản lượng tháng cao/thấp ≤ 25% (trừ tháng Setup)
   - [ ] **Sản lượng tháng ≤ trần thẩm định bác sĩ** — vượt thì phải có dòng cảnh báo
   - [ ] **Mọi dòng nội dung có đúng một tên miền** — không có dòng nào ghi "cả ba" trừ đầu việc hạ tầng
   - [ ] Không có số tuyệt đối bịa ở cột `Hiện tại`
   - [ ] Dòng của line SWD mang nhãn `[BLOCKED · R4]` và nền hồng
5. **Sinh file bằng script:** chạy cục bộ dùng `tools/build-geo-plan.py` — script khoá sẵn toàn bộ màu, gộp ô, freeze panes và công thức tổng.


===== geo-phuong-phap-luan.md =====

# PHƯƠNG PHÁP LUẬN GEO — SUNWOO (THỊ TRƯỜNG PHILIPPINES)

Version 1.0 · Cập nhật 2026-11-10 · Đây là **xương sống tư duy** của Agent. Mọi kế hoạch GEO phải đi đúng trục này, không đảo bước, không bỏ bước.

---

# 0. TUYÊN NGÔN — KHÔNG ĐI KỂ CHUYỆN MÌNH CHUẨN HÀN

> **Sunwoo không đi kể chuyện mình là K-beauty. Sunwoo đi theo hành trình của một người đang ở Metro Manila, gỡ từng nỗi lo, rồi mới xuất hiện như lời giải.**

| Cách cũ (brand-first) | Cách của bộ này (customer-journey-first) |
|---|---|
| *"The #1 K-beauty medical aesthetic center in the Philippines"* | *"Can laser treatment make melasma worse on brown skin?"* |
| Nội dung xoay quanh **chúng tôi có gì** | Nội dung xoay quanh **khách đang sợ gì** |
| Đo bằng thứ hạng từ khoá | Đo bằng **AI có trích dẫn Sunwoo không** |
| Né chủ đề rủi ro, biến chứng, giá | **Chiếm lĩnh** chủ đề đó — vì đó là nơi khách quyết định |
| Một trang one-page nói hết mọi thứ | **Một trang trả lời một câu hỏi**, vì AI trích theo đoạn |

**Hệ quả vận hành:** thứ tự ưu tiên nội dung KHÔNG theo giá trị ca dịch vụ, mà theo **điểm ưu tiên của cụm truy vấn**. Vì vậy cụm *"What are the risks of dermal filler and can it be dissolved?"* đứng trên cụm *"Our filler technology"*.

⚠️ **Một lưu ý riêng của Sunwoo:** câu *"#1 K-beauty"* đang nằm trên trang production và vừa là vùng cấm của ASC (rào **R6**), vừa là kiểu nội dung AI ít trích nhất. Bỏ nó đi không phải là nhún nhường — là đổi một câu không ai tin lấy một câu được trích dẫn.

---

# 1. TRỤC 6 BƯỚC (BẮT BUỘC, KHÔNG ĐẢO THỨ TỰ)

```
① Chọn lĩnh vực  →  ② Đối tượng KH  →  ③ Giai đoạn hành trình (S1–S6)
        →  ④ Cụm truy vấn (từ khoá EN)  →  ⑤ Cụm nội dung (bài viết)  →  ⑥ GEO/SEO
```

| Bước | Làm gì | Nguồn dữ liệu | Đầu ra |
|---|---|---|---|
| ① **Chọn lĩnh vực** | Chốt phạm vi: line nào, bộ nào | `data/lines.json` · `geo-bo-truy-van-index.md` | Danh sách bộ đưa vào kế hoạch |
| ② **Đối tượng KH** | Xác định nhóm khách theo **vành đai đi lại** V1–V4 + 3 nhóm đặc thù | `sunwoo-brand-geo.md` §8–§9 | Chân dung + rào cản chi phối |
| ③ **Giai đoạn** | Rải đối tượng lên 6 giai đoạn S1→S6 | §2 file này | Trọng số nỗ lực theo giai đoạn |
| ④ **Cụm truy vấn** | Lấy cụm C01–C15 + điểm ưu tiên + tầng 80/20 | `geo-bo-truy-van-index.md` | Danh sách cụm xếp hạng |
| ⑤ **Cụm nội dung** | Quy cụm → số bài, dạng bài, **tên miền nào**, sóng, người phụ trách | `geo-bo-truy-van-index.md` + `geo-luat-ba-ten-mien.md` | **Khối lượng sản xuất** (đơn vị: bài) |
| ⑥ **GEO/SEO** | Gắn KPI đo được | `geo-prompt-do-luong.md` + `geo-kpi-framework.md` | 2 TAB Excel: KPI + Công việc triển khai |

**Quy tắc vàng:** không nhảy từ ① sang ⑤. Mọi bài viết phải truy ngược được về **một cụm truy vấn** → **một giai đoạn** → **một rào cản của một đối tượng thật**. Bài nào không truy ngược được → loại khỏi kế hoạch.

⚠️ **Bước ⑤ của Sunwoo có thêm một việc mà bộ Kangnam không có:** chọn **tên miền đích**. Ba tên miền nghĩa là mỗi bài đều phải trả lời *"bài này sống ở đâu"*. Xem `geo-luat-ba-ten-mien.md` §3 — bảng định tuyến.

---

# 2. BƯỚC ③ — 6 GIAI ĐOẠN HÀNH TRÌNH (S1–S6)

Khung dùng chung cho mọi bộ. Mỗi giai đoạn có **một rào cản khác nhau** — trả lời sai rào cản thì mất khách dù dịch vụ tốt.

| GĐ | Tên | Nhiệt | Khách đang nghĩ gì | Nội dung Sunwoo phải có | Vai trò trong kế hoạch |
|---|---|---|---|---|---|
| **S1** | NHẬN BIẾT | Cold · ★ | *"Something's off but I don't know what it's called"* | Nội dung **định danh vấn đề**, không bán hàng | Cửa vào rộng — traffic, không tính chuyển đổi |
| **S2** | TÌM HIỂU | Warm · ★★ | *"How many options are there? Which one fits me?"* | Bảng so sánh **trung thực, nêu cả nhược điểm** | Xây E-E-A-T, đổi cách AI phân loại Sunwoo |
| **S3** | CÂN NHẮC & NỖI SỢ | Warm→Hot · ★★★ | *"Is it safe? How much? Who is actually doing it?"* | **Rủi ro nói thật có số · bảng giá công khai · cách tự kiểm tra PRC · case thật** | ⚠ **ĐIỂM QUYẾT ĐỊNH — chiếm ~50–60% điểm ưu tiên. Ưu tiên tuyệt đối.** |
| **S4** | THỰC HIỆN | Hot · ★★ | *"How many sessions? Can I go back to work after?"* | Quy trình từng bước **có mốc thời gian** | Giảm huỷ lịch, tăng tỷ lệ đến khám |
| **S5** | TRẢI NGHIỆM & HẬU THỦ THUẬT | Existing · ★★ | *"Is this swelling normal?"* | Cẩm nang hậu thủ thuật **theo mốc giờ/ngày** | Không tạo lead mới nhưng **neo thực thể** trong AI + giảm biến chứng |
| **S6** | GẮN BÓ & MỞ RỘNG | LTV · ★ | *"It's wearing off — do I pay again forever?"* | Chu kỳ duy trì nói thật bằng mốc tháng | Tăng LTV + trả lời rào **BỀN** |

**Phân bổ nỗ lực chuẩn** (dùng khi chưa có dữ liệu riêng): S3 ≈ 50% · S2 ≈ 20% · S1 ≈ 8% · S4 ≈ 8% · S5 ≈ 8% · S6 ≈ 6%.
Hai ngoại lệ đã khai trong dữ liệu: bộ `acne` nâng S1 (khách trẻ tra cứu mạnh ở giai đoạn nhận biết) và bộ `wisdom` nâng S5 (dry socket là truy vấn cấp cứu).

---

# 2b. BỐN RÀO CẢN NỀN — BẢN PHILIPPINES

Bộ Kangnam dùng *ba nỗi sợ ngành thẩm mỹ Việt Nam*. Thị trường Philippines và mô hình **phòng khám nội địa một cơ sở** đổi bộ rào cản này — **không phải dịch lại, mà là bộ khác**. Mọi bài phải trả lời được ít nhất một:

| Mã | Rào cản | Khách đang nghĩ gì | Cụm xử lý chính |
|---|---|---|---|
| **NGỜ** | Không biết tin ai | *"Is this clinic real? Is this doctor licensed? Is this device registered?"* Ba tên miền rời nhau làm rào này nặng hơn bình thường | C14 · C12 · C08 |
| **NGẠI** | Ngại đi lại, ngại riêng tư, ngại bị bán thêm | *"How long is the drive from Makati at 6pm?"* · *"Will someone see me walking in?"* | C04 · C09 · C07 |
| **SỢ** | Sợ hỏng, sợ không đảo ngược được | *"Can filler be dissolved?"* · *"Is tooth shaving permanent?"* · *"Will laser darken my skin?"* | C06 · C11 · C10 |
| **BỀN** ★ | **Rào đặc thù của gói nội địa** — không có trong bộ Việt Nam | *"It lasts 12 months, then what? How much more do I pay, forever?"* | C15 · C07 · C05 |

> **Vì sao BỀN là rào riêng của Sunwoo:** cả ba line đều bán **thủ thuật nhiều buổi, hiệu quả có thời hạn** — mesotherapy, filler, chỉ nâng, liệu trình nám, và cả nhịp tái khám nha khoa. Khách không sợ một lần mất tiền; khách sợ **một dòng chi phí không có điểm dừng**. Nội dung trả lời thẳng bằng **mốc tháng và chi phí dặm lại** vừa gỡ rào vừa là loại nội dung AI trích mạnh nhất, vì gần như không đối thủ nào dám viết.

⛔ **Không được viết rào BỀN theo kiểu trấn an.** *"Results are long-lasting"* là câu rỗng, bị AI bỏ qua và bị ASC soi. Viết: *"Thread lift results typically last 12–18 months depending on age and skin laxity; most patients consider a top-up at month 12."*

---

# 3. BƯỚC ④ — CỤM TRUY VẤN & CÔNG THỨC ƯU TIÊN

## 3.1 Vì sao không dùng bộ từ khoá SEO cũ

- Truy vấn vào AI dài gấp **~6 lần** truy vấn Google (≈23 từ so với 3–4 từ) — khách gõ nguyên một câu chuyện.
- AI "bung" (query fan-out) một câu hỏi thành **8–20 truy vấn con** rồi mới tổng hợp. Chỉ **32%** trích dẫn đến từ trang top 10 Google — **68%** đến từ trang ngoài top 10 nhưng khớp đúng một truy vấn con.
- **88%** thương hiệu KHÔNG được AI trích dẫn nếu chỉ tối ưu SEO truyền thống. Thương hiệu phủ được **>80% không gian chủ đề** giữ được **~85%** mức hiển thị trong AI.
- → Cuộc chơi không phải "lên top từ khoá", mà là **PHỦ KÍN KHÔNG GIAN CÂU HỎI** của một khách hàng, từ lúc soi gương đến lúc tái khám.

**Thêm một lý do chỉ Sunwoo mới có:** `sunwooaesthetic.ph` hiện là **one-page WordPress**. Một trang không thể khớp 2.550 truy vấn con. Mọi cụm đều phải ra **trang riêng** — đây không phải việc tối ưu, đây là việc dựng mới.

## 3.2 Công thức điểm ưu tiên (điểm tối đa 81)

```
ĐIỂM ƯU TIÊN = Giá trị ca × Nhiệt độ × Ưu tiên × Cơ hội GEO
               (Cao 3       (Hot 3     (P1 3     (1–3, lấy từ traffic AI
                TB  2        Warm 2     P2 2      thật của trang đích)
                Thấp 1)      Existing 2 P3 1)
                             Cold 1)
```

**Ngưỡng Cơ hội GEO** theo bằng chứng traffic AI của trang đích: ≥50 phiên → 3 · ≥5 phiên → 2 · còn lại → 1.

> 🔶 **Trạng thái hiện tại: Cơ hội GEO = 1 cho MỌI cụm.** Sunwoo chưa có một mốc traffic AI nào. Nghĩa là thứ hạng cụm trong `geo-bo-truy-van-index.md` mới chỉ phản ánh **ba** thừa số đầu. Sau tháng Setup — khi GA4 đã tách được kênh LLM và bộ đo đã chạy một vòng — **phải chấm lại Cơ hội GEO và chạy lại `tools/build-index.py`**. Agent phải nhắc việc này trong mọi kế hoạch có tháng Setup.

## 3.3 Bốn tầng 80/20

| Tầng | Tên | % ngân sách | Thời điểm | Đặc điểm |
|---|---|---|---|---|
| **A** | CORE 80/20 | **70%** | 90 ngày đầu | 5 cụm, ~33% truy vấn nhưng chiếm **~60%** điểm ưu tiên. Hầu hết nằm ở S3 |
| **B** | Đòn bẩy chuyển đổi | **20%** | Khi A xong ~60% | ~5 cụm — so sánh, quy trình, xử lý sự cố, nhóm đặc thù |
| **C** | Uy tín & giữ chân | **10%** | Chạy nền | ~3 cụm — hậu thủ thuật, duy trì, cross-sell. Tái dùng qua Messenger/Viber |
| **D** | Cửa vào rộng | **0% ngân sách mới** | Sau 90 ngày | ~2 cụm — chỉ pillar nền, tái sử dụng |

Không mở Tầng B khi Tầng A chưa xong ~60%. Nếu người dùng yêu cầu khác → nêu rõ đánh đổi rồi mới làm theo.

## 3.4 Bảy hướng mở rộng — **GIẢ THUYẾT, chưa phải bằng chứng**

> ⚠️ Bộ Kangnam có bảng "7 mẫu thắng quan sát được" dựa trên traffic AI thật. **Sunwoo không có dữ liệu đó.** Bảng dưới đây là **giả thuyết có căn cứ** từ đặc điểm thị trường PH. Mỗi dòng có cột *"kiểm bằng gì"* — sau 90 ngày phải đối chiếu và loại bỏ hướng nào không ra số.

| Mã | Hướng mở rộng | Giả thuyết | Kiểm bằng gì (sau 90 ngày) |
|---|---|---|---|
| G1 | **Thực thể ba tên miền** | Khách và AI đều chưa nối được ba tên miền về một phòng khám → mỗi lần AI "không chắc" là một lần mất trích dẫn | 3 prompt kiểm tra sức khoẻ thực thể ở cuối `geo-prompt-do-luong.md` |
| G2 | **Vành đai × Dịch vụ** | *"clinic near me"* và *"dental clinic BGC"* là nhóm truy vấn lớn nhất, vì PH đo khoảng cách bằng **phút kẹt xe** | Phiên AI vào các trang `/areas/*` · trường `Your area` trên form |
| G3 | **Bác sĩ · Diplomate PDS** | Ở PH, *Diplomate, Philippine Dermatological Society* là tín hiệu phân biệt rõ nhất giữa derm clinic và beauty clinic — và khách PH **có biết** nhãn này | Phiên AI vào `/doctors/*` · prompt P-BRAND-07 |
| G4 | **Giá & tổng chi phí liệu trình** | AI trích bài **có con số**. Ở PH, câu hỏi không phải *"giá bao nhiêu"* mà *"tổng cả liệu trình bao nhiêu"* | Phiên AI vào `/pricing/*` · prompt P-AES-01, P-DEN-01 |
| G5 | **Rào BỀN — hiệu quả kéo dài bao lâu** | Gần như không đối thủ nào viết thẳng; đây là khoảng trống rẻ nhất để chiếm | Prompt P-AES-02 · P-DEN-07 |
| G6 | **Hậu thủ thuật & sự cố theo mốc giờ** | Câu hậu thủ thuật được Perplexity/Claude trích mạnh. Dry socket, PIH sau laser, sưng sau chỉ nâng là ba cụm nóng nhất | Prompt P-DEN-05 · P-AES-06 |
| G7 | **Cầu nối ba mảng** | Một khách nha khoa và một khách thẩm mỹ là cùng một người ở cùng một toà nhà — nhưng ba site đang không nói chuyện với nhau | Lượt chuyển tiếp giữa ba tên miền trong GA4 |

---

# 4. BƯỚC ⑤ — 6 QUY TẮC VIẾT ĐỂ ĐƯỢC AI TRÍCH DẪN

Bắt buộc với mọi bài. Khi Agent mô tả đầu việc nội dung, phải nhắc được các quy tắc này trong cột công việc chi tiết.

1. **BLUF** — câu đầu tiên của mỗi mục PHẢI là câu trả lời đứng độc lập, hiểu được khi tách khỏi ngữ cảnh. *AI trích theo đoạn, không trích theo bài.*
2. **CÓ SỐ** — nội dung có số liệu được hiển thị trong câu trả lời AI cao hơn **30–40%**. *"Swelling settles in about 70% of patients by day 10"* thắng *"swelling goes down quickly"*.
3. **PHỦ 8 GÓC HỎI** cho mỗi chủ đề: định nghĩa · so sánh · hướng dẫn · trường hợp áp dụng · phản đối/rủi ro · thực thể liên quan · chi phí/chỉ số · địa phương. *Đây chính là 8 hướng AI bung truy vấn.*
4. **DÁM NÓI ĐIỀU BẤT LỢI** — *"Veneers require permanent enamel reduction; this cannot be reversed."* Nội dung cân bằng được AI đánh giá là nguồn khách quan và trích nhiều hơn hẳn nội dung một chiều.
5. **GHI NGÀY CẬP NHẬT + BÁC SĨ THẨM ĐỊNH CÓ SỐ PRC** trên mọi bài y khoa (schema `ProfilePage` / `Physician`). Ở PH đây vừa là tín hiệu E-E-A-T vừa là yêu cầu pháp lý (**R4**).
6. **KHÔNG NHỒI TỪ KHOÁ** — nhồi từ khoá cho kết quả **thấp hơn mức nền** trong AI search. Viết như đang trả lời một người thật.

**Quy tắc thứ 7 chỉ Sunwoo mới có — NGÔN NGỮ:**
> Nội dung trên site viết bằng **English chuẩn, câu ngắn**. ⛔ **Không Taglish trên trang y khoa** — Taglish chỉ dùng cho creative mạng xã hội và kịch bản Messenger. ⛔ Không dùng Taglish trong: tên dịch vụ y khoa · câu miễn trừ · thông tin giá · nội dung về chỉ định điều trị.

**Quy đổi khối lượng sản xuất:**

| Nhóm | Mô tả | Độ dài | Hệ số |
|---|---|---|---|
| A1 | Bài trụ / pillar / trang dịch vụ chính | 2.000–2.750 từ | **1,5** |
| A2 | Bài thường / tình huống / FAQ dài | 1.400–1.750 từ | **1,0** |
| A3 | Trang vành đai, FAQ ngắn, khối nhúng | <1.400 từ | **0,5** |

---

# 5. BƯỚC ⑥ — ĐO LƯỜNG GEO

Giao thức đầy đủ + 36 prompt tiếng Anh: `geo-prompt-do-luong.md`. Năm trụ cột KPI: `geo-kpi-framework.md`.

Tóm tắt bắt buộc nhớ: **ẩn danh · dán nguyên văn · ghi 1/0 · chạy 3 lần lấy đa số · nhân bản sheet mỗi tháng · đo XU HƯỚNG, không đo tuyệt đối một lần.**

---

# 6. QUY TẮC LẬP KẾ HOẠCH THEO THÁNG

## 6.1 Ánh xạ sóng → tháng

| Số tháng | Ánh xạ |
|---|---|
| 3 tháng | T1 = Sóng 1 (Tầng A) · T2 = Sóng 2 (Tầng B) · T3 = Sóng 3 (Tầng C) |
| 4 tháng | T1 Setup + Sóng 1 · T2 Sóng 1 (tiếp) + Sóng 2 · T3 Sóng 2 + Sóng 3 · T4 Sóng 3 + Nền |
| 6 tháng | Sóng 1 trải T1–T2 · Sóng 2 trải T3–T4 · Sóng 3 T5 · Nền T6 |
| 12 tháng | Quý 1 Sóng 1 · Quý 2 Sóng 2 · Quý 3 Sóng 3 · Quý 4 Nền + mở line mới |

## 6.2 Bốn giai đoạn của một chu kỳ

**Setup → Tăng tốc → Đột phá → Về đích** (trọng số tháng 20% · 25% · 30% · 25%).

Tháng **Setup** của Sunwoo luôn gồm **bảy** việc, không được bỏ việc nào:
1. Khoá 36 prompt đo GEO, chạy lấy **mốc gốc**.
2. Dựng GA4 trên **cả ba tên miền** + cấu hình cross-domain tracking, tách kênh traffic LLM.
3. **Dựng khối thực thể** trên `sunwoomedical.ph` (cụm C14) — việc này ra TRƯỚC mọi bài dịch vụ.
4. Sửa **hai lỗi cổng chặn** trên trang production: con số *"300++ doctors"* và FAQ nêu dịch vụ ngoài phạm vi. ⛔ Chưa sửa xong thì không đổ nội dung mới vào.
5. Chuẩn hoá **NAP** giống hệt nhau trên ba tên miền + chốt **một** Google Business Profile.
6. Ban hành khung loại bài + checklist từ cấm (rào R1 · R6).
7. Nộp hồ sơ **duyệt quảng cáo trước khi phát** (ASC · FDA PH — rào **R9**) cho nhóm nội dung thuộc health product.

## 6.3 Bảy nguyên tắc phân bổ sản lượng

1. **Tầng A trước** — không mở Tầng B khi Tầng A chưa xong ~60%.
2. **S3 trước S1** — luôn xuất bản cụm nỗi sợ/giá/chọn cơ sở trước cụm nhận biết.
3. **Tháng nào cũng chạy đủ các line đang mở** — không dồn hết một line vào một tháng.
4. **Sản lượng phẳng** — chênh lệch tháng cao nhất / thấp nhất ≤ 25%, trừ tháng Setup được phép thấp hơn.
5. **C14 ra trước tất cả** — khối thực thể trên tên miền trục là nền của mọi cụm còn lại. Bài dịch vụ ra trước C14 là bài mồ côi.
6. **Cụm 🏠 gộp một lần** — bốn cụm C08/C12/C13/C14 của nhiều bộ dùng chung trang trên tên miền trục. ⛔ Không dựng hai trang `/doctors/`.
7. **Mỗi đầu việc có người phụ trách + hạn chót** = ngày cuối tháng. Không để trống.

## 6.4 ⛔ CỔNG DUYỆT BÁC SĨ — trần sản lượng thật của Sunwoo

Đây là ràng buộc **không có trong bộ Kangnam** và là lý do kế hoạch Sunwoo không thể copy quy mô của một bệnh viện.

> **Mọi bài y khoa phải được một bác sĩ có giấy phép PRC đúng chuyên khoa thẩm định trước khi đăng (R4).** Sunwoo công bố **hai** bác sĩ, và **không bác sĩ nào là nha sĩ**.

**Ba hệ quả bắt buộc khi lập kế hoạch:**

| # | Luật | Cách Agent áp dụng |
|---|---|---|
| ① | **Trần thẩm định** | Mặc định quy hoạch **≤ 24 bài/bác sĩ/tháng**. Hai bác sĩ → trần **48 bài/tháng** cho line SWA + SWM. Vượt trần → Agent **cảnh báo và đề xuất giãn tiến độ**, ⛔ không im lặng nhận chỉ tiêu không khả thi. Con số 24 là giả định — ghi `⚠ Cần Sunwoo xác nhận` và hỏi năng lực thật. |
| ② | **Line SWD bị chặn** | Mọi dòng công việc của 4 bộ nha khoa mang nhãn `[BLOCKED · R4]`. Agent **vẫn lập kế hoạch đầy đủ** (để Sunwoo thấy quy mô việc) nhưng hạn chót tính **từ ngày có nha sĩ**, không tính từ hôm nay, và tháng Setup phải có một đầu việc riêng: *"Xác minh & công bố nha sĩ có giấy phép PRC"*. |
| ③ | **Không lấy content writer thay bác sĩ** | Bài không có bác sĩ thẩm định vẫn viết được nhưng **không đăng**. Khi đó đếm vào cột *"đã sản xuất"*, ⛔ không đếm vào cột *"đã phát hành"* — hai con số khác nhau trong TAB KPI. |

## 6.5 Quy tắc số liệu

- Chỉ tiêu **sản lượng**: tính được từ `geo-bo-truy-van-index.md` → được phép đưa số cụ thể.
- Chỉ tiêu **SEO/GEO/Traffic/Lead**: phải có số hiện tại làm mốc. Chưa có → cột *"Hiện tại"* ghi `⚠ Cần Sunwoo xác nhận`, đề xuất **mức tăng trưởng tương đối (%)**, ⛔ **không bịa số tuyệt đối**.
- Mọi **giá, số buổi, downtime, chỉ định** phải do phòng khám cung cấp. ⛔ Agent không tự điền — xem bảng `[CHỜ XÁC NHẬN]` ở `sunwoo-brand-geo.md` §10.


===== geo-prompt-do-luong.md =====

# BỘ PROMPT ĐO GEO — SUNWOO (TIẾNG ANH)

> Sinh tự động từ `data/geo-prompts.json` bằng `tools/build-index.py`. **Không sửa tay.**

**4 bộ · 36 prompt.** Đây là thước đo của trụ cột KPI số 3 (trọng số 0,40).

**Ngôn ngữ:** English — đây là ngôn ngữ khách Philippines thật sự gõ vào AI. ⛔ Không dịch sang tiếng Việt, không dùng Taglish trong bộ đo (Taglish chỉ dùng cho creative mạng xã hội).

**Nền tảng đo:** ChatGPT · Gemini · Google AI Overview · Perplexity · Copilot

**Giao thức:** Chế độ ẩn danh · không đăng nhập · tắt cá nhân hoá · dán NGUYÊN VĂN prompt · ghi 1 nếu Sunwoo được nhắc tên, 0 nếu không · CHẠY 3 LẦN LẤY ĐA SỐ · ghi thêm đối thủ được AI nhắc · nhân bản sheet đo mỗi tháng · KHOÁ bộ đo từ tháng Setup.

> ⚠ Kết quả AI thay đổi theo phiên. Đây là **KPI xu hướng theo tháng**, không phải con số tuyệt
> đối một lần. Tháng đầu của mọi chu kỳ là tháng **lấy mốc gốc**, không đặt chỉ tiêu tăng trưởng.

---

## P-BRAND — Thực thể thương hiệu & kiểm chứng

Line **SWM** · cụm **C14 · C12 · C08** · 8 prompt

| # | Prompt (dán nguyên văn) | ChatGPT | Gemini | AI Overview | Perplexity | Copilot |
|---|---|---|---|---|---|---|
| P-BRAND-01 | What is Sunwoo Medical Center in the Philippines? | | | | | |
| P-BRAND-02 | Is Sunwoo Medical Center in Taguig legitimate? | | | | | |
| P-BRAND-03 | Who are the doctors at Sunwoo Medical Center? | | | | | |
| P-BRAND-04 | Is Sunwoo Aesthetic and Sunwoo Dental the same clinic as Sunwoo Medical Center? | | | | | |
| P-BRAND-05 | Does Sunwoo Medical Center have PRC-licensed doctors? | | | | | |
| P-BRAND-06 | Which Korean medical centers operate in the Philippines? | | | | | |
| P-BRAND-07 | Which clinics in Metro Manila have a board-certified dermatologist who is a PDS diplomate? | | | | | |
| P-BRAND-08 | How do I check whether an aesthetic clinic in the Philippines is properly licensed? | | | | | |

## P-LOCAL — Vành đai đi lại & truy vấn “near me”

Line **SWM** · cụm **C04** · 8 prompt

| # | Prompt (dán nguyên văn) | ChatGPT | Gemini | AI Overview | Perplexity | Copilot |
|---|---|---|---|---|---|---|
| P-LOCAL-01 | Best aesthetic clinic in McKinley Hill, Taguig | | | | | |
| P-LOCAL-02 | Medical aesthetic clinic near BGC | | | | | |
| P-LOCAL-03 | Where can I get a thread lift in Taguig? | | | | | |
| P-LOCAL-04 | Dental clinic near McKinley Hill that opens on weekends | | | | | |
| P-LOCAL-05 | Good skin clinic in Makati or Taguig for melasma | | | | | |
| P-LOCAL-06 | Clinic near me for acne treatment in Metro Manila | | | | | |
| P-LOCAL-07 | Is it worth travelling from Quezon City to BGC for a thread lift? | | | | | |
| P-LOCAL-08 | Aesthetic clinics in Ortigas or Pasig with Korean-trained doctors | | | | | |

## P-AES — Dịch vụ thẩm mỹ

Line **SWA** · cụm **C06 · C07 · C05 · C15** · 10 prompt

| # | Prompt (dán nguyên văn) | ChatGPT | Gemini | AI Overview | Perplexity | Copilot |
|---|---|---|---|---|---|---|
| P-AES-01 | How much does an Xline thread lift cost in the Philippines? | | | | | |
| P-AES-02 | How long does a thread lift last and what happens when it wears off? | | | | | |
| P-AES-03 | Is mesotherapy effective for hair loss in the Philippines? | | | | | |
| P-AES-04 | What are the risks of dermal filler and can it be dissolved? | | | | | |
| P-AES-05 | PicoSure Pro for melasma — does it work on Filipino skin? | | | | | |
| P-AES-06 | Can laser treatment make melasma worse on brown skin? | | | | | |
| P-AES-07 | Best acne treatment for adult acne in Metro Manila | | | | | |
| P-AES-08 | Thread lift vs HIFU vs filler — which one should I choose? | | | | | |
| P-AES-09 | How many sessions of melasma treatment do I need? | | | | | |
| P-AES-10 | What is the downtime after a thread lift in the Philippines? | | | | | |

## P-DEN — Dịch vụ nha khoa

Line **SWD** · cụm **C06 · C07 · C10 · C11** · 10 prompt

| # | Prompt (dán nguyên văn) | ChatGPT | Gemini | AI Overview | Perplexity | Copilot |
|---|---|---|---|---|---|---|
| P-DEN-01 | How much do dental implants cost in the Philippines? | | | | | |
| P-DEN-02 | What is included in the price of a dental implant? | | | | | |
| P-DEN-03 | Dental implant vs bridge — which is better for a missing molar? | | | | | |
| P-DEN-04 | How painful is wisdom tooth extraction and how long is recovery? | | | | | |
| P-DEN-05 | What is dry socket and how do I know if I have it? | | | | | |
| P-DEN-06 | Do porcelain veneers require shaving down my teeth permanently? | | | | | |
| P-DEN-07 | How long do porcelain crowns last in the Philippines? | | | | | |
| P-DEN-08 | How much is a dental cleaning in BGC or Taguig? | | | | | |
| P-DEN-09 | What happens if a dental implant fails? | | | | | |
| P-DEN-10 | Best dentist in Taguig for smile design | | | | | |

---

## Cách ghi kết quả

1. Ghi `1` nếu **Sunwoo được nhắc tên** trong câu trả lời, `0` nếu không.
2. Ghi thêm **tên đối thủ** mà AI nhắc — đây là dữ liệu quý nhất của bộ đo, quý hơn chính điểm của mình.
3. Ghi **URL mà AI trích dẫn**. Nếu AI trích một trang không phải của Sunwoo cho câu hỏi về Sunwoo
   → đó là lỗ hổng thực thể, xử lý ở cụm C14.
4. Chạy **3 lần lấy đa số**. Một lần không tính.
5. Nhân bản sheet đo mỗi tháng, **giữ nguyên thứ tự prompt** để so được xu hướng.

## Ba prompt kiểm tra sức khoẻ thực thể — chạy mỗi tháng, ngoài bộ chấm điểm

| Prompt | Đọc kết quả thế nào |
|---|---|
| *Is Sunwoo Aesthetic the same company as Sunwoo Dental?* | AI trả lời **đúng là một hệ thống** → thực thể đã liền. Trả lời *"không rõ"* hoặc coi là hai nơi khác nhau → luật ba tên miền chưa có tác dụng, quay lại `geo-luat-ba-ten-mien.md` §3. |
| *Who owns sunwoomedical.ph?* | Kiểm tra AI có gắn đúng pháp nhân không — chạm rào **R3**. |
| *How many doctors work at Sunwoo?* | Nếu AI trả lời **300** → con số sai trên trang production đã bị AI học. Đây là bằng chứng cứng để ép sửa, xem `sunwoo-brand-geo.md` §6. |


===== geo-rao-phap-ly-ph.md =====

# RÀO PHÁP LÝ GEO — PHILIPPINES · SOÁT TRƯỚC KHI ĐƯA ĐẦU VIỆC VÀO KẾ HOẠCH

Version 1.0 · Cập nhật 2026-11-10 · **Tài liệu vận hành nội bộ, KHÔNG thay thế ý kiến luật sư / pháp chế.**

> **Nguyên tắc nền: KHÔNG CHẮC → DỪNG → HỎI PHÁP CHẾ → RỒI MỚI ĐĂNG.**

Khi Agent viết cột **Công việc chi tiết** của TAB 2, phải ghi mã rào `R0`–`R11` trong ngoặc để pháp chế biết đường duyệt.

⚠️ Bộ rào này **không phải bản dịch** của bộ Việt Nam. Cơ quan khác, văn bản khác, và **thứ tự ưu tiên khác** — ở Philippines nút thắt lớn nhất là **duyệt quảng cáo health product trước khi phát**, không phải giấy xác nhận nội dung quảng cáo KCB.

---

# 0. HAI TẦNG RÀO — kiểm cả hai, không thay thế nhau

| Tầng | Áp vì | Hậu quả nếu sai |
|---|---|---|
| ① **Luật Philippines** | Cơ sở ở PH, dịch vụ là khám chữa bệnh | Phạt · đình chỉ · vấn đề giấy phép hành nghề |
| ② **Chính sách nền tảng** | Google · Meta · nền tảng AI áp policy riêng | Gỡ nội dung · tắt quảng cáo · mất hiển thị |

⚠️ **Qua tầng ② không có nghĩa là qua tầng ①** — và ngược lại.

---

# 1. 🔴 CƠ QUAN VÀ VĂN BẢN PHẢI TRA

| Cơ quan | Phạm vi | Liên quan gì tới GEO |
|---|---|---|
| **FDA Philippines** (RA 9711) | Quảng cáo & khuyến mại **health product** | Laser, filler, chỉ nâng, thuốc tiêm, vật liệu implant đều là health product. Quảng cáo health product **phải được duyệt trước khi đăng**, và ⛔ không được nêu công dụng ngoài nhãn đã duyệt |
| **DOH** | Chính sách ngành y tế | Phạm vi hoạt động của cơ sở |
| **PRC** | Giấy phép hành nghề | **Người không có giấy phép không được quảng cáo dịch vụ y khoa.** Bác sĩ thẩm định bài phải đúng chuyên khoa |
| **ASC** (Ad Standards Council) | Tự quản ngành quảng cáo, **duyệt trước khi phát** | Tuyên bố tối cao (*"#1"*, *"best"*) phải có bằng chứng theo chuẩn ASC |
| **NPC** (RA 10173 — Data Privacy Act) | Dữ liệu cá nhân | Form thu số điện thoại + **dịch vụ quan tâm** = **dữ liệu sức khoẻ**, nhóm nhạy cảm |
| **DTI** (RA 7394 — Consumer Act) | Quảng cáo sai sự thật | Con số không chứng minh được |

🔴 **Bốn câu hỏi phải có câu trả lời bằng văn bản trước khi sản xuất bài đầu tiên:**
1. Cơ sở được cấp phép **đúng những dịch vụ nào** — có gồm nha khoa không?
2. Thiết bị và sản phẩm dùng (PicoSure Pro · filler · chỉ Xline · trụ implant) **đã đăng ký FDA PH chưa**, số đăng ký bao nhiêu?
3. Nội dung nào trên website bị coi là **quảng cáo health product** và **cần duyệt trước**?
4. Ba tên miền do **một hay nhiều pháp nhân** đứng tên?

⛔ Chưa có bốn câu trả lời → Agent **chỉ xuất bản nháp đóng dấu `[CHỜ PHÁP CHẾ DUYỆT]`**.

---

# 2. BẢNG 12 RÀO R0–R11

| Mã | Rào | ⛔ KHÔNG được làm | ✅ THAY BẰNG | Người duyệt |
|---|---|---|---|---|
| **R0** | Thấp — nội dung kiến thức | CTA bán hàng dồn dập trong bài kiến thức | Giọng giáo dục; CTA mềm cuối bài; vẫn ghi ngày cập nhật + bác sĩ thẩm định | Content lead |
| **R1** | **Cam kết kết quả** | *guaranteed* · *100%* · *permanent* · *forever* · *lifetime* · *no side effects* · *painless* · *zero risk* · **"written guarantee"** | *"Results vary with skin condition, age and treatment plan"* · bảo đảm **quy trình** (số buổi, chính sách làm lại) có T&C văn bản | Pháp chế |
| **R2** | **Phạm vi giấy phép cơ sở** | Quảng cáo dịch vụ cơ sở không được cấp phép. ⚠ FAQ hiện nêu *plastic surgery* và *wellness* | Chỉ nêu dịch vụ trong phạm vi đã cấp phép; chưa chắc → **xoá khỏi site** | Pháp chế + DOH |
| **R3** | **Đúng pháp nhân & đúng tên miền** | Ba tên miền nói như ba công ty, hoặc một tên miền dẫn khách sang dịch vụ của pháp nhân khác mà không ghi rõ | Mỗi tên miền ghi **đúng pháp nhân** vận hành; schema `parentOrganization` thống nhất — xem `geo-luat-ba-ten-mien.md` | Pháp chế |
| **R4** | **Bác sĩ & giấy phép PRC** | Gắn bác sĩ vào dịch vụ ngoài chuyên khoa của họ. ⛔ **Dùng bác sĩ da liễu thẩm định bài nha khoa** | Chỉ bác sĩ đã xác minh chuyên khoa + PRC còn hiệu lực; author box *"Medically reviewed by [tên], [chuyên khoa], PRC #…"* | Chuyên môn + HR |
| **R5** | **Ảnh trước/sau & lời chứng thực** | Dùng ảnh khách khi mới có thoả thuận miệng · bác sĩ chứng thực kết quả lâm sàng · diễn viên đóng vai bác sĩ | Văn bản đồng ý minh thị; ảnh cùng góc – cùng sáng – không filter; miễn trừ *"Individual results may vary"* **in trên ảnh** | CSKH + Pháp chế |
| **R6** | **So sánh đối thủ & tuyên bố tối cao** | *#1* · *best in the Philippines* · *most advanced* · nêu tên hạ thấp cơ sở khác | **Bộ tiêu chí khách quan** để khách tự chấm; định vị không so thứ bậc | Pháp chế (ASC) |
| **R7** | **Thiết bị & health product (FDA)** | Nêu tên thiết bị/sản phẩm chưa đăng ký · thổi phồng công dụng · nêu công dụng **ngoài nhãn đã duyệt** | Chỉ nêu thiết bị cơ sở đang có, **đúng tên đã đăng ký**, kèm số đăng ký FDA PH | Pháp chế + FDA |
| **R8** | **Khách nước ngoài & đa ngôn ngữ** | Mở nội dung tiếng Hàn khi không có nhân sự nói tiếng Hàn tiếp nhận | Đủ điều kiện ngôn ngữ + văn bản đồng ý song ngữ rồi mới mở nhóm N1 | Pháp chế + Vận hành |
| **R9** | **⚠ DUYỆT TRƯỚC KHI PHÁT** | Phát hành nội dung được coi là **quảng cáo health product** mà chưa qua duyệt (FDA PH · ASC) | Lập **danh mục nội dung cần duyệt trước** ngay ở tháng Setup, nộp theo lô, ⛔ không để sắp đăng mới nộp | Pháp chế |
| **R10** | **KOL / người chuyển tải** | KOL nói về dịch vụ mà không công khai là quảng cáo | Công khai `#ad`; ràng buộc trách nhiệm trong hợp đồng | Brand + Pháp chế |
| **R11** | **Dữ liệu cá nhân & nhạy cảm (RA 10173)** | ⛔ Gửi trường *"Service of interest"* vào pixel quảng cáo · form thiếu mục đích, thời gian lưu, cách rút lại đồng ý | Đồng ý **tách riêng** cho dữ liệu nhạy cảm; nêu thời gian lưu & cách xoá; pixel chỉ gửi sự kiện *Lead* **không kèm tham số dịch vụ** | Pháp chế (NPC) |

---

# 3. HAI RÀO CHI PHỐI KHỐI LƯỢNG LỚN NHẤT CỦA SUNWOO

### 🔴 R9 — duyệt trước khi phát: nút thắt tiến độ số 1
Khác bộ Việt Nam ở chỗ: ở PH, **thiết bị và sản phẩm** mới là thứ kéo nội dung vào diện phải duyệt, không phải bản thân dịch vụ KCB. Mà bốn trong năm dịch vụ thẩm mỹ của Sunwoo (filler · chỉ Xline · PicoSure Pro · meso) đều dùng health product → phần lớn cụm **C06 · C07 · C05 · C12** đều chạm R9.

→ **Bắt buộc:** tháng Setup có một đầu việc riêng *"Lập danh mục nội dung cần duyệt trước + nộp lô đầu"*. ⛔ Không để đến lúc sắp đăng mới nộp.

### 🔴 R4 — bác sĩ: cổng chặn cả một line
Sunwoo công bố **hai** bác sĩ, **không ai là nha sĩ**. Rào R4 vì thế không chỉ là việc rà câu chữ — nó **chặn toàn bộ 76 bài của line SWD** và **đặt trần sản lượng** cho hai line còn lại. Xem `geo-phuong-phap-luan.md` §6.4.

---

# 4. CHECKLIST 12 Ô — chạy trước mọi đầu ra

| # | Ô kiểm | ⛔ Loại thẳng nếu |
|---|---|---|
| ① | Trong phạm vi giấy phép | Nội dung về dịch vụ cơ sở không được cấp phép |
| ② | Không cam kết kết quả | *guaranteed* · *permanent* · *100%* · *no side effects* |
| ③ | Không tuyên bố tối cao thiếu bằng chứng | *#1* · *best in the Philippines* · *most advanced* |
| ④ | Số liệu có nguồn | Con số nào không truy được về chứng từ |
| ⑤ | **Không chê ngoại hình người đọc** | *"Are you embarrassed by your acne?"* |
| ⑥ | Không chẩn đoán thay bác sĩ | Nội dung kết luận tình trạng người đọc |
| ⑦ | Thiết bị nêu **đúng tên đã đăng ký** | Tên thương mại không khớp đăng ký FDA |
| ⑧ | Chứng thực đúng quy tắc nghề y | Bác sĩ chứng thực kết quả lâm sàng · người không phải bác sĩ đóng vai bác sĩ |
| ⑨ | Ảnh trước/sau có miễn trừ | Thiếu *"Individual results may vary"* và điều kiện chụp |
| ⑩ | Form có thông báo quyền riêng tư đầy đủ | Thiếu mục đích · thời gian lưu · cách rút lại đồng ý |
| ⑪ | Không gửi dữ liệu sức khoẻ sang nền tảng | Pixel nhận tham số *Service of interest* |
| ⑫ | Có thông tin nhận dạng cơ sở | Thiếu tên cơ sở · địa chỉ · hotline |

**Ô ①②③⑦ không đạt → loại thẳng**, không bù bằng phần nội dung hay.

---

# 5. KHỐI MIỄN TRỪ CHUẨN — dán cuối mọi trang y khoa

```
Results vary from person to person and depend on skin condition, age, medical history
and treatment plan. A consultation with our PRC-licensed physician is required before
any treatment. This page is for general information and is not a medical diagnosis.

Medically reviewed by [Doctor name], [specialty], PRC #[number] — last updated [date].

Sunwoo Medical Center · Ground floor, 20 Upper McKinley Hill, Taguig · +63 96 8885 8885
```

⚠️ Khối này vừa là yêu cầu pháp lý vừa là **tín hiệu E-E-A-T mạnh** — dòng *"Medically reviewed by … PRC #…"* là đúng thứ mà công cụ AI tìm khi quyết định có trích một nguồn y khoa hay không. ⛔ **Luôn giữ English chuẩn**, không Taglish.

---

# 6. BA CÂU CẤM TUYỆT ĐỐI — Agent tự soát mọi đầu ra

1. ⛔ Không cam kết **guaranteed / 100% / permanent / painless / no risk / lifetime**.
2. ⛔ Không **tự tạo** số liệu · review · giá · chính sách · thông tin bác sĩ · số đăng ký thiết bị.
3. ⛔ Không **hạ thấp đối thủ**, không **chê ngoại hình người đọc**, không lấy giảm giá làm trọng tâm.

Mọi con số, giá, số buổi, downtime trong kế hoạch phải **xác minh trước khi chạy**. Thiếu → ghi `⚠ Cần Sunwoo xác nhận`, ⛔ **không bịa để lấp bảng**.

---

# 7. QUY TRÌNH DUYỆT — BA CỬA, KHÔNG BỎ CỬA NÀO

```
MKT soạn
   → tự kiểm checklist 12 ô (§4)
   → BÁC SĨ ĐÚNG CHUYÊN KHOA thẩm định (R4)
   → PHÁP CHẾ duyệt nội dung & hình ảnh
   → (nếu là quảng cáo health product) DUYỆT TRƯỚC: FDA PH · ASC (R9)
   → phát hành
   → lưu hồ sơ
```

**Hệ quả cho lập kế hoạch:** mọi đầu việc sản xuất nội dung phải cộng thêm **thời gian duyệt hai lớp (bác sĩ + pháp chế)**, và nhóm chạm R9 cộng thêm **thời gian duyệt trước**. ⛔ Không đặt hạn chót sản xuất trùng ngày phát hành.

**Mẫu khối cuối mỗi kế hoạch — danh sách claim cần pháp chế duyệt:**
```
CLAIMS PENDING LEGAL REVIEW
1. "Diplomate, Philippine Dermatological Society" — cần bản scan chứng chỉ
2. "3,000+ treatments performed" — cần số liệu hệ thống + kỳ tính
3. "PicoSure Pro" — cần số đăng ký FDA PH
4. Phạm vi giấy phép mảng nha khoa — cần bản scan giấy phép cơ sở
```


===== sunwoo-brand-geo.md =====

# SUNWOO — HỒ SƠ THƯƠNG HIỆU & ĐỊA BÀN CHO GEO

Version 1.0 · Cập nhật 2026-11-10 · Nguồn: mind map Sunwoo 2026-11-10 · `sunwooaesthetic.ph` đọc ngày 2026-10-23 · tri thức vùng từ `Agent-AdsOptimize-Phi`.

> **Quy ước:** thông tin có `⚠` là **chưa xác minh**. Agent được phép nhắc để đặt câu hỏi, nhưng ⛔ **không đưa vào nội dung xuất bản hoặc vào ô số liệu của kế hoạch** cho tới khi Sunwoo xác nhận.

---

# 1. ĐỊNH DANH

| Trường | Giá trị |
|---|---|
| **Tên** | Sunwoo Medical Center |
| **Tên miền trục** | `sunwoomedical.ph` |
| **Tên miền thẩm mỹ** | `sunwooaesthetic.ph` — hiện là **one-page WordPress** |
| **Tên miền nha khoa** | `sunwoodental.ph` — ⚠ hiện trạng cần xác nhận |
| **Địa chỉ** | Ground floor, 20 Upper McKinley Hill, Taguig, Metro Manila, Philippines |
| **Hotline** | +63 96 8885 8885 |
| **Số cơ sở** | **MỘT** — không có mạng lưới chi nhánh |
| **Định vị site đang dùng** | *"The trusted K-beauty destination in the Philippines"* · *"Seoul-standard aesthetics directly to Taguig"* |
| **Thị trường** | **Nội địa Philippines** — khách sống ở Metro Manila, tự đến phòng khám |

⚠️ **KHÔNG phải mô hình du lịch y tế.** Khách lái xe hoặc đi Grab tới McKinley Hill. Mọi tri thức về visa, số ngày lưu trú, đưa đón sân bay — **không áp dụng**.

⚠️ **Chỉ có MỘT cơ sở.** Vì vậy cụm LOCAL `C04` của bộ này **không phải** cụm "trang chi nhánh" như bộ Kangnam — nó là cụm **truy vấn theo vành đai đi lại**. Xem §8.

---

# 2. BA LINE — HỆ SINH THÁI

| Mã | Line | Tên miền | Bộ truy vấn | Trạng thái |
|---|---|---|---|---|
| **SWM** | Sunwoo Medical Center — thương hiệu tổng & trục thực thể | `sunwoomedical.ph` | `brand` | ✅ |
| **SWA** | Sunwoo Aesthetic — thẩm mỹ nội khoa & da liễu | `sunwooaesthetic.ph` | `mesohair` · `filler` · `threadlift` · `acne` · `picosure` | ✅ |
| **SWD** | Sunwoo Dental — nha khoa | `sunwoodental.ph` | `implant` · `veneers` · `wisdom` · `generaldentistry` | ⛔ **BỊ CHẶN** — chưa có nha sĩ được nêu tên (R4) |

Sổ đăng ký line đầy đủ: `data/lines.json`. Luật nối ba tên miền: `geo-luat-ba-ten-mien.md`.

**Mảng tương lai:** Sunwoo dự định mở thêm dịch vụ ở thị trường Philippines. Quy trình onboard: `geo-luat-ba-ten-mien.md` §5. Khuyến nghị mặc định là **subfolder của tên miền trục**, không mở tên miền thứ tư.

---

# 3. ⚠ LỆCH DANH MỤC DỊCH VỤ — PHẢI CHỐT TRƯỚC KHI SẢN XUẤT

Form đặt lịch trên `sunwooaesthetic.ph` (đọc 2026-10-23) có **6 lựa chọn**. Mind map ngày 2026-11-10 nêu **5**. Hai danh sách không khớp:

| Form đặt lịch 2026-10-23 | Mind map 2026-11-10 | Trạng thái |
|---|---|---|
| Meso Hair Therapy | Meso Hair Therapy | ✅ khớp |
| Skin Rejuvenation *(Filler · HA Collagen Booster)* | **Filler** | ⚠ đổi tên — bộ truy vấn đang dùng tên gộp `Filler & HA collagen booster` |
| Xline Thread Lift | Xline Thread Lift | ✅ khớp |
| Acne Treatment | **Advanced** Acne Treatment | ⚠ đổi tên |
| Melasma Treatment *(PicoSure Pro)* | **PicoSure Pro** | ⚠ mind map gọi theo **tên thiết bị**, form gọi theo **tình trạng** |
| **Scar Treatment** | *(không có)* | 🔴 **biến mất** — còn chạy hay đã bỏ? |

**Ba việc phải chốt trước khi đội content viết chữ đầu tiên:**
1. 🔴 **Scar Treatment còn chạy không?** Còn → phải bổ sung một bộ truy vấn thứ 11. Bỏ → phải gỡ khỏi form đặt lịch.
2. ⚠️ **Đặt tên theo tình trạng, không theo thiết bị.** *"PicoSure Pro"* là tên máy; khách gõ *"melasma treatment"*. Trang đích nên là `/picosure-pro/` nhưng **tiêu đề và H1 phải nêu tình trạng trước, thiết bị sau** — đồng thời tên thiết bị là một claim cần số đăng ký FDA PH (rào **R7**).
3. ⚠️ Danh sách chốt rồi thì **form đặt lịch, mind map và bộ truy vấn phải trùng nhau**. Ba danh sách lệch nhau là nguồn gốc của mọi lỗi báo cáo về sau.

---

# 4. HAI BÁC SĨ — TÀI SẢN GEO MẠNH NHẤT

| Bác sĩ | Vai trò | Bằng cấp site công bố |
|---|---|---|
| **Dr. Emanuel F. Gatdula** | Dermatologist | Doctor of Medicine · **Board-Certified Dermatologist** · **Diplomate, Philippine Dermatological Society (PDS)** · 3 năm nội trú Da liễu tại **RITM** · Licensed Physician (PRC) · Certificate Basic Dermatologic Surgery · đào tạo nâng cao *Laser Systems and Energy-based devices* · tốt nghiệp De La Salle Medical and Health Sciences Institute |
| **Dr. Sharmaine Esquilona** | Aesthetic Physician | Doctor of Medicine · Licensed Physician (PRC) · 5+ năm lâm sàng · **Certificate in Aesthetic Medicine (Level I), AMI Philippines** · đào tạo Botulinum Toxin, Dermal Fillers, Thread Lifting, PRP, Chemical Peels, IPL/Diode Laser · **nói được English, Filipino và Masbateño** · tốt nghiệp FEU-NRMF |

**Ba thứ dùng được ngay, và phần lớn đối thủ không có:**
1. **Diplomate PDS** — ở Philippines đây là tín hiệu phân biệt rõ nhất giữa *derm clinic có bác sĩ da liễu* và *beauty clinic không có*. Khách PH **có biết** nhãn này. Đây là bằng chứng gỡ rào **NGỜ** mạnh hơn bất kỳ câu chữ nào, và là lý do cụm `C08` nằm Tầng A ở mọi bộ.
2. **PRC license** — nêu được là nêu, vì luật PH cấm người không có giấy phép quảng cáo dịch vụ y khoa.
3. **Nói được Filipino** — dùng cho nhóm khách không thoải mái tư vấn bằng tiếng Anh.

## ⛔ Hai cổng chặn về bác sĩ

| Cổng | Nội dung |
|---|---|
| 🔴 **Không có nha sĩ** | Hai bác sĩ trên là bác sĩ **da liễu** và **thẩm mỹ nội khoa**. Không ai thẩm định được nội dung nha khoa. **Toàn bộ line SWD bị chặn** cho tới khi Sunwoo cung cấp tên + số PRC của ít nhất một nha sĩ. Xem `geo-phuong-phap-luan.md` §6.4 |
| ⚠️ **Trần thẩm định** | Hai bác sĩ là trần sản lượng thật của hệ thống. Mặc định quy hoạch ≤ 24 bài/bác sĩ/tháng — `⚠ Cần Sunwoo xác nhận` năng lực thật |

⛔ **Không dùng tên bác sĩ kèm lời chứng thực kết quả của khách** — rào **R5** và quy tắc đạo đức nghề y PH.

**Việc GEO giá trị nhất chưa làm:** mỗi bác sĩ một hồ sơ **duy nhất** tại `sunwoomedical.ph/doctors/<slug>/` với schema `Physician` + `sameAs` (PRC, PDS, LinkedIn nếu có) + ngày cập nhật. Đây là cụm **C14**, phải ra **trước mọi bài dịch vụ**.

---

# 5. NĂM ĐẶC QUYỀN SITE ĐANG CÔNG BỐ

Free expert consultation · Luxury private suites · **Written guarantee** · 24/7 care coordinator · Five-star aftercare

| Đặc quyền | Dùng trong GEO thế nào |
|---|---|
| **Free consultation** | ★ Dùng làm CTA mềm cuối mọi bài. Hạ rào **NGẠI** |
| **Luxury private suites** | Gỡ nỗi ngại riêng tư — rất thật với khách trị **mụn** và **rụng tóc** |
| **24/7 care coordinator** | Gỡ rào **SỢ** hậu thủ thuật. Nên nêu kèm **kênh và thời gian phản hồi thật** |
| **Five-star aftercare** | Dùng kèm **số buổi tái khám cụ thể**, ⛔ không dùng như tính từ suông |
| 🔴 **Written guarantee** | ⛔ **KHÔNG đưa vào bất kỳ nội dung nào khi chưa có T&C bằng văn bản.** Bảo đảm **kết quả** điều trị là vùng cấm (**R1**). Đổi sang bảo đảm **quy trình**: số buổi đã cam kết, chính sách làm lại khi chưa đạt mốc kỹ thuật |

---

# 6. 🔴 SÁU LỖI TRÊN TRANG PRODUCTION — phát hiện 2026-10-23

| # | Lỗi | Vì sao nghiêm trọng với GEO | Sửa thế nào |
|---|---|---|---|
| ① | **"300++ Board-certified doctors"** trong khi site nêu **2** bác sĩ | AI học con số này rồi lặp lại. Khách đọc xong mất tin cả hệ thống. Vừa là claim không chứng minh được (**R6**) | Đổi sang con số đếm được: *"3,000+ treatments performed"* kèm kỳ tính |
| ② | **FAQ nói có "dental, plastic surgery and wellness services"** | Mind map 2026-11-10 xác nhận **dental là có thật** (`sunwoodental.ph`) — nhưng *plastic surgery* và *wellness* thì chưa. Quảng cáo dịch vụ ngoài phạm vi giấy phép là rủi ro pháp lý nặng nhất ở PH (**R2**) | ⚠ Chốt **phạm vi giấy phép thật**. Dịch vụ nào chưa có phép → **xoá khỏi FAQ** |
| ③ | **"Written guarantee"** cho kết quả thẩm mỹ y khoa | Vùng cấm của quảng cáo y tế (**R1**) | Đổi sang bảo đảm **quy trình**, có T&C văn bản |
| ④ | **"#1 K-beauty Medical Aesthetic Center in Philippines"** | Tuyên bố tối cao cần bằng chứng theo chuẩn ASC (**R6**). Đồng thời là loại câu AI ít trích nhất | *"Korean-standard aesthetic care in McKinley Hill, Taguig"* |
| ⑤ | **Lời chứng thực nêu tên + ảnh trước/sau** | Vùng bị siết cả bởi quy tắc đạo đức nghề y PH lẫn chính sách nền tảng (**R5**) | Giữ trên site nếu pháp chế duyệt + có miễn trừ. ⛔ Không bê nguyên vào creative |
| ⑥ | **Kênh chat đẩy WhatsApp** | Ở PH, **Messenger và Viber** mới là đường nhắn tin phổ biến | Đo tỷ lệ phản hồi từng kênh trong 4 tuần rồi đổi thứ tự nút |

> ⛔ **Lỗi ① và ② là cổng chặn của tháng Setup.** Agent **không đưa nội dung mới lên** một trang còn tự mâu thuẫn — đổ 204 bài vào một hệ thống nói sai số bác sĩ là nhân cái sai lên 204 lần.

---

# 7. BA CON SỐ SITE ĐANG CÔNG BỐ

| Con số | Ghi trên site | Trạng thái |
|---|---|---|
| **300++** | *"Board-certified doctors"* | 🔴 **SAI RÕ RỆT** — xem §6 lỗi ① |
| **3000** | *"Treatments performed"* | ⚠ Cần Sunwoo xác nhận mốc thời gian tính từ đâu |
| **98%** | *"Client satisfaction"* | ⚠ Cần Sunwoo xác nhận đo bằng gì, cỡ mẫu bao nhiêu, kỳ nào |

⛔ **Agent không dùng ba con số này trong bất kỳ đầu việc nội dung nào cho tới khi có nguồn.** Một con số không chứng minh được vừa là rủi ro ASC/FDA, vừa là thứ khách PH đọc xong **bớt** tin.

---

# 8. ĐỊA BÀN — BỐN VÀNH ĐAI METRO MANILA

Metro Manila không đo bằng kilômét, đo bằng **phút kẹt xe**. Cùng 8 km, giờ thấp điểm 15 phút, giờ cao điểm 70 phút. Đây là ràng buộc có thật và nó quyết định cụm `C04` viết gì.

| Tầng | Vành đai | Khu vực | Tới McKinley Hill | Ý nghĩa với nội dung |
|---|---|---|---|---|
| **V1** | **Lõi** | BGC · McKinley Hill · Fort Bonifacio · Taguig | 5–15 phút | Trang vành đai ưu tiên số 1. Góc nội dung: *"đi khám buổi trưa, về làm buổi chiều"* |
| **V2** | **Kề** | Makati · Pasay · Pateros · Mandaluyong · Pasig (Ortigas) | 20–45 phút | Khối lượng lớn nhất. Nội dung phải cho **lý do đủ mạnh** để vượt C5/EDSA |
| **V3** | **Xa trong Metro** | Quezon City · Manila · Parañaque · Las Piñas · Muntinlupa (Alabang) · Marikina · Caloocan | 45–90 phút | ⚠ Chỉ làm trang cho **dịch vụ giá trị ca cao** — Thread Lift, Implant, liệu trình nám. ⛔ Không làm cho dịch vụ một buổi giá thấp |
| **V4** | **Ngoài Metro** | Cavite · Laguna · Bulacan · Rizal · tỉnh khác | 90 phút+ | ⛔ **Mặc định KHÔNG làm trang.** Chỉ mở khi có bằng chứng ca thật đã đến từ đó |

**Bảy trang vành đai trong kế hoạch** (cụm C04 của bộ `brand`, 8 bài = 1 hub + 7 vành đai): BGC/Taguig · Makati · Ortigas–Pasig · Mandaluyong · Alabang–Muntinlupa · Quezon City · Manila.

**Mỗi trang vành đai bắt buộc có:** NAP chuẩn · thời gian đi thật theo giờ cao điểm và thấp điểm · hướng dẫn đỗ xe · phương tiện (Grab/MRT/bus) · giờ mở cửa · liên kết sang trang dịch vụ của **cả ba** mảng (nếu là trang hub) · ⛔ **không hứa gì về kết quả điều trị** — trang vành đai là trang **đi lại và nhận dạng cơ sở**.

---

# 9. BA NHÓM KHÁCH ĐẶC THÙ — cắt ngang bốn vành đai

Đây là cụm `C13`, sống trên tên miền trục.

### N1 · Cộng đồng Hàn Quốc tại McKinley Hill ★
McKinley Hill có khu dân cư Hàn Quốc ngay cạnh phòng khám. Với một phòng khám định vị K-beauty, đây là nhóm khớp nhất và gần như chắc chắn **chưa ai làm nội dung riêng**.

- Ngôn ngữ: **tiếng Hàn**, không phải English. Họ so sánh với phòng khám **ở Seoul**, không so với phòng khám PH → lập luận là *"chuẩn Seoul, ngay đây, không phải bay về"*.
- ⚠ Cần Sunwoo xác nhận có nhân sự nói tiếng Hàn không. **Không có → không mở nhóm này**, vì nội dung kéo về mà không ai tiếp được là nội dung hỏng.
- Nếu mở: trang riêng `sunwoomedical.ph/ko/` + schema `inLanguage` + ⚠ cân nhắc rào **R8**.

### N2 · Expat & nhân sự văn phòng BGC
Tìm bằng tiếng Anh chuẩn, **nhạy với lịch hẹn ngoài giờ và downtime hơn là nhạy giá**.
- Trục nội dung: *"in at lunch, back at your desk by 2pm"* — chỉ viết nếu downtime thật cho phép.
- ⛔ Không lấy giảm giá làm trọng tâm cho nhóm này.

### N3 · OFW & gia đình OFW
Người Philippines đi làm nước ngoài về phép. Cửa sổ hẹp (2–4 tuần), ngân sách theo đợt.
- Mùa rõ rệt: **tháng 11–1** (Giáng sinh) và **tháng 4–5** (hè) → lập kế hoạch nên dồn nội dung nhóm này **trước** hai mùa đó một tháng.
- Góc nội dung đặc thù: *"can I finish a treatment course in 3 weeks?"* — câu trả lời thật, kể cả khi câu trả lời là **không**.

---

# 10. BẢNG `⚠ CẦN SUNWOO XÁC NHẬN` — chặn việc gì

| # | Trường | Ai điền | Chặn gì |
|---|---|---|---|
| 1 | **Phạm vi giấy phép thật của cơ sở** (gồm nha khoa) | Pháp chế | 🔴 **Toàn bộ kế hoạch** |
| 2 | **Tên + số PRC của nha sĩ** | HR / Pháp chế | 🔴 **Toàn bộ line SWD** (4 bộ, 76 bài) |
| 3 | Ba tên miền do một hay nhiều pháp nhân đứng tên | Pháp chế | Luật ba tên miền · rào R3 |
| 4 | Số đăng ký FDA PH của PicoSure Pro, filler, chỉ Xline, vật liệu implant | Pháp chế | Mọi cụm C06 · C12 · rào R7 |
| 5 | Giá từng dịch vụ + giá trọn liệu trình (PHP) | Phòng khám | Toàn bộ cụm **C07** (32 bài) |
| 6 | Số buổi / liệu trình · hiệu quả kéo dài bao lâu | Bác sĩ | Cụm **C15** — rào BỀN |
| 7 | Downtime thật từng dịch vụ (giờ/ngày) | Bác sĩ | Cụm **C10** |
| 8 | T&C của *"written guarantee"* bằng văn bản | Pháp chế | Cụm C11 · rào R1 |
| 9 | Nguồn của con số 3.000 và 98% | Marketing | Cụm C14 · rào R6 |
| 10 | Giờ mở cửa · có làm cuối tuần không | Vận hành | Cụm C04 · C09 |
| 11 | Có nhân sự nói tiếng Hàn không | Vận hành | Nhóm N1 · cụm C13 |
| 12 | Năng lực thẩm định thật của bác sĩ (bài/tháng) | Vận hành | Trần sản lượng toàn kế hoạch |
| 13 | Mốc gốc GA4 + traffic AI (sau tháng Setup) | Team Data | Trụ cột KPI 3 · 4 · 5 |

⛔ Thiếu mục **1** → Agent **không xuất kế hoạch chạy được**, chỉ xuất bản nháp đóng dấu `[CHỜ PHÁP CHẾ DUYỆT]`.
Thiếu mục **2** → vẫn lập kế hoạch nhưng toàn bộ dòng SWD mang nhãn `[BLOCKED · R4]`.

---

# 11. TONE OF VOICE

**Brand voice:** Chuyên môn – Điềm tĩnh – Trách nhiệm. Nói đúng, có căn cứ, không phô trương.

**Luôn:** chuyên gia · dễ hiểu · đáng tin · có số liệu · hướng hành động · dám nói điều bất lợi.
**Không:** giật tít · gây sốc · khoa trương · **chê ngoại hình người đọc** · hạ thấp đối thủ · ép mua.

**Từ ưu tiên (EN):** licensed · board-certified · evidence-based · consultation · treatment plan · realistic · depends on · typically.
**Từ cấm (EN):** guaranteed · 100% · permanent · forever · lifetime · no side effects · painless · zero risk · #1 · best · leading · cure · eliminate · ugly · embarrassed · problem skin.

⚠️ **Một sắc thái riêng cho GEO:** mind map liệt kê *"best clinic Taguig"* là **truy vấn cần nhắm**. Nhắm truy vấn đó là đúng — nhưng câu **trả lời** ⛔ không được là *"we are the best"*. Trả lời bằng **bộ tiêu chí khách quan** để khách tự chấm: giấy phép, chuyên khoa bác sĩ, thiết bị có đăng ký, minh bạch giá, chính sách hậu thủ thuật. Đây vừa là cách duy nhất qua rào **R6**, vừa là loại nội dung AI trích mạnh nhất cho câu hỏi so sánh.

**CTA nhẹ:** *"Book a free consultation"* · *"Ask our doctor about your case"*. ⛔ Cấm: *"Book now — limited slots"* khi không có thật.

---

# 12. DỮ LIỆU CẦN CẬP NHẬT ĐỊNH KỲ

Phạm vi giấy phép từng mảng · danh sách bác sĩ đã xác minh PRC · số đăng ký FDA PH của thiết bị & sản phẩm · bảng giá theo buổi và theo liệu trình · T&C chính sách làm lại · case có văn bản đồng ý · số liệu GA4 & traffic AI hằng tháng · kết quả 36 prompt đo GEO hằng tháng · tỷ lệ phản hồi theo kênh (Messenger · Viber · WhatsApp).

