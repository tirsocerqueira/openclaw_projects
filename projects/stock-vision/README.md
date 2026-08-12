# StockVision (MVP) 🚀

Sistema SaaS de gestión de inventario automática mediante visión por ordenador en tiempo real, optimizado para ejecutarse de forma eficiente en un portátil local (8 GB de RAM).

## 🛠️ Stack Tecnológico Obligatorio

*   **Backend:** Python 3.12, FastAPI, SQLite (para persistencia simplificada).
*   **Machine Learning / Visión:** YOLOv11n (Inferencia ultraligera), ByteTrack (Tracking de objetos).
*   **Frontend:** React + Vite.
*   **Infraestructura:** Docker Compose.

---

## 📂 Estructura del Repositorio

```text
stockvision/
├── README.md               # Este archivo. Guía de inicio y visión general.
├── AGENT.md                # Reglas y directrices del Agente de IA.
├── ROADMAP.md              # Plan de ejecución del MVP (30 días) detallado.
├── DECISIONS.md            # Registro de decisiones de arquitectura y negocio (ADRs).
├── docker-compose.yml      # Orquestación de servicios locales para desarrollo.
├── business/               # FASE 1: Análisis y validación de negocio.
│   └── problem.md          # Definición del problema e impacto.
├── architecture/           # FASE 3: Planos de arquitectura y C4.
│   └── overview.md         # Vista general del sistema y flujos de datos.
├── product/                # FASE 2: Gestión de producto, user stories, KPIs.
├── specs/                  # FASE 4: APIs, esquemas de datos y contratos.
├── ml/                     # FASE 5: Etiquetado, entrenamiento y evaluación.
├── services/               # FASE 6: Código fuente de los servicios.
├── tests/                  # FASE 7: Control de calidad y benchmarks.
└── docs/                   # FASE 8: Material de ventas y demos.
```

---

## ⚡ Quick Start (Inicio Rápido)

Para levantar el entorno completo del MVP (FastAPI, SQLite, React Dashboard) en desarrollo:

```bash
docker compose up --build
```

*   **Dashboard React:** `http://localhost:5173`
*   **API FastAPI (Docs Swagger):** `http://localhost:8000/docs`
