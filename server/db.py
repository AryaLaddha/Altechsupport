import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Database:
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL')
        self.conn = None

    def get_connection(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(self.database_url)
        return self.conn

    def get_comments(self):
        conn = self.get_connection()
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("SELECT * FROM Comments;")
            comments = cur.fetchall()
        return comments

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
