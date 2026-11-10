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
