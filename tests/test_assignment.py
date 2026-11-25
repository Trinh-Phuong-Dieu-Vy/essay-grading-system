import unittest
from io import BytesIO
import docx
from services.file_parser import extract_text_from_docx
from services.assignment_service import AssignmentService


class TestAssignmentFeature(unittest.TestCase):
    def setUp(self):
        self.service = AssignmentService()

    def test_extract_text_from_docx(self):
        """Kiểm thử đọc văn bản từ file .docx giả lập trong bộ nhớ"""
        doc = docx.Document()
        doc.add_paragraph("Câu 1: Trình bày quy trình Scrum.")
        doc.add_paragraph("Scrum gồm Product Backlog, Sprint Backlog và các buổi họp.")
        
        file_stream = BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)

        result = extract_text_from_docx(file_stream)
        self.assertIn("Câu 1: Trình bày quy trình Scrum.", result)
        self.assertIn("Scrum gồm Product Backlog", result)

    def test_create_and_get_assignment(self):
        """Kiểm thử lưu đề bài & đáp án mẫu vào MySQL và truy vấn lại"""
        new_id = self.service.create_assignment(
            course_id=1,
            title="Đề kiểm thử Unit Test SCRUM-5",
            question_text="Nội dung câu hỏi tự luận mẫu",
            sample_answer="Nội dung đáp án chuẩn mẫu"
        )
        self.assertIsNotNone(new_id)
        self.assertGreater(new_id, 0)

        assignments = self.service.get_all_assignments()
        titles = [item["title"] for item in assignments]
        self.assertIn("Đề kiểm thử Unit Test SCRUM-5", titles)


if __name__ == "__main__":
    unittest.main()