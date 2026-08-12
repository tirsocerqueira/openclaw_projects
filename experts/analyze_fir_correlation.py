import os
from google.cloud import bigquery
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/bigquery/credentials.json"
client = bigquery.Client()

query = """
SELECT 
    round_date,
    fir_pct,
    total_gross,
    total_stableford
FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
WHERE player_id = 'tirsocerqueira'
ORDER BY round_date DESC
"""

df = client.query(query).to_dataframe()

# Calcular correlación de Pearson
correlation_gross = df['fir_pct'].corr(df['total_gross'])
correlation_stableford = df['fir_pct'].corr(df['total_stableford'])

print(f"Correlación FIR% vs Gross Score: {correlation_gross:.2f}")
print(f"Correlación FIR% vs Stableford: {correlation_stableford:.2f}")
print("\nDataFrame (últimos 5):")
print(df.head(5))
