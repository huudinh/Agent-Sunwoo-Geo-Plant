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
