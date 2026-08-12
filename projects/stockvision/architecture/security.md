# Arquitectura: Seguridad

## Medidas principales
- API restringida mediante autenticación básica en el MVP.
- Validación de tipos de archivos (imágenes) en el endpoint de subida.
- Ejecución de contenedores con usuario no root.
- SQLite con acceso limitado al servicio de API.
