# Chi phí khi dùng thật

> Track A · A2 (Trợ lý Discord). Mọi số liệu truy từ `cost/simulate-1.csv`, `cost/simulate-1-summary.md`, `eval/run-2.csv` và `further-reading/model-prices.md`.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu (`dung_it` 40% · 1,5 lần/tháng · 1 lượt; `dung_vua` 40% · 3 lần/tháng · 1 lượt; `dung_nhieu` 20% · 4 lần/tháng · 2 lượt). Nguồn: phỏng vấn `P1–P3` (`evidence/interviews/`).
- **Số người dùng thật** 3 kịch bản: thấp `300` *(tự ước tính)* · cơ sở `436` *(số học viên L3–L4 hoạt động thực tế)* · cao `721` *(tổng tài khoản L3–L4)*. Nguồn: `data/preclass/README.md`.
- **Giá** 2 mức model (từ `further-reading/model-prices.md`, xem ngày `25/11/2026`):
  - `gemini-3.5-flash-lite` (tầng Nhỏ): vào `$0.30` / 1M · ra `$2.50` / 1M.
  - `gpt-6.2-sol` (tầng Lớn): vào `$2.00` / 1M · ra `$10.00` / 1M.
- **Tỉ lệ đạt** dùng để tính: `24/24 (100%)` — lượt `run-2@20261128-033154` (`eval/run-2.csv`).
- **Đo token:** đo thật trên model `google/gemini-3.5-flash-lite`, tính giá quy đổi cho `gemini-3.5-flash-lite` và `gpt-6.2-sol` *(nếu chạy thật trên `gpt-6.2-sol`, số token có thể lệch nhẹ do khác bộ tách token)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-044701` · `50` phiên (`31` phiên thành công, `19` phiên lỗi hết số dư API từ `S032` đã được khung loại khỏi trung bình) · `seed 42`.

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (300) | / tháng — cơ sở (436) | / tháng — cao (721) | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| `gemini-3.5-flash-lite` (vào 0.3 · ra 2.5 $/1M) | `$0.00069` (≈ 18 ₫) | `$0.00069` (≈ 18 ₫) | `$0.6271` (≈ 15.929 ₫) | `$0.9115` (≈ 23.151 ₫) | `$1.51` (≈ 38.284 ₫) | `$0.0021` (≈ 53 ₫) |
| `gpt-6.2-sol` (vào 2.0 · ra 10.0 $/1M) | `$0.0037` (≈ 93 ₫) | `$0.0037` (≈ 93 ₫) | `$3.33` (≈ 84.616 ₫) | `$4.84` (≈ 122.975 ₫) | `$8.01` (≈ 203.361 ₫) | `$0.0111` (≈ 282 ₫) |

*Tỉ giá tham khảo: `1 USD = 25.400 ₫` (tự ước tính).*

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):** `2,7 lần/tháng × 13 phút/lần ≈ 35 phút/người/tháng` (tổng toàn lớp cơ sở 436 người ≈ `255 giờ/tháng`, chưa tính 23–76 phút chờ trên `#chung`).
- **Chi phí / người / tháng (cơ sở, model `gemini-3.5-flash-lite`):** `$0.0021` (≈ **53 ₫/người/tháng**; cả lớp 436 người chỉ tốn **$0.91/tháng ≈ 23.151 ₫**).
- **Kết luận một dòng — đáng làm không:** **Rất đáng làm** — chỉ tốn ~**53 ₫/người/tháng** (chưa tới 1 USD/tháng cho cả 436 học viên) để tiết kiệm ~35 phút tìm kiếm/người/tháng và giảm hẳn việc nhầm phòng/trễ hạn.
