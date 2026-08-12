import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/node/.openclaw/workspace/config/bigquery/credentials.json"
client = bigquery.Client()

query = """
SELECT round_date, course_id, birdies, total_gross, total_stableford
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
WHERE player_id = 'tirsocerqueira' AND course_id = 'PONTEDELIMA'
ORDER BY round_date DESC
LIMIT 1
"""

query_job = client.query(query)
results = list(query_job.result())

if results:
    r = results[0]
    print(f"Fecha: {r['round_date']}, Campo: {r['course_id']}")
    print(f"Birdies: {r['birdies']}")
    print(f"Score Bruto: {r['total_gross']}, Stableford: {r['total_stableford']}")
else:
    print("No se encontró la ronda.")
