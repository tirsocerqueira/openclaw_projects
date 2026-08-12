# DECISIONS.md - Registro de Decisiones de Arquitectura y Negocio

## ADR-001: Arquitectura Monolítica Modular para el MVP
- **Fecha:** 2026-08-10
- **Contexto:** Se requiere un MVP funcional en 30 días ejecutable en un portátil de 8 GB de RAM sin sobreingeniería.
- **Decisión:** Descartar microservicios distribuidos (nada de Kubernetes o Kafka). Se estructurará como un monolito modular orquestado mediante Docker Compose con servicios lógicos separados (API FastAPI, motor de inferencia YOLO, SQLite y frontend React).
- **Consecuencias:** Desarrollo y despliegue ultrarrápidos, bajo consumo de recursos y facilidad de mantenimiento en solitario.
