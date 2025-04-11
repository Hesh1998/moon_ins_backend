# Import dependencies
from flask import Flask, jsonify
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)
CORS(app)

@app.route("/test-app", methods=["GET"])
def test_app():
    return jsonify({"message": "Hello, world!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)