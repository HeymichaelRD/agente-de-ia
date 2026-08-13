from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from tools import consultar_precio, verificar_disponibilidad, registrar_contacto
from prompts import SYSTEM_PROMPT
from schemas import herramientas_disponibles

load_dotenv()

client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY_V2'),
    base_url="https://api.groq.com/openai/v1"
)

funciones_disponibles = {
    "consultar_precio": consultar_precio,
    "verificar_disponibilidad": verificar_disponibilidad,
    "registrar_contacto": registrar_contacto
}

def iniciar_conversacion():
    historial = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    print("Agente listo (escribre 'salir' para terminar)\n")
    
    while True:
        mensaje_usuario = input("Tu: ")
        if mensaje_usuario.lower() == "salir":
            break

        historial.append({"role": "user", "content": mensaje_usuario})

        respuesta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=historial,
            tools=herramientas_disponibles
        )

        mensaje = respuesta.choices[0].message   
         
        if mensaje.tool_calls:
            historial.append(mensaje)

            for llamada in mensaje.tool_calls:
                nombre_funcion = llamada.function.name
                argumentos = json.loads(llamada.function.arguments)

                funcion = funciones_disponibles[nombre_funcion]
                resultado = funcion(**argumentos)

                historial.append({
                    "role": "tool",
                    "tool_call_id": llamada.id,
                    "content": resultado
                })

            respuesta_final = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=historial
            )
            texto_respuesta = respuesta_final.choices[0].message.content
        else:
            texto_respuesta = mensaje.content

        historial.append({"role": "assistant", "content": texto_respuesta})
        print(f"Agente: {texto_respuesta}\n")
        
#respuesta = client.chat.completions.create(#
#    model="llama-3.3-70b-versatile",
#    messages=[
#        {
#            'role': 'user', 
#            'content': 'hola, esta funcionando'
#        }
#    ],
#)

if __name__ == "__main__":
    iniciar_conversacion()

# print(respuesta.choices[0].message.content)

# print(PRECIOS)
# print()
# print(DISPONIBILIDAD)