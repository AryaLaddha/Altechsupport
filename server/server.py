from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import psycopg2
import psycopg2.extras  # Import this to use DictCursor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access environment variables
database_url = os.getenv('DATABASE_URL')
print(database_url)

# Function to establish a database connection
def get_db_connection():
    conn = psycopg2.connect(database_url)
    return conn

# Function to fetch all comments
def get_comments():
    conn = get_db_connection()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute("SELECT * FROM Comments;")
        comments = cur.fetchall()
    conn.close()
    return comments

# Flask app initialization
app = Flask(__name__)

# CORS configuration to allow requests from any origin (use specific origins in production)
CORS(app)

# Example API endpoint
@app.route('/api/members', methods=['GET'])
def members():
    return jsonify({
        "members": ["member1", "member2", "member3"]
    })

# Endpoint to fetch comments
@app.route('/api/comments', methods=['GET'])
def comments():
    try:
        comments = get_comments()
        return jsonify(comments)
    except psycopg2.Error as e:
        error_msg = f"Database error: {e}"
        return Response(error_msg, status=500)

if __name__ == '__main__':
    app.run(debug=True)
