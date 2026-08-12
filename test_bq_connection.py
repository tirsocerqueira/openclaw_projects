import os
from google.cloud import bigquery

# Set environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/bigquery/credentials.json"

try:
    client = bigquery.Client()
    print(f"Conexión exitosa.")
    print(f"Proyecto detectado: {client.project}")
except Exception as e:
    print(f"Error al conectar: {e}")
