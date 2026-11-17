import unittest
from ui.validator import InputValidator

class TestValidator(unittest.TestCase):
    def test_valid_input(self):
        # 1. Arrange
        iv = InputValidator()
        expected = True
        # 2. Act
        actual = iv.is_valid_input("SV01", "Noi dung bai lam hop le")
        # 3. Assert
        self.assertEqual(expected, actual)

    def test_empty_content(self):
        # 1. Arrange
        iv = InputValidator()
        expected = False
        # 2. Act
        actual = iv.is_valid_input("SV01", "   ")
        # 3. Assert
        self.assertEqual(expected, actual)