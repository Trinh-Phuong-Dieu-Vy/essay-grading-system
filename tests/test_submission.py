import unittest
from services.submission_service import SubmissionService
from services.assignment_service import AssignmentService

class TestSubmissionFeature(unittest.TestCase):
    def setUp(self):
        self.sub_service = SubmissionService()
        self.assign_service = AssignmentService()

    def test_save_and_get_submission(self):
        aid = self.assign_service.create_assignment(1, "Đề test Nộp bài", "Câu hỏi", "Đáp án")
        sid = self.sub_service.save_submission(aid, "22T102999", "Nguyen Van Test", "22T102999_NguyenVanTest.docx", "Bài làm mẫu")
        self.assertGreater(sid, 0)
        subs = self.sub_service.get_submissions(aid)
        self.assertEqual(len(subs), 1)

if __name__ == "__main__":
    unittest.main()
 

