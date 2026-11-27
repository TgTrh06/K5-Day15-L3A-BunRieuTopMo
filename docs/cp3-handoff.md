# Phân công công việc & Chỉ dẫn Checkpoint 3 (CP3) — Nhóm BunRieuTopMo

> **Track A · A2 (Trợ lý Discord)**  
> **Hạn nộp CP3:** `10:00 Thứ Bảy 28/11/2026` *(Sáng Thứ Bảy không có lớp, nhóm tự làm)*  
> **Mục tiêu CP3:** Nối model thật · bộ câu thử **20–30 câu** (≥1/3 từ `nguoi_dung` / `data_that`) · hoàn thiện `evidence/summary.md` và `spec.md` §0–§7 · chạy `eval` lượt 1 (`eval/run-1.csv` + `score`) · quay **video 30 giây** bản chạy thử gọi AI thật.

---

## Luật cứng sau CP2 (tuyệt đối không vi phạm)

1. **Không sửa chuẩn "đạt"** ở `spec.md` §7 và `eval/metric_spec.yaml`.
2. **Không xoá câu thử trượt**, không sửa `expected` cho khớp output của model.
3. **Không commit `.env` hoặc API key** lên GitHub (`-10 điểm` ngay lập tức).
4. **Không bịa số liệu** — số tự ước tính (ví dụ số lần/tháng ở bảng Impact) phải ghi rõ `*(tự ước tính)*`.
5. **Mọi thay đổi thiết kế sau CP2** phải ghi vào `spec.md` §10 (bảng Changelog `CP2 → CP4`).

---

## Phân công 4 thành viên (Tối Thứ Sáu 27/11 → 09:30 Thứ Bảy 28/11)

### 1. Trịnh Thanh Tùng (`2A202603456` · Đội trưởng) — Nối model thật & chạy Eval lượt 1
- **File phụ trách:** `.env` *(chỉ giữ ở máy, không commit)* · `codebase/ai.py` · `codebase/agent.py` · `codebase/tools.py` · `README.md` (điền tên Model thật)
- **Việc cần làm:**
  1. Tạo `.env` từ `.env.example`, điền API key của nhóm và cấu hình `codebase/ai.py` theo `docs/connect-model.md`.
  2. Tinh chỉnh `SYSTEM` prompt và logic tra cứu trong `codebase/tools.py` / `codebase/agent.py` (đảm bảo trích mã `ANN-xx`/`THR-xx` + link, bỏ qua tin `superseded`, chuyển TA khi thiếu/mâu thuẫn/tấn công).
  3. Chạy thử `python run.py` và `python run.py eval --try` thấy `tokens_in > 0`, `tokens_out > 0`.
  4. Khi Hoàng Tùng chốt xong 20–30 câu ở `eval/benchmark.csv`, chạy trọn bộ:
     ```bash
     python run.py eval
     ```
     → sinh `eval/run-1.csv` và `traces/run-1.jsonl` (dùng `--wait 4` nếu API giới hạn lượt/phút).
- **Xong nối model:** `tối 27/11` (nên xong trước khi ngủ) · **Xong chạy `run-1.csv`:** `08:45 sáng 28/11`.

---

### 2. Trương Hoàng Tùng (`2A202603651`) — Mở rộng bộ câu thử (20–30 câu) & DATA_CARD
- **File phụ trách:** `eval/benchmark.csv` · `data/announcements_sample.json` · `data/DATA_CARD.md`
- **Việc cần làm:**
  1. Mở rộng `eval/benchmark.csv` từ **12 câu lên 22–25 câu** *(trong ngưỡng 20–30 câu)*, vẫn giữ nguyên 12 câu cũ `Q01–Q12`.
  2. **Bắt buộc đạt tỉ lệ nguồn thật (`≥ 1/3` tổng số câu):** lấy trực tiếp **8–10 câu** từ lời người dùng trong `evidence/interviews/P1–P3.md` và câu hỏi thật trên `#chung` trong `evidence/data-mining.md` (gắn cột `source` bắt đầu bằng `nguoi_dung:` hoặc `data_that:`).
     - Ví dụ: hỏi đổi giờ mentor duty nằm trong thread (P1), hỏi thông tin hackathon không có trên Discord (P2), hỏi workshop lùi giờ (P3), hỏi phòng C303 bị chiếm sang C204 (`#chung`), hỏi TKB tuần sau bị trôi (`#chung`), hỏi nghỉ workshop có mất trợ cấp (`#chung`)...
  3. Bổ sung thông báo/thread giả lập tương ứng vào `data/announcements_sample.json` nếu cần, và cập nhật số lượng thực tế vào `data/DATA_CARD.md`.
  4. Chạy `python run.py check` xác nhận **0 cảnh báo** ở `benchmark.csv` và `metric_spec.yaml`.
- **Xong lúc:** `08:30 sáng 28/11` để Đội trưởng chạy `python run.py eval`.

---

### 3. Nguyễn Phú Nam (`2A202603501`) — Tổng hợp bằng chứng & Impact (`evidence/summary.md`, `spec.md` §0–§3)
- **File phụ trách:** `evidence/summary.md` · `spec.md` (§0, §1, §2, §3)
- **Việc cần làm:**
  1. Tổng hợp số liệu từ `evidence/data-mining.md` (`N=13`) và `P1–P3.md` vào **`evidence/summary.md`** (đối chiếu với giả thuyết ban đầu ở `evidence/hypothesis.md`, ghi rõ cả điểm khớp và điểm ngược giả định từ P2).
  2. Điền **`spec.md` §0–§3**:
     - **§0:** Luồng tra cứu hiện tại trên Discord (3–5 bước, bot đang có nếu quan sát được).
     - **§1:** Tóm tắt người dùng, pain và số liệu bằng chứng chính từ `evidence/summary.md`.
     - **§2:** Bảng **Impact / tháng** (`số người gặp × số lần/tháng × số phút tốn`), ghi rõ nguồn từng thừa số (hoặc `*(tự ước tính)*`), và hướng đã loại (ví dụ A5) kèm lý do.
     - **§3:** 1–2 giải pháp tương tự (ví dụ FAQ bot Discord thông thường / tìm kiếm mặc định của Discord) và điểm khác biệt của nhóm.
- **Xong lúc:** `09:00 sáng 28/11`.

---

### 4. Nguyễn Hoàng (`2A202603447`) — Hoàn thiện `spec.md` §5–§6, chấm `run-1` & quay video 30s
- **File phụ trách:** `spec.md` (§5, §6, §9) · `eval/run-1.csv` (điền cột `pass`) · Video demo 30s
- **Việc cần làm:**
  1. Điền **`spec.md` §5** (4 lớp chỗ khó, ≥ 6 kịch bản + 2 tấn công khớp với `eval/benchmark.csv`), **§6** (4 đường đi trải nghiệm) và **§9** (rủi ro & an toàn).
  2. Ngay sau khi có `eval/run-1.csv` (`08:45`): đọc từng output, chấm cột `pass` (`1`/`0`) và `ghi_chu` theo đúng `eval/metric_spec.yaml`, rồi chạy:
     ```bash
     python run.py score eval/run-1.csv
     ```
     Cập nhật kết quả lượt 1 vào `spec.md` §7 (dòng `Kết quả: lượt 1 __/__ (__%)`).
  3. Quay **video 30 giây** thao tác thật trên `python run.py` với AI thật (upload YouTube *Không công khai* hoặc Google Drive *Bất kỳ ai có đường liên kết*, thử mở bằng cửa sổ ẩn danh và dán link vào `README.md`).
- **Xong lúc:** `09:30 sáng 28/11`.

---

## Tự soát trước khi nộp CP3 (09:30 – 10:00 sáng Thứ Bảy 28/11)

- [ ] `python run.py check` → **0 cảnh báo** (đủ 20–30 câu, ≥ 1/3 từ `nguoi_dung`/`data_that`, ≥ 5 `kho`, ≥ 2 `tu_choi`, 3 metric).
- [ ] `evidence/summary.md` hoàn chỉnh + `spec.md` điền đủ **§0–§7**.
- [ ] `eval/run-1.csv` đã chấm cột `pass` và chạy `python run.py score eval/run-1.csv`.
- [ ] Video 30s chạy AI thật mở được ở cửa sổ ẩn danh.
- [ ] `git status` không có `.env` hay API key → `git add`, `git commit`, `git push origin main` → Đội trưởng nộp link CP3 trước **10:00**.
