
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SmartNestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            status_code = 200
            response = {
                "status": "healthy",
                "application": "SmartNest AI"
            }

        elif self.path == "/":
            status_code = 200
            response = {
                "message": "SmartNest AI - CI/CD Automation Successful."
            }

        else:
            status_code = 404
            response = {
                "error": "Not found"
            }

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), SmartNestHandler)
    print("SmartNest AI running on port 8000")
    server.serve_forever()
