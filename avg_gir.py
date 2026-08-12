import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/node/.openclaw/workspace/config/bigquery/credentials.json"
client = bigquery.Client()

query = """
SELECT AVG(gir_pct) as media_gir_pct, AVG(gir_count) as media_gir_count
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
WHERE player_id = 'tirsocerqueira'
"""

query_job = client.query(query)
results = list(query_job.result())

if results:
    r = results[0]
    print(f"Media GIR %: {r['media_gir_pct']:.2f}%")
    print(f"Media Greenes cogidos: {r['media_gir_count']:.1f} de 18")
