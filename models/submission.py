class Submission:
    def __init__(self, sub_id: int, student_id: str, content: str):
        self.id = sub_id
        self.student_id = student_id
        self.content = content
        self.score = 0.0

class SubmissionRepository:
    def __init__(self):
        self.storage = []

    def save(self, sub: Submission):
        self.storage.append(sub)
        return sub