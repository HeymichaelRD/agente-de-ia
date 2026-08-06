from knowledge_base import PRECIOS, DISPONIBILIDAD

def consultar_precio(programa: str):
    programa = programa.lower()
    if programa in PRECIOS:
        return f"El precio de {programa} es de RD${programa}"
    return f"No encontre información de precio para {programa}"

def verificar_disponibilidad(programa: str) -> str:
    programa = programa.lower()
    if programa in DISPONIBILIDAD:
        cupos = DISPONIBILIDAD[programa]
        if cupos > 0:
            return f"Sí, hay {cupos} disponibles para {programa}."
        return f"Lo sentimos. No hay cupos disponibles para {programa} en este caso"
    return "No encuentro disponibilidad para {programa}"

def registrar_contacto(nombre:str, telefono: int):
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }
    
    archivo = "contactos.json"
    
    if os.path.exists(archivo):
        try:
            with open(archivo, "r") as f:
                contactos = json.load(f)
        except json.JSONDecodeError:
            contactos = []
            
    else: 
        contactos = []