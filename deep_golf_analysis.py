import os
from google.cloud import bigquery
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/bigquery/credentials.json"
client = bigquery.Client()

query = """
SELECT 
    round_date,
    fir_pct,
    gir_pct,
    total_putts,
    total_penalties,
    total_gross,
    total_net,
    total_stableford
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
WHERE player_id = 'tirsocerqueira'
ORDER BY round_date DESC
"""

df = client.query(query).to_dataframe()

print(f"Total de rondas analizadas: {len(df)}")
print("\n--- MATRIZ DE CORRELACIÓN ---")
# Calcular la correlación de Pearson para todas las variables clave
cols_to_correlate = ['fir_pct', 'gir_pct', 'total_putts', 'total_penalties', 'total_gross', 'total_net', 'total_stableford']
correlation_matrix = df[cols_to_correlate].corr()
print(correlation_matrix[['total_gross', 'total_stableford', 'total_net']])

print("\n--- PROMEDIOS POR CAMPO ---")
query_course = """
SELECT 
    course_id,
    COUNT(*) as total_rounds,
    AVG(total_gross) as avg_gross,
    AVG(total_stableford) as avg_stableford,
    AVG(fir_pct) as avg_fir,
    AVG(gir_pct) as avg_gir,
    AVG(total_putts) as avg_putts
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
WHERE player_id = 'tirsocerqueira'
GROUP BY course_id
ORDER BY total_rounds DESC
"""
df_course = client.query(query_course).to_dataframe()
print(df_course)
