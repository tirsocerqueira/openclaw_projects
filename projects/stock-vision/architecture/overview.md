# Arquitectura del Sistema - Vista General (Overview)

Este documento describe la arquitectura general de **StockVision** para el MVP de 30 días. El sistema está diseñado para ser monolítico modular, maximizando el rendimiento en una CPU local con limitaciones de recursos (8 GB RAM) al evitar la sobrecarga de latencia y red que supondría un enfoque distribuido complejo o el uso de colas de mensajes pesadas como Kafka.

---

## 🏗️ Flujo de Datos Principal

```text
  [ Cámara / Móvil ] (Sube imagen o frame)
         │
         ▼
  [ API FastAPI ] ───────► [ Motor de Inferencia (YOLOv11n) ]
         │                               │ (Detección de bounding boxes)
         ▼                               ▼
  [ Base de Datos ] ◄─── [ Motor de Inventario / ByteTrack ]
     (SQLite)            (Tracking de objetos y conteo por SKU)
         ▲
         │ (Consulta de stock y alertas)
  [ Dashboard React ] (Visualización web)
```

1.  **Captura:** Un dispositivo cliente (cámara fija, webcam local o smartphone) captura un frame o imagen estática de la estantería y lo envía a la API de backend mediante HTTP POST.
2.  **Inferencia (ML):** El módulo de visión recibe la imagen y ejecuta el modelo **YOLOv11n** optimizado en CPU para detectar productos individuales basándose en bboxes (cajas delimitadoras) y etiquetas de SKU predefinidas.
3.  **Tracking (ByteTrack):** Se procesan las detecciones consecutivas a través de **ByteTrack** para asegurar la estabilidad temporal de los objetos detectados (evitando dobles conteos debido a ligeros parpadeos u oclusiones momentáneas).
4.  **Inventory Engine:** Consolida el conteo total por cada SKU detectado, cruza los resultados con el stock de seguridad y persiste los datos del estado actual de las baldas en la base de datos **SQLite**.
5.  **Alertas & Dashboard:** Si un producto está por debajo del umbral mínimo configurado, se activa un flag de alerta de bajo stock. El **Dashboard React** consulta periódicamente (mediante polling corto) el estado actual para refrescar la vista en tiempo real y desplegar las notificaciones oportunas.

---

## 📦 Componentes del MVP (Docker Compose)

El sistema completo se orquesta como un único entorno de desarrollo local con los siguientes servicios:

*   **`services/api` (FastAPI):** Expone los endpoints HTTP para la ingesta de imágenes, la gestión de inventario, la lectura de alertas y la exportación de datos en formato CSV.
*   **`services/dashboard` (React + Vite):** Panel visual del usuario para configurar umbrales de stock, ver el conteo de la última imagen procesada y descargar reportes.
*   **Base de datos:** SQLite en un volumen persistente local.
*   **Modelos de ML:** Pesos de YOLOv11n cargados directamente en la memoria local del backend.
