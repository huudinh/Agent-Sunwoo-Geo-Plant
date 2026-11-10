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
