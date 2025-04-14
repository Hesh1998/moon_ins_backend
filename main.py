# Import dependencies
from flask import Flask
from flask_cors import CORS
from agent_service.microservice_logic import agent_bp

# Create Flask application
app = Flask(__name__)
CORS(app)

app.register_blueprint(agent_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)