---
name: "local-ollama"
description: "Skill para interactuar con Ollama local a través de curl y host.docker.internal"
---

# local-ollama

Esta skill permite enviar prompts al modelo Ollama configurado en la máquina host (Windows) desde el entorno Docker.

## Uso

Para enviar un prompt al modelo:

```bash
# Ejemplo de uso interno (para el asistente)
curl http://host.docker.internal:11434/api/generate -d '{
  "model": "gemma3:4b",
  "prompt": "Tu prompt aquí",
  "stream": false
}'
```

## Integración

El asistente usará esta skill cuando el usuario pida usar el modelo local.

### Variables de Entorno
Asegúrate de que `OLLAMA_HOST=0.0.0.0` esté configurado en Windows.
