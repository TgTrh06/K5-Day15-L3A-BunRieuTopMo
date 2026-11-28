# Tóm tắt mô phỏng simulate-1@20261128-044701

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 13 | 1 | 1001 | 116 | 1.0 | 1.0 |
| dung_vua | 14 | 1 | 1012 | 129 | 1.0 | 1.0 |
| dung_nhieu | 4 | 2 | 2017 | 250 | 2.0 | 2.0 |

Tỉ lệ đạt dùng để tính: 24/24 (100%) — lượt run-2@20261128-033154

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (436 người) | Chi phí / tháng — cao (721 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00069 (≈ 18 ₫) | $0.00069 (≈ 18 ₫) | $0.00061 (≈ 16 ₫) | $0.6271 (≈ 15.929 ₫) | $0.9115 (≈ 23.151 ₫) | $1.51 (≈ 38.284 ₫) | $0.0021 (≈ 53 ₫) |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0037 (≈ 93 ₫) | $0.0037 (≈ 93 ₫) | $0.0032 (≈ 82 ₫) | $3.33 (≈ 84.616 ₫) | $4.84 (≈ 122.975 ₫) | $8.01 (≈ 203.361 ₫) | $0.0111 (≈ 282 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.1) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: google/gemini-3.5-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 19/50.
- Tỷ giá: 1 USD = 25.400 ₫ (tỉ giá tham khảo (tự ước tính)).
