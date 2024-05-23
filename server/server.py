from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from db import Database
import psycopg2
from auth.auth import AuthManager

# Flask app initialization
app = Flask(__name__)

# CORS configuration to allow requests from any origin (use specific origins in production)
CORS(app)

# Initialize the Database object
db = Database()

# Initialize the AuthManager object
auth_manager = AuthManager(db)

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
        comments = db.get_comments()
        return jsonify(comments)
    except psycopg2.Error as e:
        error_msg = f"Database error: {e}"
        return Response(error_msg, status=500)

# Endpoint for user authentication
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return Response("Email and password are required.", status=400)

    try:
        user = auth_manager.authenticate_user(email, password)
        if user:
            return jsonify({"message": "Login successful", "user": user})
        else:
            return Response("Invalid credentials", status=401)
    except psycopg2.Error as e:
        error_msg = f"Database error: {e}"
        return Response(error_msg, status=500)

if __name__ == '__main__':
    app.run(debug=True)
