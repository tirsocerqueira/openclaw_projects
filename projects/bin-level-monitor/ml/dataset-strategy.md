# ML Strategy - BinLevel

## Enfoque: Regresión Volumétrica
A diferencia del conteo, aquí estimamos el porcentaje de llenado (0-100%).

## Estrategia de Datos
- **Dataset:** Colección de imágenes cenitales (vistas desde arriba) de contenedores en diversos estados de llenado.
- **Etiquetado:** Cada imagen se etiqueta con un valor de 0 a 100 (estimación visual del % de volumen ocupado).
- **Modelo:** ResNet o EfficientNet pre-entrenado adaptado para regresión (output: valor escalar), o YOLO con clasificación de cajas si se segmentan residuos.

## Métricas
- **MAPE (Mean Absolute Percentage Error):** Objetivo < 10%.
- **MAE (Mean Absolute Error):** Objetivo < 5% de llenado.

## Pipeline
1. Captura (Imagen cenital).
2. Preprocesamiento (Alineación con el borde del cubo).
3. Inferencia (Regresión de volumen).
4. Persistencia (Guardado en SQLite).
