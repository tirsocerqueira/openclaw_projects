import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/bigquery/credentials.json"
client = bigquery.Client()

# Primero obtenemos el esquema para confirmar el nombre de la columna de fecha/id
table_ref = client.dataset("dwh_gld_data").table("gold_round_summary")
table = client.get_table(table_ref)

# Buscamos una columna que parezca de fecha o ID
columns = [field.name for field in table.schema]
print(f"Columnas disponibles: {columns}")

# Ejecutamos la query usando la columna más probable (si existe round_date, si no, round_id)
order_col = "round_date" if "round_date" in columns else "round_id"
query = f"""
SELECT *
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
ORDER BY {order_col} DESC
LIMIT 5
"""

query_job = client.query(query)
results = query_job.result()

print(f"\nResultados (ordenados por {order_col}):")
for row in results:
    print(dict(row))
