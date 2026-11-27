# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Repo chỉ chứa số đã tổng hợp và các ví dụ ngắn đã ẩn danh — không commit file dump chat Discord hay thông tin cá nhân thật.

## 1. Cách đếm — quy ước áp dụng

- **Data dùng:** Tin nhắn trên kênh công khai `#chung` của cộng đồng lớp L3 trên Discord, khoảng ngày **20/11/2026 – 26/11/2026** (7 ngày gần nhất trước Hackathon).
- **Đếm gì:**
  - `x1`: Số câu hỏi về **logistics** (phòng học, đổi phòng, thời khoá biểu/lịch học, thông tin sự kiện Hackathon, nơi nộp thông tin nhóm).
  - `x2`: Số câu hỏi **lặp lại** thông tin đã từng được thông báo trước đó (trên kênh hoặc qua email chính thức).
  - `x3`: Số câu hỏi **học vụ cá nhân / quy định** (điểm danh, nghỉ học, trợ cấp, giấy cam kết) — để kiểm chứng phạm vi cần từ chối / chuyển TA.
  - `x4`: Số câu hỏi logistics phải **chờ lâu (>15 phút) hoặc bị trôi không có người trả lời** trên kênh.
- **Lọc bỏ:** Tin nhắn của Lab Coach/BTC, tin chấm `.`, chào `Hi`, `+1`, trả lời ngắn (`yes`, `oke`, `cảm ơn`, `ib`), 1 tin quảng bá vote sản phẩm và 16 tin rao tìm/ghép nhóm Hackathon (không phải câu hỏi tra cứu thông tin).
- **Mẫu số là gì:** **`N = 13`** — tổng số câu hỏi thật của học viên trên kênh `#chung` trong 7 ngày `20/11 – 26/11/2026` sau khi lọc bỏ các tin không phải câu hỏi.
- **Cách đếm lại:** Đọc lần lượt toàn bộ tin nhắn trên `#chung` từ `19:01 20/11/2026` đến `23:58 26/11/2026`, tách tin nhắn của học viên có mục đích hỏi thông tin (`N = 13`), gắn nhãn từng câu vào 3 nhóm loại trừ nhau (`logistics`, `học vụ cá nhân / quy định`, `khác`) và đếm chéo số câu lặp + thời gian chờ phản hồi.

## 2. Đọc trước, đếm sau

Đã đọc toàn bộ tin nhắn trên kênh `#chung` trong 7 ngày `20/11 – 26/11/2026` (61 lượt nhắn của học viên, lọc ra `N = 13` câu hỏi thật). Các *kiểu* câu hỏi thấy được:
- **Hỏi phòng học & đổi phòng sát giờ:** hỏi vị trí phòng, hỏi phòng thay thế khi phòng cũ bị chiếm (kèm nhiều bạn bấm `+1`), và hỏi lại dù đã có thông báo đổi phòng ngay phía trên.
- **Hỏi lịch học / TKB / thông tin Hackathon & nơi nộp:** hỏi TKB tuần sau, thể lệ Hackathon, khi nào có thông tin, nộp thông tin thành viên ở đâu.
- **Hỏi học vụ cá nhân & quy định:** nghỉ workshop có ảnh hưởng trợ cấp không, xin nghỉ đi khám nghĩa vụ quân sự, điểm danh khi làm lab online, cách ký điện tử giấy cam kết.
- **Khác:** tìm đồ để quên ở phòng học (sạc laptop).

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Câu hỏi về **logistics** (phòng học, đổi phòng, TKB, thông tin & nộp nhóm Hackathon) | **7 / 13** | **53,8%** | Chiếm hơn một nửa tổng số câu hỏi trên kênh chung |
| Câu hỏi **học vụ cá nhân / quy định** (điểm danh, xin nghỉ, trợ cấp, thủ tục) | **5 / 13** | **38,5%** | Xác nhận cần luồng từ chối & chỉ đường sang email BTC / TA |
| Câu hỏi **khác** (tìm đồ thất lạc) | **1 / 13** | **7,7%** | Hỏi quên sạc laptop ở phòng H209 |
| Câu hỏi **lặp lại** thông tin đã có trên kênh / email | **2 / 13** | **15,4%** | Chiếm **2/7 (28,6%)** nhóm logistics: hỏi lại phòng C303 sau 53 phút đã thông báo đổi sang C204; hỏi lại thông tin Hackathon đã gửi qua Outlook |
| Câu hỏi logistics **chờ >15 phút hoặc không có phản hồi** | **3 / 7** *(trên nhóm logistics)* | **42,9%** | Hỏi đổi phòng C303 chờ 23 phút (thêm 3 bạn `+1`); hỏi thể lệ Hackathon chờ 76 phút; hỏi TKB tuần sau bị trôi không ai trả lời |

## 4. ≥5 ví dụ cụ thể *(trích ≤2 câu mỗi ví dụ, đã bỏ tên/username/mã học viên)*

1. *"Cho e hỏi là phòng C303 đang khám sức khỏe thì lab 3b sáng nay hc ở đâu ạ"* — `#chung`, 21/11/2026 *(thêm 3 học viên nhắn `+1`; 23 phút sau mới có Lab Coach báo chuyển sang C204)*.
2. *"em 303 nãy tìm không thấy lớp e qua 301 được khong ạ"* — `#chung`, 21/11/2026 *(hỏi lại sau 53 phút kể từ khi đã có tin báo chuyển sang phòng C204 ngay trên cùng kênh)*.
3. *"cac anh oi, co TKB cho tuan sau chua a?"* — `#chung`, 22/11/2026 *(không có phản hồi trên kênh)*.
4. *"anh/chị cho em hỏi là bao giờ sẽ có thông tin về buổi hackathon vậy ạ?"* — `#chung`, 26/11/2026 *(Lab Coach phải nhắc kiểm tra mail Outlook; trùng khớp insight P2)*.
5. *"Nộp ttin tvien ở đâu v ạ"* — `#chung`, 26/11/2026 *(hỏi nơi nộp thông tin nhóm ngay sau thông báo lập team Hackathon)*.
6. *"mng cho em hỏi em không vào 1 buổi workshop thì có bị tính là 1 buổi nghỉ hay ảnh hưởng gì đến việc nhận trợ cấp không ạ"* — `#chung`, 20/11/2026 *(ví dụ câu hỏi học vụ cá nhân nằm ngoài phạm vi trả lời tự động)*.

## 5. Giới hạn của data

- Chỉ mới đếm trên **1 kênh công khai (`#chung`)** trong 7 ngày (`20/11 – 26/11/2026`), chưa bao gồm các kênh riêng của từng lớp (`#l3a-lab`, `#l3b-lab`), các thread con hoặc tin nhắn hỏi riêng qua Zalo/DM.
- Mẫu số còn nhỏ (`N = 13` câu hỏi thật sau khi lọc 16 tin tìm nhóm và chat phiếm) và data chỉ cho thấy học viên **hỏi gì, chờ bao lâu**, chưa giải thích hết **vì sao** họ bỏ sót thông báo trước đó.
- → Đã kiểm chéo trực tiếp bằng 3 cuộc phỏng vấn học viên thật (`evidence/interviews/P1.md`, `P2.md`, `P3.md`): cả 2 nguồn khớp nhau rất rõ ở pain **đổi phòng sát giờ** (P1 & ca phòng C303 → C204) và **thông tin Hackathon gửi qua email không có trên Discord** (P2 & câu hỏi ngày 26/11).
