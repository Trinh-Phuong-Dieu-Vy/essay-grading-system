import unittest
from services.rubric_service import RubricService
from services.assignment_service import AssignmentService

class TestRubricFeature(unittest.TestCase):
    def setUp(self):
        self.rubric_service = RubricService()
        self.assign_service = AssignmentService()

    def test_save_and_get_rubrics(self):
        # Lấy danh sách assignment có sẵn hoặc tạo mới với đúng cấu trúc của nhóm
        assignments = self.assign_service.get_all_assignments()
        if assignments:
            aid = assignments[0]['id']
        else:
            # Nếu chưa có đề nào, truyền đúng các trường theo schema (course_id, title, description, deadline, ...)
            aid = self.assign_service.create_assignment(1, "Đề test Rubric", "Mô tả đề", "2026-12-31 23:59:00")
            
        items = [
            {"idea_content": "Ý 1", "max_score": 5.0, "weight_percent": 50.0},
            {"idea_content": "Ý 2", "max_score": 5.0, "weight_percent": 50.0}
        ]
        self.rubric_service.save_rubrics(aid, items)
        saved = self.rubric_service.get_rubrics(aid)
        self.assertEqual(len(saved), 2)

if __name__ == "__main__":
    unittest.main()

