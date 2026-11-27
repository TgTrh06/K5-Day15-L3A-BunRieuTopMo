# Phân công công việc & Chỉ dẫn Checkpoint 4 (CP4) — Nhóm BunRieuTopMo

> **Track A · A2 (Trợ lý Discord)**  
> **Hạn nộp CP4:** `14:30 Thứ Bảy 28/11/2026` *(Demo Zone 14:30–16:00 · Demo Phòng 16:00–18:00 · Hạn chót 23:59)*  
> **Lưu ý nhân sự:** **Nguyễn Phú Nam** bận việc trong chặng CP4 — 3 thành viên còn lại (*Trịnh Thanh Tùng, Trương Hoàng Tùng, Nguyễn Hoàng*) chia nhau hoàn tất toàn bộ hạng mục CP4.  
> **Lợi thế hiện tại:** Nhóm đã xong sớm Lượt 1 (`22/24 = 92%`), cải tiến prompt và Lượt 2 (`24/24 = 100%`), video 30s và `spec.md` §0–§7, §9, §10.

---

## Luật cứng (tránh mất điểm ở CP4 & Demo)

1. **Không sửa chuẩn "đạt"** (`spec.md` §7 và `eval/metric_spec.yaml`), không xoá câu thử, không sửa kết quả `eval/run-1.csv` / `eval/run-2.csv`.
2. **Mọi số liệu trên slide & `cost/cost-estimate.md`** phải truy được về file gốc (`evidence/summary.md`, `eval/run-*.csv`, `cost/simulate-*.csv`, `further-reading/model-prices.md`) — số tự ước tính phải ghi rõ `*(tự ước tính)*`.
3. **Không commit `.env` hay API key** lên GitHub (`-10 điểm`).
4. **Xuất `demo-slides.pdf`** đặt ngay tại **thư mục gốc repo** (nộp PDF, không nộp link slide).

---

## Phân công chi tiết 3 thành viên (10:00 – 14:00 Thứ Bảy 28/11)

### 1. Trịnh Thanh Tùng (`2A202603456` · Đội trưởng) — Mô phỏng chi phí & `spec.md` §8
- **File phụ trách:** `cost/personas.yaml` · `cost/simulate-1.csv` · `cost/simulate-1-summary.md` · `cost/cost-estimate.md` · `spec.md` §8
- **Việc cần làm:**
  1. Điền **`cost/personas.yaml`** (xoá mọi chỗ `(ví dụ)`):
     - `sessions: 50`, `seed: 42`
     - `users`: `low`, `base: 700` (lớp L3 hơn 700 học viên theo README khoá), `high: 1000` (cả khoá >1.000 học viên), ghi rõ nguồn.
     - `personas`: ≥ 3 kiểu (`dung_it`, `dung_vua`, `dung_nhieu`), `share` cộng lại = `1.0`, `uses_per_month` & `turns_per_session` lấy từ phỏng vấn `P1–P3` (~1–4 lần/tháng) và `#chung` (hoặc ghi rõ `*(tự ước tính)*`).
     - `prices`: ≥ 2 mức model (model đang chạy `google/gemini-3.5-flash-lite` và 1 model mạnh hơn để so sánh), lấy giá USD / 1M token từ `further-reading/model-prices.md`.
  2. Chạy kiểm khung 10 phiên rồi chạy thật ≥ 50 phiên:
     ```bash
     python run.py simulate --try
     python run.py simulate --rate-from eval/run-2.csv
     ```
     *(Kiểm tra `cost/simulate-1.csv` và `cost/simulate-1-summary.md` được tạo thành công).*
  3. Chép bảng từ `cost/simulate-1-summary.md` sang **`cost/cost-estimate.md`**, tính **chi phí / task thành công**, đối chiếu với Impact/người/tháng ở `spec.md` §2 và viết kết luận 1 dòng (*đáng làm không*).
  4. Điền **`spec.md` §8** (chi phí / task thành công, 3 kịch bản thấp/cơ sở/cao, kết luận so với impact).
- **Xong lúc:** `12:30`.

---

### 2. Trương Hoàng Tùng (`2A202603651`) — Báo cáo & Hồ sơ đánh giá (`eval/`)
- **File phụ trách:** `eval/report.md` · `eval/README.md`
- **Việc cần làm:**
  1. Điền **`eval/report.md`**:
     - **Mục 1 (Kết quả):** Bảng Lượt 1 (`run-1@20261128-032957`, `22/24 = 92%`, `thuong 7/8`, `kho 7/8`, `tu_choi 8/8` — Đạt) và Lượt 2 (`run-2@20261128-033154`, `24/24 = 100%`, `thuong 8/8`, `kho 8/8`, `tu_choi 8/8` — Đạt).
     - **Mục 2 (Lỗi Lượt 1):** Gom nhóm lỗi & ghi chi tiết 2 lỗi thật ở Lượt 1 (`Q03` thiếu link Zoom thao tác dù đã nêu Online + ANN-08; `Q09` chưa hỏi làm rõ bài Lab/Checkpoint cụ thể khi câu hỏi mơ hồ) + ghi chú minh bạch về lỗi kỹ thuật `HTTP 402` ở lần chạy thử trước đó nếu có.
     - **Mục 3 (Một lần cải tiến):** Nêu rõ sửa `SYSTEM` prompt trong `codebase/agent.py` (giữ nguyên link thao tác + bắt buộc hỏi làm rõ câu mơ hồ) → nâng tổng từ `92%` lên `100%`, không làm câu nào tệ đi.
     - **Mục 4 (Còn lại):** Rủi ro còn lại (dữ liệu hiện là `synthetic`, chưa nối webhook Discord thật, tìm kiếm từ khoá đơn giản) & hướng 1 tuần tiếp theo.
  2. Điền **`eval/README.md`** (Hồ sơ đánh giá 1 trang):
     - Tóm tắt dataset (`data/DATA_CARD.md`), 24 câu thử (11/24 nguồn thật), 3 metric (`eval/metric_spec.yaml`), kết quả người thứ hai chấm chéo 5 output (nếu chấm chéo giữa Hoàng Tùng & Hoàng), bảng 2 lượt chạy và tóm tắt lỗi chính.
- **Xong lúc:** `12:30`.

---

### 3. Nguyễn Hoàng (`2A202603447`) — Slide PDF (`demo-slides.pdf`) & *(Bonus)* Người dùng thử
- **File phụ trách:** `slides/outline.md` · `demo-slides.pdf` (ở thư mục gốc repo) · `validation/log.md` *(bonus)*
- **Việc cần làm:**
  1. *(10:00 – 11:15 · Bonus +5 điểm)*: Nhờ **2–3 bạn ngoài nhóm** (học viên lớp L3A/L3B) dùng thử trực tiếp `python run.py` (~5–10 phút/người), giao 2–3 tình huống thật (hỏi đổi phòng, hỏi mâu thuẫn, hỏi ngoài phạm vi), quan sát im lặng và ghi vào **`validation/log.md`** theo đúng 5 nhịp + 4 dòng tổng hợp.
  2. *(11:15 – 13:30 · Bắt buộc)*: Dựng slide **8 trang** theo đúng dàn ý **`slides/outline.md`** (lấy số từ `evidence/summary.md`, `spec.md` §2/§4, `eval/README.md`, `eval/report.md`, `cost/cost-estimate.md`, `validation/log.md`):
     - Trang 1: Người dùng & pain (`7/13` logistics, `42,9%` chờ >15p, trích `P1–P3`).
     - Trang 2: Vì sao chọn A2 (bảng impact & lý do loại A5).
     - Trang 3: Giải pháp (lát cắt 1 câu, sơ đồ, mức tự động & chỗ người duyệt).
     - Trang 4: Demo live (`Q05` hoặc `Q06` + `Q12` tấn công; có video dự phòng).
     - Trang 5: Đánh giá (`24` câu, `92% → 100%`, `2` lỗi đã sửa).
     - Trang 6: Chi phí khi dùng thật (`cost/cost-estimate.md` — lấy số từ Thanh Tùng lúc `12:30`).
     - Trang 7: Kết luận (*Go / Iterate / Stop* kèm số ở trang 1, 5, 6).
     - Trang 8: Nếu có thêm 1 tuần (dẫn từ `eval/report.md` mục 4 & `validation/log.md`).
  3. Xuất PDF thành **`demo-slides.pdf`** ngay tại **thư mục gốc repo** và điền bảng phân công người nói trong `slides/outline.md`.
- **Xong lúc:** `13:30`.

---

## Hợp lực rà soát, tập demo & nộp CP4 (13:30 – 14:30)

1. **13:30 – 14:00 (Kiểm tra chéo & chạy thử máy demo):**
   - Kiểm tra đủ file ở gốc repo: `TEAMS.md`, `README.md`, `canvas.md`, `spec.md` (§0–§10), `evidence/`, `data/DATA_CARD.md`, `codebase/`, `eval/` (`report.md`, `README.md`, `run-1.csv`, `run-2.csv`), `cost/` (`personas.yaml`, `simulate-1.csv`, `cost-estimate.md`), `demo-slides.pdf`, `validation/log.md`.
   - Chạy kiểm tra:
     ```bash
     python run.py check
     python run.py
     ```
     *(Thử 1 câu thật trên máy sẽ mang đi demo).*
   - Tập demo 3–5 phút (mỗi người trong 3 thành viên nói ít nhất 1 phần) và chuẩn bị sẵn trả lời 4 câu hỏi vấn đáp: *Vì sao chọn hình dạng workflow cố định? · Lỗi nguy hiểm nhất là gì? · Chi phí / task thành công tính thế nào? · Phần bạn làm là gì?*
2. **14:00 – 14:15 (Push & Nộp CP4 trước 14:30):**
   - `git status` kiểm tra **không có `.env`**, rồi `git add .`, `git commit -m "CP4: eval report, cost simulation, demo-slides.pdf and validation"`, `git push origin main`.
   - Đội trưởng (`2A202603456`) nộp form CP4 trước **14:30**.

---

## Sau Demo — Hạn chót `23:59 Thứ Bảy 28/11` *(cả 4 người, nhớ nhắc Nam)*
- Mỗi thành viên viết **1 file riêng** trong `reflection/`:
  - `reflection/trinh-thanh-tung.md`
  - `reflection/nguyen-phu-nam.md`
  - `reflection/nguyen-hoang.md`
  - `reflection/truong-hoang-tung.md`
- Hoàn thiện **`docs/ai-usage.md`** rồi commit & push trước `23:59`.
