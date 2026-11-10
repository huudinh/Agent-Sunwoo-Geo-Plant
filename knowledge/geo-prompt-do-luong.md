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

