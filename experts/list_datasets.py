import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/bigquery/credentials.json"

client = bigquery.Client()
datasets = list(client.list_datasets())

if datasets:
    print("Datasets encontrados:")
    for dataset in datasets:
        print(f"- {dataset.dataset_id}")
else:
    print("No se encontraron datasets en este proyecto.")
