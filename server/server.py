from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from db import Database
import psycopg2
from auth.auth import AuthManager
import jwt
from functools import wraps

# Flask app initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_default_secret_key'

# CORS configuration to allow requests from any origin (use specific origins in production)
CORS(app)

# Initialize the Database object
db = Database()

# Initialize the AuthManager object
auth_manager = AuthManager(db)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['user_id']  # Get user info from the token
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

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
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return Response("Email and password are required.", status=400)

    try:
        user = auth_manager.authenticate_user(email, password)
        if user:
            token = jwt.encode({
                'user_id': user[0]
            }, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({"message": "Login successful", "token": token})
        else:
            return Response("Invalid credentials", status=401)
    except psycopg2.Error as e:
        error_msg = f"Database error: {e}"
        return Response(error_msg, status=500)

# New route to retrieve user profile
@app.route('/api/profile', methods=['GET'])
@token_required
def user_profile(current_user):
    # Simulate fetching user data from a database
    user = {"id": current_user}

    return jsonify({"message": "User profile retrieved successfully", "user": user})

if __name__ == '__main__':
    app.run(debug=True)
