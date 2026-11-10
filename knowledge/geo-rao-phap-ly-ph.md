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
