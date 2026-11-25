import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class DbHelper:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "plagiarism_grading")

    def get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def get_columns(self):
        return ["id", "student_id", "content", "plagiarism_rate", "score"]

    def is_valid_table(self, table_name: str) -> bool:
        return table_name.isalpha()