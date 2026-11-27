# Phân công công việc & Chỉ dẫn Checkpoint 2 (CP2) — Nhóm BunRieuTopMo

> **Track A · A2 (Trợ lý Discord)**  
> **Hạn nộp CP2:** `19:30 Thứ Sáu 27/11/2026` *(4 điểm)*  
> **Mục tiêu CP2:** Có bằng chứng pain đầu tiên · chốt kiến trúc `spec.md` §4 & chuẩn "đạt" `spec.md` §7 · có `eval/benchmark.csv` (≥ 10 câu), `eval/metric_spec.yaml` (≥ 3 metric), `data/DATA_CARD.md` bản đầu · chạy được `python run.py` với AI giả.

---

## Nguyên tắc bắt buộc (tránh bị trừ điểm)

1. **Không commit dữ liệu cá nhân thật / dump chat Discord** (`-10 điểm` nếu vi phạm). Khi trích dẫn từ Discord: **tối đa 2 câu**, **xoá tên/username/ID**, không đoán tin nhắn của ai.
2. **Không bịa số liệu, trích dẫn hay người phỏng vấn.** Kết quả thực tế thế nào ghi đúng như vậy.
3. **Chuẩn "đạt" ở `spec.md` §7 chốt tại CP2 (19:30)** — sau CP2 **không được sửa** chuẩn đạt, không xoá câu thử bị trượt.
4. **Dữ liệu tự dựng (`synthetic`) không phải bằng chứng pain** — chỉ dùng để chạy thử và làm test case.

---

## Phân công 3 thành viên (15:30 – 17:45)

### 1. Nguyễn Phú Nam (`2A202603501`) — Đào & đếm bằng chứng Discord
- **File phụ trách:** `evidence/data-mining.md` *(Mục 1 đã điền sẵn cách đếm và mẫu số)*
- **Việc cần làm:**
  1. Chọn 2–3 kênh công khai hay hỏi đáp/thông báo của lớp L3A trong 7 ngày gần nhất (ghi rõ tên kênh và khoảng ngày vào Mục 1).
  2. Đọc lướt và phân loại các kiểu câu hỏi vào **Mục 2**.
  3. **Đếm có mẫu số `N`** (tổng số câu hỏi của học viên, bỏ chat phiếm và bot) và điền vào **Mục 3** dạng `x/N (y%)`:
     - Số câu hỏi về logistics (hạn nộp, lịch học, phòng học, link tài liệu).
     - Số câu hỏi lặp lại ý đã có trong thông báo.
     - *(Nếu đếm được)* Số câu trả lời chậm / bị trôi.
  4. Ghi **≥ 5 ví dụ cụ thể** vào **Mục 4** *(mỗi ví dụ ≤ 2 câu, đã xoá tên/username)*.
  5. Ghi ngắn gọn giới hạn của data vào **Mục 5**.
- **Xong lúc:** `17:30` — push lên repo hoặc gửi tóm tắt số liệu cho Đội trưởng.

---

### 2. Nguyễn Hoàng (`2A202603447`) — Phỏng vấn người dùng thật
- **File phụ trách:** `evidence/interviews/P1.md`, `P2.md`, `P3.md`... *(tạo từ `evidence/interviews/TEMPLATE.md`)*
- **Việc cần làm:**
  1. Phỏng vấn nhanh **≥ 3 người ngoài nhóm**: ưu tiên **2–3 học viên lớp L3A** (người hay tra lịch/hạn nộp trên Discord) và **1 TA hoặc lab coach** (người hay trả lời câu lặp).
  2. Mỗi cuộc 5–10 phút, hỏi theo sự thật quá khứ (không hỏi dẫn dắt kiểu *"bạn có muốn dùng AI không"*):
     - *"Lần gần nhất bạn phải tìm lại hạn nộp / phòng học trên Discord là khi nào?"*
     - *"Bạn tìm mất bao lâu, gặp khó ở đâu?"*
     - *"Đã từng nhầm hạn nộp hoặc đi nhầm phòng chưa? Hậu quả thế nào?"*
  3. Ghi lại thành từng file `P1.md`, `P2.md`, `P3.md` (ẩn danh tên người trả lời), giữ lại **1–2 trích dẫn nguyên văn** đắt giá.
  4. Tóm tắt **số đầu tiên + 1 trích dẫn** để cập nhật dòng 4 của `canvas.md`.
- **Xong lúc:** `17:45`.

---

### 3. Trương Hoàng Tùng (`2A202603651`) — Dữ liệu giả lập & Bộ câu thử đầu
- **File phụ trách:**
  - Kho dữ liệu mẫu trong `data/` (ví dụ `data/announcements_sample.json` hoặc `.md`)
  - `data/DATA_CARD.md` *(đã tạo sẵn khung Dataset 1 & 2)*
  - `eval/benchmark.csv`
- **Việc cần làm:**
  1. Tham khảo cấu trúc lịch/phòng trong `data/training-ops/` để tạo bộ **10–15 thông báo & thread Discord giả lập** (gắn nhãn `synthetic`), gồm đủ các tình huống:
     - Thông báo hạn nộp lab có link chính thức.
     - Thông báo đổi phòng học (có bản cũ bị thay thế bởi bản mới).
     - Thread đã có TA giải đáp.
     - Câu hỏi nằm ngoài thông báo (không có nguồn).
  2. Điền đầy đủ số dòng/số đoạn thực tế vào `data/DATA_CARD.md`.
  3. Soạn **≥ 10 câu thử đầu** trong `eval/benchmark.csv` (**xoá 3 dòng mẫu `B01, B02, B03`**), đủ 3 loại:
     - `thuong`: hỏi hạn nộp, phòng học có sẵn trong thông báo.
     - `kho`: 2 thông báo lệch hạn, thông báo cũ bị ghi đè, thông tin nằm ở thread khác.
     - `tu_choi`: hỏi điểm/điểm danh cá nhân, hỏi thứ không có trong thông báo, prompt injection (`"bỏ qua hướng dẫn cũ..."`).
- **Xong lúc:** `17:45`.

---

## Hợp lực chốt CP2 (17:45 – 19:00 · Trịnh Thanh Tùng điều phối)

1. **17:45 – 18:05 (Họp 20 phút cả nhóm):**
   - Nam & Hoàng báo cáo số liệu pain đầu tiên → cập nhật dòng 4 và dòng *"Đã đổi gì so với CP1"* trong `canvas.md`.
   - Cả nhóm thống nhất luồng xử lý & các trường hợp phải từ chối/escalate TA.
2. **18:05 – 19:00 (Hoàn thiện kỹ thuật & kiểm tra):**
   - **Trịnh Thanh Tùng (`2A202603456`):**
     - Hoàn thiện `spec.md` §4 (sơ đồ kiến trúc giải pháp) và **chốt §7 (chuẩn "đạt" bằng số)**.
     - Điền `eval/metric_spec.yaml` (**≥ 3 metric** đủ `name`, `definition`, `grader`, `threshold`).
     - Viết khung `codebase/` (`agent.py`, `tools.py`, `ai.py`) sao cho `python run.py` chạy hết luồng với AI giả + đọc được dữ liệu giả lập trong `data/`.
   - **Chạy kiểm tra bắt buộc:**
     ```bash
     python run.py check
     python run.py
     ```
     *(Đảm bảo `run.py check` không báo lỗi `TEAMS.md`, `eval/metric_spec.yaml` đủ ≥ 3 metric, `eval/benchmark.csv` đủ ≥ 10 câu và đã xoá dòng mẫu `B01–B03`.)*
   - *(Khuyến khích trước khi rời lớp)*: 1 người tạo `.env` từ `.env.example` và gọi thử 1 câu với API model thật để sáng hôm sau không bị kẹt.
3. **19:00 – 19:30:** `git add`, `git commit`, `git push` lên GitHub và Đội trưởng nộp link CP2.
