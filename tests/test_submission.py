import unittest
from models.submission import Submission, SubmissionRepository

class TestSubmission(unittest.TestCase):
    def test_save_submission(self):
        # 1. Arrange
        repo = SubmissionRepository()
        sub = Submission(1, "SV01", "Bai lam tu luan")
        expected = 1
        # 2. Act
        repo.save(sub)
        actual = len(repo.storage)
        # 3. Assert
        self.assertEqual(expected, actual)

    def test_default_score(self):
        # 1. Arrange
        sub = Submission(2, "SV02", "Noi dung bai")
        expected = 0.0
        # 2. Act
        actual = sub.score
        # 3. Assert
        self.assertEqual(expected, actual)