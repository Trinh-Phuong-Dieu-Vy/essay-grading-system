import unittest
from database.db_helper import DbHelper

class TestDbHelper(unittest.TestCase):
    def test_valid_table_name(self):
        # 1. Arrange
        db = DbHelper()
        expected = True
        # 2. Act
        actual = db.is_valid_table("Submission")
        # 3. Assert
        self.assertEqual(expected, actual)

    def test_columns_count(self):
        # 1. Arrange
        db = DbHelper()
        expected = 5
        # 2. Act
        actual = len(db.get_columns())
        # 3. Assert
        self.assertEqual(expected, actual)