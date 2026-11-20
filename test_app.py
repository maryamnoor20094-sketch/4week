
import unittest
import tempfile
import os

import app as flask_app
from database import create_table, get_messages


class ContactAPITestCase(unittest.TestCase):

    def setUp(self):
        # Create a separate temporary database for each test
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)
        self.temp_db.close()

        flask_app.app.config["TESTING"] = True
        flask_app.app.config["DATABASE"] = self.temp_db.name

        create_table(self.temp_db.name)

        self.client = flask_app.app.test_client()

    def tearDown(self):
        # Remove temporary database after each test
        if os.path.exists(self.temp_db.name):
            os.remove(self.temp_db.name)

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_valid_contact(self):
        response = self.client.post(
            "/api/contact",
            json={
                "name": "Maryam",
                "message": "Testing my application"
            }
        )

        self.assertEqual(response.status_code, 201)

        messages = get_messages(self.temp_db.name)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["name"], "Maryam")

    def test_empty_name(self):
        response = self.client.post(
            "/api/contact",
            json={"name": "", "message": "Hello"}
        )
        self.assertEqual(response.status_code, 400)

    def test_empty_message(self):
        response = self.client.post(
            "/api/contact",
            json={"name": "Maryam", "message": ""}
        )
        self.assertEqual(response.status_code, 400)

    def test_name_only_spaces(self):
        response = self.client.post(
            "/api/contact",
            json={"name": "   ", "message": "Hello"}
        )
        self.assertEqual(response.status_code, 400)

    def test_message_only_spaces(self):
        response = self.client.post(
            "/api/contact",
            json={"name": "Maryam", "message": "   "}
        )
        self.assertEqual(response.status_code, 400)

    def test_name_too_long(self):
        response = self.client.post(
            "/api/contact",
            json={"name": "A" * 51, "message": "Hello"}
        )
        self.assertEqual(response.status_code, 400)

    def test_message_too_long(self):
        response = self.client.post(
            "/api/contact",
            json={"name": "Maryam", "message": "A" * 501}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_json(self):
        response = self.client.post(
            "/api/contact",
            data="invalid-json",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
