from flask import Flask
from flask_cors import CORS
from agent_service.microservice_logic import agent_bp
from integration_service.microservice_logic import integration_bp
from notification_service.microservice_logic import notification_bp
from aggregator_service.microservice_logic import run_aggregator_service
from apscheduler.schedulers.background import BackgroundScheduler

# Create Flask application
app = Flask(__name__)
CORS(app)

# Route/Endpoint blueprints
app.register_blueprint(agent_bp)
app.register_blueprint(integration_bp)
app.register_blueprint(notification_bp)

# Schedule the aggregator_service job daily at 7 AM
scheduler = BackgroundScheduler()
scheduler.add_job(run_aggregator_service, 'cron', hour=11, minute=40)
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)