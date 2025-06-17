# archivo = open("archivo.txt", "w")
# archivo.write("Hola, este es un archivooooooooooooooooo")
# archivo.write("Hola, este es un archivooooooooooooooooo")
# archivo.write("Hola, este es un archivooooooooooooooooo")
# archivo.write("Hola, este es un archivooooooooooooooooo")
# archivo.write("Hola, este es un archivooooooooooooooooo")
# archivo.close()

# archivo = open("archivo.txt", "a")
# archivo.write("\nHola, este es un archivo modificadooooo")
# archivo.close()

# archivo = open("carpeta_ejemplo/archivo.txt", "w")
# archivo.write("Hola, este es un archivooooooooooooooooo")
# archivo.close()

# print()
# archivo = open("archivo.txt", "r")
# contenido = archivo.read()
# print(contenido)
# archivo.close()
# print()


# print()
# archivo = open("carpeta_ejemplo/archivo.txt", "r")
# contenido = archivo.read()
# print(contenido)
# print()

# print()
# archivo = open("carpeta_ejemplo/archivo.txt", "r")
# contenido = archivo.read()
# print(contenido)
# archivo.close()
# print()

############################################################################

print()
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
print()

with open("carpeta_ejemplo/archivo.txt", "a") as archivo:
    archivo.write("\nHola, este es un archivo modificadooooo")

with open("D:/python-comision-78315/archivo_fuera.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


###########################################################
print("\n--- Contar líneas, palabras y caracteres ---")
print("\n--- Contar líneas, palabras y caracteres ---")
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()

num_lineas = len(lineas)
num_palabras = sum(len(linea.split()) for linea in lineas)
num_caracteres = sum(len(linea) for linea in lineas)

print(f"Número de líneas: {num_lineas}")
print(f"Número de palabras: {num_palabras}")
print(f"Número de caracteres: {num_caracteres}")
