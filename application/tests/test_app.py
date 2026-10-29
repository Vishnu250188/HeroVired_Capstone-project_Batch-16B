import os
import sys
import unittest

# Make the application's src directory available to Python.
APP_SRC = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src")
)
sys.path.insert(0, APP_SRC)

from app import app


class TestApplication(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_returns_success(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(
            data["message"],
            "DevOps Capstone Application"
        )
        self.assertEqual(data["status"], "success")

    def test_health_endpoint_returns_healthy(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["status"],
            "healthy"
        )


if __name__ == "__main__":
    unittest.main()
