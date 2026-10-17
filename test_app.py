
import unittest
import json
from unittest.mock import patch
from io import BytesIO

from app import SmartNestHandler


class TestSmartNestApp(unittest.TestCase):

    def test_home_response(self):
        handler = SmartNestHandler.__new__(SmartNestHandler)
        handler.path = "/"

        handler.send_response = lambda status: setattr(
            handler, "status_code", status
        )
        headers = {}
        handler.send_header = lambda key, value: headers.update(
            {key: value}
        )
        handler.end_headers = lambda: None

        handler.wfile = BytesIO()
        handler.do_GET()

        self.assertEqual(handler.status_code, 200)

        response = json.loads(
            handler.wfile.getvalue().decode()
        )
        self.assertEqual(
            response["message"],
            ""SmartNest AI - Version 2 deployed automatically!""
        )

    def test_health_response(self):
        handler = SmartNestHandler.__new__(SmartNestHandler)
        handler.path = "/health"

        handler.send_response = lambda status: setattr(
            handler, "status_code", status
        )
        handler.send_header = lambda key, value: None
        handler.end_headers = lambda: None

        handler.wfile = BytesIO()
        handler.do_GET()

        self.assertEqual(handler.status_code, 200)

        response = json.loads(
            handler.wfile.getvalue().decode()
        )
        self.assertEqual(response["status"], "healthy")
        self.assertEqual(response["application"], "SmartNest AI")


if __name__ == "__main__":
    unittest.main()
