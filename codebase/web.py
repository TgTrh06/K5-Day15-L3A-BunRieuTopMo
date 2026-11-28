"""Web UI đơn giản (thư viện chuẩn Python) để demo trực tiếp Trợ lý Discord A2.

Chạy bằng: python codebase/web.py
Mở trình duyệt: http://127.0.0.1:8000
"""
import json
import os
import sys
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

CODEBASE_DIR = os.path.dirname(os.path.abspath(__file__))
if CODEBASE_DIR not in sys.path:
    sys.path.insert(0, CODEBASE_DIR)

import tracing  # noqa: E402
from agent import answer  # noqa: E402

UI_PATH = os.path.join(CODEBASE_DIR, "ui.html")


class DemoHandler(BaseHTTPRequestHandler):
    def _send_json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            with open(UI_PATH, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        self.send_error(404)

    def do_POST(self) -> None:
        if self.path != "/api/ask":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            req = json.loads(self.rfile.read(length).decode("utf-8"))
            text = str(req.get("text", "")).strip()
            if not text:
                self._send_json(400, {"error": "Thiếu câu hỏi."})
                return
            t0 = time.time()
            tracing.begin("web")
            try:
                res = answer(text)
            finally:
                tracing.end()
            self._send_json(200, {
                "output": res.get("output", ""),
                "latency_s": round(time.time() - t0, 2),
            })
        except Exception as e:
            self._send_json(500, {"error": f"{type(e).__name__}: {e}"})

    def log_message(self, format: str, *args) -> None:
        pass


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("127.0.0.1", port), DemoHandler)
    url = f"http://127.0.0.1:{port}"
    print(f"Đang chạy Demo UI tại {url} (nhấn Ctrl+C để dừng)")
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng server.")


if __name__ == "__main__":
    main()
