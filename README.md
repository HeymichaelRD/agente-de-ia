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
- Los precios y la disponibilidad se definen en [knowledge_base.py](knowledge_base.py); para actualizarlos, edita ese archivo directamente.
