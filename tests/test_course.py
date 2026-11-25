import unittest
from services.course_service import CourseService


class TestCourseFeature(unittest.TestCase):
    def setUp(self):
        self.service = CourseService()

    def test_create_and_get_course(self):
        cid = self.service.create_course(1, "TEST101", "Môn học Unit Test", "HK1")
        self.assertGreater(cid, 0)
        courses = self.service.get_courses(1)
        codes = [c["course_code"] for c in courses]
        self.assertIn("TEST101", codes)


if __name__ == "__main__":
    unittest.main()