import unittest
from services.compare_service import CompareService

class TestCompareFeature(unittest.TestCase):
    def setUp(self):
        self.service = CompareService()

    def test_highlight_text(self):
        html = self.service.highlight_text("Đây là câu bị trùng lặp.", ["câu bị trùng lặp"])
        self.assertIn("<mark", html)
        self.assertIn("câu bị trùng lặp", html)

if __name__ == "__main__":
    unittest.main()
