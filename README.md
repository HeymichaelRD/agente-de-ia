# Agente de IA - Talendig

Proyecto desarrollado durante la **Masterclass de AI Agents** impartida por [paulestrella](https://github.com/paulestrella) para estudiantes de **Talendig**, una institución educativa en tecnología.

Es un asistente virtual conversacional por consola que responde preguntas sobre programas académicos, consulta precios y disponibilidad en tiempo real, y registra los datos de contacto de los interesados en inscribirse.

Construido con la API de [Groq](https://groq.com/) (modelo `llama-3.3-70b-versatile`) usando function calling.

## Funcionalidades

- Conversación en español, con un tono cálido y profesional definido en el system prompt.
- **Consulta de precios** de programas académicos.
- **Verificación de disponibilidad** (cupos) por programa.
- **Registro de contactos** (nombre y teléfono) de clientes interesados, evitando duplicados por teléfono.

## Requisitos

- Python 3.10+
- Una API key de [Groq](https://console.groq.com/keys)

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con tu API key de Groq:

```
GROQ_API_KEY_V2= tu_api_key_aqui
```

## Uso

```bash
python app.py
```

Escribe tus mensajes en la consola y el agente responderá. Escribe `salir` para terminar la conversación.

## Estructura del proyecto

```
app.py             # Punto de entrada: loop de conversación y llamadas al modelo
tools.py           # Funciones que el modelo puede invocar (precio, disponibilidad, registro)
schemas.py         # Definición de las herramientas (function calling) para la API
prompts.py         # System prompt del agente
knowledge_base.py  # Datos de precios y disponibilidad por programa
requirements.txt   # Dependencias del proyecto
```

## Datos

- `contactos.json` se genera automáticamente al registrar contactos y **no se versiona** (está en `.gitignore`).
- Los precios y la disponibilidad se definen en [knowledge_base.py](knowledge_base.py); para actualizarlos, edita ese archivo directamente. El listado de programas en el system prompt ([prompts.py](prompts.py)) se genera automáticamente a partir de esos mismos datos, así que no requiere edición aparte.

## Mejoras aplicadas sobre el proyecto base

A partir del código entregado en la masterclass, se hicieron los siguientes ajustes:

- **Fix:** eliminada una llamada de prueba a la API de Groq que se ejecutaba automáticamente al importar `app.py`, sin usarse y consumiendo cuota en cada arranque.
- **Mejora:** normalización de nombres de programas (tildes, mayúsculas, espacios) en `consultar_precio` y `verificar_disponibilidad`, para que variaciones como "Análisis" o "análisis" coincidan igual.
- **Mejora:** `contactos.json` ahora se guarda siempre junto al proyecto (ruta basada en la ubicación del script), en vez de depender del directorio desde el que se ejecute `python app.py`.
- **Mejora:** el `SYSTEM_PROMPT` ahora incluye el listado exacto de programas disponibles (generado dinámicamente desde `knowledge_base.py`), para que el modelo use el nombre correcto al llamar las herramientas incluso si el cliente los menciona de forma informal o abreviada (ej. "la carrera de datos").
- **Seguridad:** removido `contactos.json` (con datos reales de contacto) del historial de git, y agregado `*.json` a `.gitignore` para evitar que vuelva a versionarse.
