from app import app
import unittest

import json

BASE_URI = "/user"
sample_username = "Megan@email.com"
sample_payload = {
            "email": sample_username,
            "password": "Password1",
            "name": "Megan"
        }
content_type = 'application/json'

class UserServiceTest(unittest.TestCase):

    def test_A01_post_success_status_code(self):
        tester = app.test_client()
        response = tester.post(BASE_URI, data=json.dumps(sample_payload),content_type=content_type)
        status_code = response.status_code
        self.assertEqual(status_code, 201)

    def test_A02_post_existing_user_status_code(self):
        tester = app.test_client()
        response = tester.post(BASE_URI, data=json.dumps(sample_payload),content_type=content_type)
        status_code = response.status_code
        self.assertEqual(status_code, 400)

    def test_A03_post_existing_user_content(self):
        tester = app.test_client()
        response = tester.post(BASE_URI, data=json.dumps(sample_payload),content_type=content_type)
        self.assertTrue(b"already exists" in response.data)

    def test_B01_get_success_http_status_200(self):
        tester = app.test_client()
        response = tester.get(f"{BASE_URI}/{sample_username}")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_B02_get_success_response_conent(self):
        tester = app.test_client()
        response = tester.get(f"{BASE_URI}/{sample_username}")
        self.assertTrue(sample_username in str(response.data))

    def test_B03_get_missing_user(self):
        tester = app.test_client()
        response = tester.get(f"{BASE_URI}/dummy{sample_username}")
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_B04_get_missing_user_response_conent(self):
        tester = app.test_client()
        response = tester.get(f"{BASE_URI}/dummy{sample_username}")
        self.assertTrue("User Account Not Found" in str(response.data))

    def test_C01_update_password_success_status_code(self):
        tester = app.test_client()
        sample_payload['password'] = "PASSWORD"
        response = tester.put(BASE_URI, data=json.dumps(sample_payload),content_type=content_type)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_C02_update_name_success_response_content(self):
        tester = app.test_client()
        new_name = "NewName"
        sample_payload['name'] = new_name
        temp_response = tester.put(BASE_URI, data=json.dumps(sample_payload),content_type=content_type)
        response = tester.get(f"{BASE_URI}/{sample_username}")
        self.assertTrue(new_name in str(response.data))

    def test_C03_update_missing_user_status_code(self):
        tester = app.test_client()
        new_name = "AnotherName"
        sample_payload['name'] = new_name
        sample_payload['email'] = "random@email.com"
        response = tester.put(BASE_URI, data=json.dumps(sample_payload),content_type=content_type)
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_D01_delete_success(self):
        tester = app.test_client()
        response = tester.delete(f"{BASE_URI}/{sample_username}")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_D02_delete_missing_user(self):
        tester = app.test_client()
        response = tester.delete(f"{BASE_URI}/{sample_username}")
        status_code = response.status_code
        self.assertEqual(status_code, 404)


if __name__ == "__main__":
    unittest.main()