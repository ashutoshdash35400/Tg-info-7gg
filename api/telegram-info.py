import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

DEVELOPER = "@rajanhackerd"
SERVICE = "telegram-info"


def json_response(handler, payload, status=200):
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type, X-API-Key")
    handler.end_headers()
    handler.wfile.write(body)


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        json_response(self, {"success": True})

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        supplied_key = query.get("key", [""])[0]
        expected_key = os.environ.get("API_KEY", "change-me")
        tg_id = query.get("tg", [""])[0].strip()

        if expected_key != "*" and supplied_key != expected_key:
            json_response(
                self,
                {
                    "success": False,
                    "service": SERVICE,
                    "developer": DEVELOPER,
                    "error": "Invalid API key",
                },
                401,
            )
            return

        if not tg_id or not tg_id.isdigit():
            json_response(
                self,
                {
                    "success": False,
                    "service": SERVICE,
                    "developer": DEVELOPER,
                    "error": "The tg parameter must be a numeric Telegram user ID",
                },
                400,
            )
            return

        # This endpoint intentionally does not retrieve or disclose private phone data.
        # Only public, user-supplied metadata can be added here after authorization.
        payload = {
            "channel": "",
            "credits_remaining": int(os.environ.get("CREDITS_REMAINING", "0")),
            "data": {
                "Today_Used": 0,
                "result": {
                    "country": "",
                    "country_code": "",
                    "msg": "Public Telegram metadata only; private phone lookup is disabled",
                    "number": None,
                    "response_time": "0ms",
                    "tg_id": tg_id,
                },
            },
            "developer": DEVELOPER,
            "service": SERVICE,
            "success": True,
        }
        json_response(self, payload)

    def log_message(self, format, *args):
        return
                      
