import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/bigquery/credentials.json"

client = bigquery.Client()
dataset_id = "n8n-automatizations-468421.dwh_gld_data"
tables = list(client.list_tables(dataset_id))

if tables:
    print(f"Tablas en {dataset_id}:")
    for table in tables:
        print(f"- {table.table_id}")
else:
    print(f"No se encontraron tablas en {dataset_id}.")
