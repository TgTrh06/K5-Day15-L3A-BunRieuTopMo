# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

Chuẩn "đạt" (`spec.md` §7): ≥ 80% tổng số câu thử qua **và** 100% câu `tu_choi` qua.

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-032957` | 22/24 | 92% | 7/8 | 7/8 | 8/8 | đạt |
| 2 | `run-2@20261128-033154` | 24/24 | 100% | 8/8 | 8/8 | 8/8 | đạt |

Cả hai lượt chạy trên cùng 24 câu thử, cùng model `google/gemini-3.5-flash-lite`, cùng cách chấm (cột `pass` chấm tay theo `pass_criterion`). Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Bỏ sót link thao tác (có nguồn đúng nhưng thiếu link người dùng cần bấm) | 1 | Q03 |
| Không hỏi lại khi câu hỏi mơ hồ (liệt kê mọi hạn thay vì hỏi bài nào) | 1 | Q09 |

**Lỗi cụ thể** — lượt 1 chỉ có **2 câu trượt**, nên chỉ ghi được 2 lỗi (không thêm lỗi không có thật):

| Câu | Input | Output (rút gọn) | Vì sao sai |
|---|---|---|---|
| Q03 (`thuong`) | "Buổi LEC 14 sáng Chủ nhật học ở phòng nào ạ?" | "…buổi LEC 14 sáng Chủ nhật (29/11/2026) của lớp L3A chuyển sang hình thức học Online qua Zoom, không học tại phòng trực tiếp. Nguồn: ANN-08" | `pass_criterion` yêu cầu kèm link Zoom `https://zoom.example/l3a-lec14`. Bot trích đúng ANN-08 nhưng bỏ mất link Zoom có trong thông báo → học viên biết học online nhưng vẫn phải tự đi tìm link. |
| Q09 (`kho`) | "Hạn nộp bài tuần này là khi nào vậy ạ?" | Liệt kê hạn Lab 12 (ANN-01) và hai hạn Lab 14 (ANN-04, ANN-05), rồi đề nghị hỏi TA | `pass_criterion` yêu cầu hỏi lại bài/checkpoint cụ thể. Bot không bịa và không chọn bừa một hạn, nhưng không hỏi làm rõ mà đổ một danh sách dài, dễ khiến học viên đọc nhầm hạn. |

## 3. Một lần cải tiến

- **Nhắm vào nhóm lỗi:** cả hai nhóm ở mục 2 (đều là câu trả lời "có nguồn nhưng chưa dùng được ngay"). **Vì sao đau nhất với người dùng:** pain trong phỏng vấn là mất 10–15 phút lục kênh để tìm đúng thông tin (P1, P3). Câu trả lời thiếu link Zoom (Q03) hoặc liệt kê nhiều hạn (Q09) bắt học viên tìm/đọc tiếp, đúng chỗ đau nhóm muốn gỡ.
- **Đã sửa gì:** chỉ sửa `SYSTEM` prompt trong `codebase/agent.py` (ghi ở `spec.md` §10, 28/11 03:31):
  1. Quy tắc 1 thêm: giữ nguyên mọi link thao tác (link Zoom, form, LMS) có trong nội dung thông báo.
  2. Tách quy tắc "câu hỏi mơ hồ" thành quy tắc riêng (quy tắc 4): bắt buộc hỏi lại học viên muốn tra Lab/Checkpoint nào, có thể gợi ý, không chọn bừa một hạn.
  Không đổi công cụ, dữ liệu, model hay câu thử.
- **Kết quả:** nhóm lỗi đó 0/2 → 2/2 (Q03 có link Zoom kèm ANN-08; Q09 hỏi lại "Lab hay Checkpoint cụ thể nào") · tổng 92% → 100%.
- **Câu nào tệ đi sau khi sửa:** không có — 22 câu đạt ở lượt 1 vẫn đạt ở lượt 2. Chi phí phụ: prompt dài hơn nên token vào tăng khoảng 100 token mỗi câu (vd Q01: 893 → 990).

## 4. Còn lại

- **Lỗi chưa sửa + nguy hiểm thế nào:**
  - Lượt 2 đạt 100% trên **chính bộ câu đã dùng để sửa prompt**, nên con số này có thể lạc quan hơn thực tế; câu hỏi lạ (cách hỏi khác, viết tắt, không dấu) chưa được đo.
  - Dữ liệu thông báo là `synthetic` (20 mục tự soạn); chưa nối Discord thật nên chưa biết bot xử lý thế nào với hàng trăm tin, tin sửa trong thread thật, hay ảnh chụp thông báo.
  - Tìm kiếm thông báo còn đơn giản (theo từ khoá): nếu học viên hỏi bằng từ khác với thông báo, bot có thể không tìm thấy và trả lời "không có thông báo" dù thông báo có tồn tại — học viên vẫn phải hỏi TA.
- **Nếu có thêm 1 tuần:**
  1. Thêm 10–15 câu thử mới viết theo cách học viên thật hỏi (viết tắt, không dấu, hỏi nối tiếp) mà prompt chưa từng thấy, chạy lại để đo đúng hơn.
  2. Nối đọc kênh thông báo Discord thật (chỉ đọc, có người duyệt) và thử với một tuần thông báo thật đã ẩn danh.
  3. Cải thiện bước tìm kiếm (khớp từ đồng nghĩa: "phòng"/"room", "hạn"/"deadline") và đo số câu bị trả lời "không có" nhầm.
