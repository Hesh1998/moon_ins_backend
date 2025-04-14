from flask import Flask
from flask_cors import CORS
from agent_service.microservice_logic import agent_bp
from integration_service.microservice_logic import integration_bp

# Create Flask application
app = Flask(__name__)
CORS(app)

# Route/Endpoint blueprints
app.register_blueprint(agent_bp)
app.register_blueprint(integration_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)