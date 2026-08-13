from openai import OpenAI
from dotenv import load_dotenv
import os
from knowledge_base import PRECIOS, DISPONIBILIDAD

load_dotenv()

client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY_V2'),
    base_url="https://api.groq.com/openai/v1"
)

respuesta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            'role': 'user', 
            'content': 'hola, esta funcionando'
        }
    ]
)

# print(respuesta.choices[0].message.content)

print(PRECIOS)
print()
print(DISPONIBILIDAD)