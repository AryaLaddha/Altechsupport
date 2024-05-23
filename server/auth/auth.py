import psycopg2

class AuthManager:
    def __init__(self, db):
        self.db = db

    def authenticate_user(self, email, password):
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Users WHERE email = %s AND passwordhash = %s;", (email, password))
                user = cur.fetchone()
            return user
        except psycopg2.Error as e:
            print(f"Error fetching user: {e}")
            return None
        finally:
            if conn:
                conn.close()
