# User Stories - BinLevel

1. Como gestor de flota, quiero visualizar el nivel de llenado de todos los contenedores en un mapa para optimizar la ruta del día.
   - Given: Un conjunto de contenedores con sensores visuales
   - When: Accedo al dashboard
   - Then: Veo el % de llenado de cada uno sobre el plano de Vigo.

2. Como conductor, quiero recibir una ruta optimizada que solo incluya contenedores con >75% de llenado para ahorrar combustible.
   - Given: Una lista de contenedores llenos
   - When: Solicito la ruta del día
   - Then: Se genera un recorrido que evita paradas innecesarias.

3. Como gestor, quiero recibir una alerta inmediata si un contenedor se desborda para enviar una brigada de refuerzo.
   - Given: El nivel de llenado detectado supera el 100%
   - When: El sistema procesa la imagen
   - Then: Se dispara una notificación al equipo de limpieza.

4. Como gestor de mantenimiento, quiero ver un reporte del desgaste estimado de los camiones para planificar reparaciones.
   - Given: Histórico de rutas y orografía del terreno
   - When: Analizo el reporte mensual
   - Then: El sistema estima el ahorro en frenos y transmisiones.

... (resto hasta 10, enfocadas en ahorro, eficiencia, alertas y reportes para gestores municipales).
