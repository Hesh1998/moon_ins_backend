from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from agent_service.microservice_logic import agent_bp
from integration_service.microservice_logic import integration_bp
from notification_service.microservice_logic import notification_bp
from aggregator_service.microservice_logic import run_aggregator_service

# Create Flask application
app = Flask(__name__)
CORS(app)

# Route/Endpoint blueprints
app.register_blueprint(agent_bp)
app.register_blueprint(integration_bp)
app.register_blueprint(notification_bp)

if __name__ == '__main__':
    # Schedule the aggregator_service job daily at 11:15 AM
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_aggregator_service, 'cron', hour=11, minute=15, timezone=timezone('Asia/Colombo'), max_instances=1, id='daily_aggregation_job')
    scheduler.start()

    # Start Flask web server
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)