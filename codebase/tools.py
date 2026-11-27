"""Công cụ của bài toán — Trợ lý Discord tra cứu lịch & hạn nộp (Track A · A2).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không.
"""
import json
import os
import re
from tracing import tool, TOOLS  # noqa: F401

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "announcements_sample.json",
)


def _load_items() -> list:
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("items", [])


@tool
def search_announcements(query: str) -> list:
    """Tra cứu thông báo và thread hỏi đáp chính thức giả lập trong data/announcements_sample.json.
    Input: câu hỏi hoặc từ khoá (str). Output: danh sách các mục liên quan (id, status, timestamp, title, content, link). Không tác động ra ngoài."""
    items = _load_items()
    tokens = [t for t in re.findall(r"\w+", query.lower()) if len(t) >= 2]
    scored = []
    for item in items:
        haystack = " ".join([
            str(item.get("id", "")),
            str(item.get("title", "")),
            str(item.get("content", "")),
            str(item.get("channel", "")),
        ]).lower()
        score = sum(1 for tok in tokens if tok in haystack)
        if score > 0:
            scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scored[:5]]


@tool
def get_thread(item_id: str) -> dict:
    """Lấy chi tiết một thông báo hoặc thread theo mã định danh (ANN-xx / THR-xx).
    Input: mã thông báo/thread (str). Output: dict thông tin chi tiết hoặc thông báo không tìm thấy. Không tác động ra ngoài."""
    target = item_id.strip().upper()
    for item in _load_items():
        if str(item.get("id", "")).upper() == target:
            return item
    return {"error": f"Không tìm thấy mục {item_id}"}


@tool
def escalate_to_ta(question: str, reason: str, refs: list = None) -> dict:
    """Tạo bản nháp chuyển câu hỏi cho TA xử lý khi thiếu căn cứ, thông báo mâu thuẫn hoặc thuộc học vụ cá nhân.
    Input: question (str), reason (str), refs (list mã nguồn liên quan). Output: dict bản nháp chờ TA duyệt. Không tự gửi ra ngoài."""
    return {
        "draft_status": "pending_ta_review",
        "question": question,
        "reason": reason,
        "refs": refs or [],
        "note": "Bản nháp chờ TA duyệt — hệ thống không tự gửi tin nhắn công khai.",
    }
