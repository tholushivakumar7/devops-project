
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SmartNestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "SmartNest AI"
            }
            self.send_response(200)
        else:
            response = {
                "message": ""message": "SmartNest AI - Version 2 deployed automatically! Deployed""
            }
            self.send_response(200)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), SmartNestHandler)
    print("SmartNest AI demo running on port 8000")
    server.serve_forever()
