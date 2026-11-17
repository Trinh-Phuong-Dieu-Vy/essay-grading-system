class DbHelper:
    def get_columns(self):
        return ["id", "student_id", "content", "plagiarism_rate", "score"]

    def is_valid_table(self, table_name: str) -> bool:
        return table_name.isalpha()