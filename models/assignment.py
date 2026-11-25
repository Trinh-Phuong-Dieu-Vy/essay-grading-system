from dataclasses import dataclass
from typing import Optional

@dataclass
class Assignment:
    course_id: int
    title: str
    question_text: str
    sample_answer: str
    id: Optional[int] = None

    def is_valid(self) -> bool:
        return bool(self.title.strip() and self.question_text.strip() and self.sample_answer.strip())