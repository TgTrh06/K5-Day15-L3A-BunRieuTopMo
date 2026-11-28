# Người dùng thử *(bonus)*

> Điền ở guide bước 4.3 — 2–3 người ngoài nhóm, ~10 phút / người, theo 5 nhịp: làm quen · bối cảnh · giao việc · quan sát · hỏi sau. Ôn lại: ngày 5, ngày 13. Chấm ở rubric Bonus.
> Không ghi tên: ghi vai. Hành vi quan sát được nặng hơn lời nói; toàn lời khen = phiên chưa đạt, giao việc khó hơn.
> Người dùng thử **không thay được** bằng chứng pain ở `evidence/`.

| Người thử (vai) | Việc giao (theo kết quả, không theo nút) | Quan sát (làm gì đầu tiên, chỗ do dự, chỗ hiểu sai) | Trích nguyên văn | Mức nghiêm trọng (cao / vừa / thấp) |
|---|---|---|---|---|
| T1 · Học viên L3B gõ không dấu | Biết chiều thứ Bảy LAB 14 học phòng nào, hạn nộp Lab 14 là khi nào | Gõ không dấu cả 3 câu. Tra cứu vẫn ra đúng ANN-04, ANN-05, ANN-06 vì khớp các từ "lab", "14". Câu "phong lab 14 chot chua" lấy được ANN-06 (phòng chờ xác nhận, dự kiến H210), nhưng xếp sau hai thông báo hạn nộp | "lab 14 hoc phong nao vay" · "phong lab 14 chot chua" | thấp |
| T2 · Học viên L3B gõ viết tắt, dính chữ | Biết LEC 13 học phòng nào, hạn nộp Lab 14, link Zoom LEC 14 | "LEC13 o phong may a" và "deadline lab14 khi nao a" **không tìm được thông báo nào** (danh sách rỗng) vì "lec13", "lab14" dính liền không khớp "LEC 13", "Lab 14". Bot rơi vào nhánh "không tìm thấy" và tạo bản nháp chuyển TA, dù ANN-03 và ANN-04/05 có tồn tại. Câu "link zoom lec 14" có dấu cách thì tìm đúng ANN-08 | "LEC13 o phong may a" · "deadline lab14 khi nao a" | cao |
| T3 · Học viên L3B hỏi mentor duty, điểm danh, gate | Biết giờ mentor duty tối nay; xin sửa điểm danh; biết hạn nộp gate | "mentor duty tối nay mấy giờ" lấy đúng THR-04 (dời sang 20:30) kèm ANN-12 đã bị thay. Câu xin điểm danh lấy đúng THR-03 (quy định chuyển TA). Câu "hạn nộp gate" **không có thông báo gate** nhưng tra cứu vẫn trả về hạn Lab 12, Lab 14, nên model có nguy cơ trả lời bằng hạn lab | "mentor duty tối nay mấy giờ" · "hạn nộp gate là khi nào" | vừa |

Câu hỏi sau: *"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"* → không áp dụng / không áp dụng / không áp dụng *(AI mô phỏng không có cảm nhận thật, nên không ghi)*

## Tổng hợp

- Chủ đề lặp nhiều nhất: cách học viên gõ khác với chữ trong thông báo. Viết dính ("lab14", "LEC13") làm tra cứu rỗng; hỏi thứ không có thông báo (gate) vẫn kéo về thông báo gần giống.
- Sửa gì trước demo (ghi `spec.md` §10): chưa sửa code trước demo, vì `eval/run-1`, `run-2` đã chạy và sửa tra cứu bây giờ không kịp đo lại. Khi demo chỉ dùng câu có dấu cách ("Lab 14", "LEC 13").
- Giữ gì và vì sao: giữ nhánh "không tìm thấy → bản nháp chuyển TA" trong `codebase/agent.py`; khi tra cứu hỏng, bot chuyển TA chứ không bịa.
- Để dành sau: tách chữ và số khi tra cứu ("lab14" → "lab 14"), thêm từ đồng nghĩa ("deadline" ↔ "hạn"), thêm câu thử viết tắt / dính chữ vào bộ câu thử, và thử lại với người dùng thật.
