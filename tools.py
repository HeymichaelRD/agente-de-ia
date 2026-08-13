from knowledge_base import PRECIOS, DISPONIBILIDAD
import json
import os
import unicodedata

def normalizar(texto: str) -> str:
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    return " ".join(texto.split())

def consultar_precio(programa: str):
    programa = normalizar(programa)
    if programa in PRECIOS:
        return f"El precio de {programa} es de RD${PRECIOS[programa]}"
    return f"No encontre información de precio para {programa}"

def verificar_disponibilidad(programa: str) -> str:
    programa = normalizar(programa)
    if programa in DISPONIBILIDAD:
        cupos = DISPONIBILIDAD[programa]
        if cupos > 0:
            return f"Sí, hay {cupos} disponibles para {programa}."
        return f"Lo sentimos. No hay cupos disponibles para {programa} en este caso"
    return f"No encuentro disponibilidad para {programa}"

def registrar_contacto(nombre:str, telefono: str) -> str:
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }
    
    archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contactos.json")
    
    if os.path.exists(archivo):
        try:
            with open(archivo, "r") as f:
                contactos = json.load(f)
        except json.JSONDecodeError:
            contactos = []
            
    else: 
        contactos = []
        
    for contactos_existentes in contactos:
        if contactos_existentes['telefono'] == telefono:
            return f"El contacto con el telefono {telefono} ya esta registrado"
        
    contactos.append(contacto)
    
    with open(archivo, "w") as f:
        json.dump(contactos, f, indent=2, ensure_ascii=False)
        
    return f"Listo {nombre}. Registramos tu contacto"