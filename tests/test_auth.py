import unittest
from services.auth_service import AuthService

class TestAuthFeature(unittest.TestCase):
    def setUp(self):
        self.auth = AuthService()

    def test_register_and_login(self):
        self.auth.register("Test User", "unittest_gv@test.com", "123456")
        user = self.auth.login("unittest_gv@test.com", "123456")
        self.assertIsNotNone(user)
        self.assertEqual(user["full_name"], "Test User")

if __name__ == "__main__":
    unittest.main()
