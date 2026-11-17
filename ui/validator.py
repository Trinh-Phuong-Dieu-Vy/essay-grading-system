class InputValidator:
    def is_valid_input(self, student_id: str, content: str) -> bool:
        return bool(student_id.strip()) and bool(content.strip())