from database.db_helper import DbHelper

class RubricService:
    def __init__(self):
        self.db = DbHelper()

    def save_rubrics(self, assignment_id: int, items: list):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rubrics WHERE assignment_id = %s", (assignment_id,))
        sql = "INSERT INTO rubrics (assignment_id, idea_content, max_score, weight_percent) VALUES (%s, %s, %s, %s)"
        for item in items:
            cursor.execute(sql, (assignment_id, item["idea_content"], item["max_score"], item["weight_percent"]))
        conn.commit()
        cursor.close()
        conn.close()

    def get_rubrics(self, assignment_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rubrics WHERE assignment_id = %s", (assignment_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
