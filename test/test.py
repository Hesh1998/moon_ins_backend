# Import dependencies
from flask import Flask, jsonify
from flask_cors import CORS
import boto3
import psycopg2
import json

# Create Flask application
app = Flask(__name__)
CORS(app)

# DB connection configuration
client = boto3.client('secretsmanager', region_name='ap-southeast-1')
secret = client.get_secret_value(SecretId='rs/admin/credentials')
creds = json.loads(secret['SecretString'])

@app.route("/test-app", methods=["GET"])
def test_app():
    return jsonify({"message": "Testing App!"})

@app.route("/test-db-conn", methods=["GET"])
def test_db_conn():
    try:
        conn = psycopg2.connect(
            host=creds['host'],
            port=creds['port'],
            user=creds['username'],
            password=creds['password'],
            dbname='mat-tdb'
        )

        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM tdb.branch;')
        count = cursor.fetchone()[0]
        print("count: ", count)
        cursor.close()
        conn.close()

        return jsonify({"DB Connection: ": "Success"})
    except Exception as e:
        return jsonify({"Error connecting to Redshift": e})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)