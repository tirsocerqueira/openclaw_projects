import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/node/.openclaw/workspace/config/bigquery/credentials.json"

class GolfAnalystAgent:
    """Agente autónomo especializado en consultar y analizar métricas de golf desde BigQuery."""
    
    def __init__(self, player_id='tirsocerqueira'):
        self.client = bigquery.Client()
        self.player_id = player_id

    def obtener_resumen_ultimas_rondas(self, limit=5):
        query = f"""
        SELECT round_date, course_id, total_gross, total_stableford, total_putts, fir_pct, gir_pct
        FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
        WHERE player_id = '{self.player_id}'
        ORDER BY round_date DESC
        LIMIT {limit}
        """
        query_job = self.client.query(query)
        return [dict(row) for row in query_job.result()]

    def obtener_estadisticas_globales(self):
        query = f"""
        SELECT 
            COUNT(*) as total_rondas,
            AVG(total_gross) as media_gross,
            AVG(total_stableford) as media_stableford,
            AVG(fir_pct) as media_fir,
            AVG(gir_pct) as media_gir,
            AVG(total_putts) as media_putts
        FROM `n8n-automatizations-468421.dwh_gld_data.gold_round_summary`
        WHERE player_id = '{self.player_id}'
        """
        query_job = self.client.query(query)
        results = list(query_job.result())
        return dict(results[0]) if results else {}

if __name__ == "__main__":
    agente = GolfAnalystAgent()
    print("--- ESTADÍSTICAS GLOBALES DEL JUGADOR ---")
    stats = agente.obtener_estadisticas_globales()
    for k, v in stats.items():
        print(f"{k}: {v}")
    
    print("\n--- ÚLTIMAS 3 RONDAS ---")
    rondas = agente.obtener_resumen_ultimas_rondas(3)
    for r in rondas:
        print(r)
