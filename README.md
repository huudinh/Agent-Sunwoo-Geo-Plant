# 🧭 Sunwoo GEO Planner

> Version 1.0 · AI lập **kế hoạch GEO (Generative Engine Optimization)** theo tháng cho hệ sinh thái **Sunwoo Medical Center** tại Philippines — đầu ra là file Excel **2 TAB: KPI + Công việc triển khai**.

Đóng vai **Growth Operating AI**: đọc 10 bộ truy vấn GEO → xác định đối tượng & rào cản theo 6 giai đoạn hành trình → xếp ưu tiên cụm theo 80/20 → quy ra khối lượng bài viết → **định tuyến từng bài về đúng một trong ba tên miền** → rải theo tháng → gắn KPI đo được và người phụ trách.

---

## Nguyên tắc tối thượng

> **Sunwoo không đi kể chuyện mình là K-beauty. Sunwoo đi theo hành trình của một người đang ở Metro Manila, gỡ từng nỗi lo, rồi mới xuất hiện như lời giải.**

| Cách cũ (brand-first) | Cách của Agent này (customer-journey-first) |
|---|---|
| *"The #1 K-beauty medical aesthetic center in the Philippines"* | *"Can laser treatment make melasma worse on brown skin?"* |
| Nội dung xoay quanh **chúng tôi có gì** | Nội dung xoay quanh **khách đang sợ gì** |
| Đo bằng thứ hạng từ khoá | Đo bằng **AI có trích dẫn Sunwoo không** |
| Né chủ đề rủi ro, biến chứng, giá | **Chiếm lĩnh** chủ đề đó — vì đó là nơi khách quyết định |

---

## Quy tắc ngôn ngữ — hai lớp, không trộn

| Lớp | Ngôn ngữ | Gồm |
|---|---|---|
| **Lớp khách Philippines** | **TIẾNG ANH** | Truy vấn · từ khoá · tên cụm chủ đề · tiêu đề bài · URL trang đích · 36 prompt đo GEO · mọi câu chữ lên website |
| **Lớp vận hành HCI** | **TIẾNG VIỆT** | Phân tích · nỗi sợ khách · mô tả đầu việc · tên cột bảng · ghi chú pháp lý · toàn bộ phần Agent nói trong chat |

---

## Trục 6 bước

```
① Chọn lĩnh vực  →  ② Đối tượng KH  →  ③ Giai đoạn hành trình (S1–S6)
      →  ④ Cụm truy vấn (EN)  →  ⑤ Cụm nội dung + TÊN MIỀN  →  ⑥ GEO/SEO
```

Mọi bài phải **truy ngược được** về một cụm → một giai đoạn → một rào cản của một đối tượng thật. Bài nào không truy ngược được → loại khỏi kế hoạch.

**6 giai đoạn:** S1 Nhận biết · S2 Tìm hiểu · **S3 Cân nhắc & nỗi sợ ★★★ (điểm quyết định, ~50–60% điểm ưu tiên)** · S4 Thực hiện · S5 Trải nghiệm & hậu thủ thuật · S6 Gắn bó & mở rộng.

**4 rào cản nền — bản Philippines:** **NGỜ** (không biết tin ai) · **NGẠI** (đi lại, riêng tư, bị bán thêm) · **SỢ** (hỏng, không đảo ngược được) · **BỀN ★** (*"hết tác dụng rồi tôi trả tiếp bao nhiêu"* — rào đặc thù gói nội địa PH, không có trong bộ Việt Nam).

---

## ⚠ Ba ràng buộc riêng của Sunwoo — thứ làm bộ này khác bộ Kangnam

### ① Ba tên miền là ba thực thể
`sunwoomedical.ph` (trục) · `sunwooaesthetic.ph` · `sunwoodental.ph` — cho **một** phòng khám ở McKinley Hill, Taguig. GEO giải thực thể, nên ba tên miền không nối với nhau = uy tín không cộng dồn, AI trả lời *"không chắc"*, hồ sơ bác sĩ bị tách đôi.

→ **7 luật L1–L7 + bảng định tuyến cụm → tên miền:** [`knowledge/geo-luat-ba-ten-mien.md`](knowledge/geo-luat-ba-ten-mien.md).
Bốn cụm `C08 · C12 · C13 · C14` của **mọi bộ** xuất bản trên tên miền trục, gộp thành trang dùng chung. Script tự định tuyến, không cần nhớ tay.

### ② Cổng duyệt bác sĩ — trần sản lượng thật
Sunwoo công bố **hai** bác sĩ, **không ai là nha sĩ**.

- Toàn bộ **line nha khoa (4 bộ · 76 bài)** mang nhãn `[BLOCKED · R4]` — sản xuất được, ⛔ **không phát hành được**.
- Trần phát hành mặc định **≤ 24 bài/bác sĩ/tháng** → 48 bài/tháng. Vượt trần → Agent cảnh báo và đề xuất giãn, ⛔ không im lặng nhận chỉ tiêu.
- KPI đếm theo **"đã phát hành"**, không đếm "đã sản xuất". Hai con số khác nhau và bảng phải nhìn ra ngay.

### ③ Hai lỗi cổng chặn trên trang production
Con số *"300++ board-certified doctors"* (site chỉ có 2) và FAQ nêu *"plastic surgery and wellness"* ngoài phạm vi giấy phép. ⛔ Không đổ 204 bài lên một hệ thống còn tự mâu thuẫn — sửa trong tháng Setup.

---

## Kho dữ liệu

**10 bộ dịch vụ · 150 cụm chủ đề · 2.550 truy vấn · 204 bài viết cần sản xuất**

| Line | Tên miền | Bộ dịch vụ | Bài | Trạng thái |
|---|---|---|---|---|
| **SWM** Sunwoo Medical Center | `sunwoomedical.ph` | Thương hiệu tổng & local | 26 | ✅ |
| **SWA** Sunwoo Aesthetic | `sunwooaesthetic.ph` | Meso Hair · Filler · Xline Thread Lift · Acne · PicoSure Pro | 102 | ✅ |
| **SWD** Sunwoo Dental | `sunwoodental.ph` | Smart Bio Implant · Veneers · Wisdom extraction · General dentistry | 76 | ⛔ **BỊ CHẶN (R4)** |

> 🔶 **Bản nháp v1.** Số liệu suy từ mind map 2026-11-10 + hồ sơ thương hiệu đọc 2026-10-23. Sunwoo **chưa có mốc traffic AI** nên *Cơ hội GEO* = 1 cho mọi cụm. Sau tháng Setup phải chấm lại và chạy lại `tools/build-index.py`.

**Mảng tương lai:** thêm một mảng = thêm **1 file JSON + 1 khối trong `data/lines.json`**, ⛔ không sửa bộ não, không sửa `tools/`. Quy trình 6 bước: [`geo-luat-ba-ten-mien.md` §5](knowledge/geo-luat-ba-ten-mien.md). Khuyến nghị mặc định là **subfolder của tên miền trục**, không mở tên miền thứ tư.

---

## Kiến trúc 3 tầng

- **Bộ não:** [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) — dán vào ô Chỉ dẫn/Instructions.
- **Tri thức:** [`knowledge/`](knowledge/) — 8 file `.md` upload vào Knowledge.
- **Dữ liệu nguồn:** [`data/`](data/) — JSON, **không upload**; dùng cục bộ để sinh lại tri thức.

---

## Quick start (3 bước)

1. **Instructions:** dán toàn bộ khối giữa hai vạch ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md).
2. **Knowledge:** upload 8 file `.md` trong [`knowledge/`](knowledge/).
3. **Template:** upload [`template/GEO-SUNWOO-MAU-6-THANG.xlsx`](template/) để Agent bám format.

→ Chi tiết từng nền tảng + smoke test 7 câu: [doc/01-cai-dat.md](doc/01-cai-dat.md)

**Câu lệnh đầu tiên để test:**
```
Bạn là ai, làm được gì? Nêu trục 6 bước, cho biết Sunwoo có bao nhiêu bài cần
sản xuất, và line nào đang bị chặn vì sao.
```

**Câu lệnh lập kế hoạch:**
```
Lập kế hoạch GEO toàn hệ thống Sunwoo trong 6 tháng, bắt đầu từ tháng 01/2027.
Xuất file 2 TAB theo mẫu.
```

---

## Đầu ra — 2 TAB

| TAB | Nội dung |
|---|---|
| **`BẢNG TỔNG QUAN KPI`** | 5 trụ cột (Hạ tầng 3 tên miền & Thực thể 0,10 · Sản lượng 0,20 · SEO&GEO 0,40 · Traffic 0,15 · Lead&Booking 0,15). ⚠ Trụ cột 3–4 cắt theo **tên miền**; trụ cột 2–5 cắt theo **line**. Số cột tháng co giãn. |
| **`CÔNG VIỆC TRIỂN KHAI`** | **11 cột** — thêm cột **`Tên miền`** so với bộ Kangnam. Bốn cấp dòng: chi tiết (kem) → **bị chặn (hồng)** → `▶ TỔNG line` (mint) → `★ TỔNG SẢN LƯỢNG THÁNG` (amber). Panel phải: sản lượng theo tháng · **trần thẩm định bác sĩ** · tiến độ. |

Output mẫu có số thật: [doc/03-output-mau.md](doc/03-output-mau.md)

---

## Công cụ

```bash
pip install openpyxl

python tools/build-index.py                                 # sinh lại 2 file tri thức từ data/
python tools/build-geo-plan.py --start 2027-01 --months 6   # sinh kế hoạch 2 TAB
python tools/build-geo-plan.py --start 2027-01 --months 4 --scope brand,threadlift,filler
python tools/build-geo-plan.py --start 2027-01 --months 6 --tran 30
python tools/gop-tham-khao.py                               # gộp 8 file tri thức thành 1
```

---

## Tài liệu

| File | Nội dung |
|---|---|
| [SYSTEM-PROMPT.md](SYSTEM-PROMPT.md) | Bộ não Agent — dán vào Instructions |
| [knowledge/geo-phuong-phap-luan.md](knowledge/geo-phuong-phap-luan.md) | Trục 6 bước · S1–S6 · 4 rào cản PH · 80/20 · **cổng duyệt bác sĩ** · quy tắc rải tháng |
| [knowledge/geo-luat-ba-ten-mien.md](knowledge/geo-luat-ba-ten-mien.md) | ★ 7 luật nối ba tên miền · bảng định tuyến cụm · **khung mở line mới** |
| [knowledge/geo-bo-truy-van-index.md](knowledge/geo-bo-truy-van-index.md) | Chỉ mục 10 bộ · 150 cụm · 204 bài *(sinh tự động)* |
| [knowledge/geo-prompt-do-luong.md](knowledge/geo-prompt-do-luong.md) | 36 prompt đo GEO tiếng Anh × 5 nền tảng *(sinh tự động)* |
| [knowledge/sunwoo-brand-geo.md](knowledge/sunwoo-brand-geo.md) | Sunwoo là ai · 2 bác sĩ · 6 lỗi trang production · 4 vành đai Metro Manila · bảng cần xác nhận |
| [knowledge/geo-kpi-framework.md](knowledge/geo-kpi-framework.md) | 5 trụ cột KPI bản PH · cách đặt chỉ tiêu · 15 mã KPI nền |
| [knowledge/geo-rao-phap-ly-ph.md](knowledge/geo-rao-phap-ly-ph.md) | 12 rào R0–R11 bản Philippines (FDA · DOH · PRC · ASC · NPC · DTI) |
| [knowledge/geo-output-excel-schema.md](knowledge/geo-output-excel-schema.md) | Khoá format 2 TAB · bảng màu · cột `Tên miền` · dòng hồng |
| [goi/](goi/) | **Bản gộp dự phòng** — 1 file thay cho 8, dùng khi chạm trần số file |
| [doc/01-cai-dat.md](doc/01-cai-dat.md) | Cài Gemini/ChatGPT/Claude · chiến lược file · smoke test · sự cố |
| [doc/02-cau-lenh.md](doc/02-cau-lenh.md) | Công thức ra lệnh · 12 prompt mẫu · điều Agent sẽ từ chối |
| [doc/03-output-mau.md](doc/03-output-mau.md) | Output mẫu có số thật · dấu hiệu đúng/sai |
| [doc/CHANGELOG.md](doc/CHANGELOG.md) | Lịch sử cập nhật · việc còn treo |

---

## Cấu trúc repo

```
SYSTEM-PROMPT.md   Bộ não Agent
knowledge/         8 file tri thức (.md) — upload vào Knowledge; 2 file sinh tự động
data/              lines.json · query-sets/*.json · geo-prompts.json — nguồn sự thật
doc/               Hướng dẫn cài đặt · câu lệnh · output mẫu · changelog
goi/               Bản gộp dự phòng
template/          File mẫu Excel 2 TAB
tools/             build-index.py · build-geo-plan.py · gop-tham-khao.py
out/               File kế hoạch sinh ra (không commit)
```

---

## Ranh giới — Agent sẽ cảnh báo, không im lặng làm theo

⛔ Không cam kết *guaranteed / 100% / permanent / painless* (**R1**) · không tuyên bố *#1 / best* thiếu bằng chứng ASC (**R6**) · không quảng cáo dịch vụ ngoài phạm vi giấy phép (**R2**) · **không dùng bác sĩ da liễu thẩm định bài nha khoa** (**R4**) · không nêu sai tên thiết bị đã đăng ký FDA PH (**R7**) · không chê ngoại hình người đọc · không gửi *Service of interest* vào pixel quảng cáo (**R11** — RA 10173) · **không bịa số liệu** — thiếu thì ghi `⚠ Cần Sunwoo xác nhận`.

*Agent không phải luật sư. Mọi phần pháp lý là hướng dẫn vận hành, phải qua pháp chế của phòng khám. Quyết định cuối luôn thuộc người dùng.*
"# Agent-Sunwoo-Geo-Plant" 
