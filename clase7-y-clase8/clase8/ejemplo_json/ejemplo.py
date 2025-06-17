import json

# Crear un diccionario de ejemplo
usuario = {
    "id": 101,
    "nombre": "Luis Fernández",
    "activo": True,
    "roles": ["admin", "editor"],
    "hobbies": ["leer", "viajar", "programar"]
}

# **1. Serialización: Convertir el diccionario a una cadena JSON**
print("\n--- Serialización: Diccionario a cadena JSON ---")
json_str = json.dumps(usuario, indent=4)
print("Cadena JSON generada:")
print(json_str)

# **2. Serialización: Guardar el diccionario en un archivo JSON**
print("\n--- Guardar en un archivo JSON ---")
with open("ejemplo_json/usuario.json", "w") as archivo:
    json.dump(usuario, archivo, indent=4)
print("Datos guardados en 'usuario.json'.")

# **3. Deserialización: Leer desde la cadena JSON**
print("\n--- Deserialización: Cadena JSON a diccionario ---")
datos_desde_cadena = json.loads(json_str)
print("Datos deserializados desde cadena:")
print(datos_desde_cadena)

# **4. Deserialización: Leer desde un archivo JSON**
print("\n--- Leer desde un archivo JSON ---")
with open("ejemplo_json/usuario.json", "r") as archivo:
    datos_desde_archivo = json.load(archivo)
print("Datos deserializados desde archivo:")
print(datos_desde_archivo)

# **5. Uso de los datos deserializados**
print("\n--- Uso de los datos cargados ---")
print(f"Nombre del usuario: {datos_desde_archivo['nombre']}")
print(f"Roles: {', '.join(datos_desde_archivo['roles'])}")
print(f"Hobbies: {', '.join(datos_desde_archivo['hobbies'])}")
