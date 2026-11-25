import hashlib
from database.db_helper import DbHelper

class AuthService:
    def __init__(self):
        self.db = DbHelper()

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register(self, full_name: str, email: str, password: str) -> bool:
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO users (full_name, email, password_hash) VALUES (%s, %s, %s)"
            cursor.execute(sql, (full_name, email, self._hash_password(password)))
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            cursor.close()
            conn.close()

    def login(self, email: str, password: str):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT id, full_name, email FROM users WHERE email = %s AND password_hash = %s"
        cursor.execute(sql, (email, self._hash_password(password)))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    def update_profile(self, user_id: int, new_name: str, new_password: str = ""):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        if new_password.strip():
            sql = "UPDATE users SET full_name = %s, password_hash = %s WHERE id = %s"
            cursor.execute(sql, (new_name, self._hash_password(new_password), user_id))
        else:
            sql = "UPDATE users SET full_name = %s WHERE id = %s"
            cursor.execute(sql, (new_name, user_id))
        conn.commit()
        cursor.close()
        conn.close()
