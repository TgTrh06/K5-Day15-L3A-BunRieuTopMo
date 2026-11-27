# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Lịch học & phân công vận hành (`data/training-ops/`)

| | |
|---|---|
| Dùng để làm gì | Nguồn lịch học, phòng học giả lập cho công cụ tra cứu lịch và bộ câu thử |
| Từ đâu | Data BTC cấp (`data/training-ops/` trong repo đề, giả lập Khoá 9) |
| Xử lý những bước gì | Chỉ trích xuất thông tin buổi học, phòng học của lớp L3A/L3B; giữ nguyên ẩn danh (`Lecturer A`, `Lab Coach A`...) |
| Số dòng / số đoạn | 111 buổi học trong 21 ngày (chi tiết phần trích cho chạy thử: __ dòng) |
| Phiên bản / ngày lấy | 2026-11-27 (theo repo đề) |
| Nhãn | `synthetic` (giả lập do BTC cấp) |
| Giới hạn | Lịch và ngày đều giả (Khoá 9, 04–05/2027), không phản ánh nội dung thông báo tự do trên Discord |

**Data `synthetic` (nhóm tự sinh):** ghi cách sinh (prompt / script), seed, người kiểm, số dòng đã kiểm tay. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Kho thông báo & thread hỏi đáp Discord giả lập (`data/announcements_sample.*`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `search_announcements` / `get_thread` và bộ câu thử `eval/benchmark.csv` |
| Từ đâu | Nhóm tự viết dựa trên cấu trúc thông báo thường gặp (hạn nộp, đổi phòng, thread giải đáp) |
| Xử lý những bước gì | Tự soạn, gắn nhãn `id`, `channel`, `timestamp`, `status` (còn hiệu lực / đã thay thế), không dùng tin nhắn thật |
| Số dòng / số đoạn | __ thông báo + __ thread (mục tiêu ≥ 10–15 mục cho CP2) |
| Phiên bản / ngày lấy | 2026-11-27 |
| Nhãn | `synthetic` |
| Giới hạn | Do nhóm tự dựng để mô phỏng tình huống khó (2 thông báo lệch hạn, tin đã cũ), không dùng làm bằng chứng pain |
