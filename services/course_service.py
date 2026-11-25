from database.db_helper import DbHelper


class CourseService:
    def __init__(self):
        self.db = DbHelper()

    def create_course(self, lecturer_id: int, course_code: str, course_name: str, semester: str):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO courses (lecturer_id, course_code, course_name, semester) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (lecturer_id, course_code, course_name, semester))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def get_courses(self, lecturer_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses WHERE lecturer_id = %s ORDER BY id DESC", (lecturer_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def delete_course(self, course_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))
        conn.commit()
        cursor.close()
        conn.close()