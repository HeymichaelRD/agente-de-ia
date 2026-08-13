herramientas_disponibles = [
    {
        "type": "function",
        "function": {
            "name": "consultar_precio",
            "description": "Consulta el precio de un programa académico específico.",
            "parameters": {
                "type": "object",
                "properties": {
                    "programa": {
                        "type": "string",
                        "description": "El nombre del programa, por ejemplo 'carrera de ia'"
                    }
                },
                "required": ["programa"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "verificar_disponibilidad",
            "description": "Verifica cuántos cupos hay disponibles para un programa específico.",
            "parameters": {
                "type": "object",
                "properties": {
                    "programa": {"type": "string", "description": "El nombre del programa"}
                },
                "required": ["programa"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "registrar_contacto",
            "description": "Registra los datos de un nuevo contacto interesado en inscribirse.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {"type": "string", "description": "Nombre completo del contacto"},
                    "telefono": {"type": "string", "description": "Número de teléfono del contacto"}
                },
                "required": ["nombre", "telefono"]
            }
        }
    }
]