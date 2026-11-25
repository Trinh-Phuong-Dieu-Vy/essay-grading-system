from database.db_helper import DbHelper

class SubmissionService:
    def __init__(self):
        self.db = DbHelper()

    def save_submission(self, assignment_id: int, student_code: str, student_name: str, file_name: str, text: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO submissions (assignment_id, student_code, student_name, file_name, extracted_text)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (assignment_id, student_code, student_name, file_name, text))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_submissions(self, assignment_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, student_code, student_name, file_name FROM submissions WHERE assignment_id = %s", (assignment_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows