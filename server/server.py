from flask import Flask, jsonify
from flask_cors import CORS

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
