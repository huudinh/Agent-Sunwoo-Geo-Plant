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
