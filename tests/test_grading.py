import unittest
from services.grading_service import GradingService

class TestGrading(unittest.TestCase):
    def testNoPenalty(self):
        # 1. Arrange
        gs = GradingService()
        expected = 8.0
        # 2. Act
        actual = gs.calculate_final_score(8.0, 10.0)
        # 3. Assert
        self.assertEqual(expected, actual)

    def testNormalPenalty(self):
        # 1. Arrange
        gs = GradingService()
        expected = 4.0
        # 2. Act
        actual = gs.calculate_final_score(8.0, 30.0)
        # 3. Assert
        self.assertEqual(expected, actual)