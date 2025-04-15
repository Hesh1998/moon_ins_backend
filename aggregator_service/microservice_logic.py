import psycopg2
import boto3
import json
from datetime import datetime

# Load DB credentials from Secrets Manager
client = boto3.client('secretsmanager', region_name='ap-southeast-1')
secret = client.get_secret_value(SecretId='rs/admin/credentials')
creds = json.loads(secret['SecretString'])

# ETL logic for dwh.dim_product warehouse table
def load_dim_product():
    try:
        # Connect to transactional database
        conn_trx = psycopg2.connect(
            host=creds['host'],
            port=creds['port'],
            user=creds['username'],
            password=creds['password'],
            dbname='mat-tdb'
        )
        cursor_trx = conn_trx.cursor()

        # Connect to data warehouse database
        conn_dwh = psycopg2.connect(
            host=creds['host'],
            port=creds['port'],
            user=creds['username'],
            password=creds['password'],
            dbname='mat-dwh'
        )
        cursor_dwh = conn_dwh.cursor()

        # Truncate dimension table
        cursor_dwh.execute("TRUNCATE TABLE dwh.dim_product")

        # Fetch product data from transactional table
        cursor_trx.execute("""
            SELECT product_id, product_name, product_type, target
            FROM tdb.insurance_product
        """)
        rows = cursor_trx.fetchall()

        # Insert into dwh.dim_product with auto-incrementing product_sk
        for sk, row in enumerate(rows, start=1):
            cursor_dwh.execute("""
                INSERT INTO dwh.dim_product (product_sk, product_id, product_name, product_type, target)
                VALUES (%s, %s, %s, %s, %s)
            """, (sk, row[0], row[1], row[2], row[3]))

        conn_dwh.commit()
        conn_trx.close()
        conn_dwh.close()

        print("load_dim_product completed successfully.")

    except Exception as e:
        print(f"Error in load_dim_product: {e}")

# 1) Run the full ETL process for datawarehouse
# 2) Load aggregated sales tables in data warehouse
def run_aggregator_service():
    print(f"Aggregation Job Started at {datetime.now()}")

    # ETL process for DWH
    load_dim_product()

    print(f"Aggregation Job Completed at {datetime.now()}")