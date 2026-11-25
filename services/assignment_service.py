from database.db_helper import DbHelper

class AssignmentService:
    def __init__(self):
        self.db = DbHelper()

    def create_assignment(self, course_id: int, title: str, question_text: str, sample_answer: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO assignments (course_id, title, question_text, sample_answer)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (course_id, title, question_text, sample_answer))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_all_assignments(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM assignments ORDER BY id DESC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows