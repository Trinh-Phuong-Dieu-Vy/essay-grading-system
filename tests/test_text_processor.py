import unittest
from services.text_processor import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def test_lowercase_split(self):
        # 1. Arrange
        tp = TextProcessor()
        expected = ["cong", "nghe", "phan", "mem"]
        # 2. Act
        actual = tp.preprocess_text("Cong Nghe Phan Mem")
        # 3. Assert
        self.assertEqual(expected, actual)

    def test_remove_punctuation(self):
        # 1. Arrange
        tp = TextProcessor()
        expected = ["xin", "chao", "viet", "nam"]
        # 2. Act
        actual = tp.preprocess_text("Xin chao, Viet Nam!")
        # 3. Assert
        self.assertEqual(expected, actual)