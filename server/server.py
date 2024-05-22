from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2

# Load the environment variable
database_url = os.getenv('DATABASE_URL')
# Connect to the PostgreSQL database
conn = psycopg2.connect(database_url)
with conn.cursor() as cur:
    cur.execute("SELECT version()")
    print(cur.fetchone())
# Close the connection
conn.close()


app = Flask(__name__)

# CORS configuration to allow requests from any origin (use specific origins in production)
CORS(app)

@app.route('/api/members', methods=['GET'])
def members():
    return jsonify(
        {
            "members": ["member1", "member2", "member3"]
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
