# User Stories - StockVision

1. Como encargado, quiero que el sistema detecte productos en estanterías para conocer mi stock en tiempo real.
   - Given: Una imagen de la estantería
   - When: Se procesa con el motor de visión
   - Then: El sistema debe devolver el conteo de cada SKU detectado.

2. Como encargado, quiero recibir una alerta si el stock baja de un umbral para evitar roturas.
   - Given: El stock calculado es inferior al umbral configurado
   - When: Se actualiza el inventario
   - Then: El sistema debe enviar una alerta en el dashboard.

... (otras 8 historias siguiendo este patrón)
