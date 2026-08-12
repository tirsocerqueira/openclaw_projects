import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/node/.openclaw/workspace/config/bigquery/credentials.json"
client = bigquery.Client()

query = """
SELECT round_date, course_id, gir_pct, total_gross
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
WHERE player_id = 'tirsocerqueira'
ORDER BY round_date DESC
LIMIT 1
"""

query_job = client.query(query)
results = list(query_job.result())

if results:
    r = results[0]
    print(f"Última ronda ({r['round_date']} en {r['course_id']}):")
    print(f"- GIR%: {r['gir_pct']}%")
    print(f"- Score Gross: {r['total_gross']}")
else:
    print("No se encontraron registros.")
