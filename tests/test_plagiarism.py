import unittest
from services.plagiarism_service import PlagiarismService

class TestPlagiarism(unittest.TestCase):
    def test_plagiarism_full_match(self):
        # 1. Arrange
        ps = PlagiarismService()
        expected = 100.0
        # 2. Act
        actual = ps.check_plagiarism("he thong quan ly", "he thong quan ly")
        # 3. Assert
        self.assertEqual(expected, actual)

    def test_plagiarism_no_match(self):
        # 1. Arrange
        ps = PlagiarismService()
        expected = 0.0
        # 2. Act
        actual = ps.check_plagiarism("hom nay troi dep", "he thong quan ly")
        # 3. Assert
        self.assertEqual(expected, actual)