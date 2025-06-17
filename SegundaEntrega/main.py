import os
from Clases.Cliente import Cliente

def main():
    # Inicializo un cliente vacío para evitar errores al verificar si el cliente existe
    nuevo_cliente = None
    while True:
        print("Opciones:")
        print("1. Crear cliente nuevo")
        print("2. Cargar cliente nuevo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            dni = input("Ingrese el DNI del cliente: ").strip()
            if nuevo_cliente and nuevo_cliente.verificarCliente(dni):
                print(f"El cliente con DNI {dni} ya existe y fue cargado con éxito.")
                continue
            nombre = input("Ingrese el nombre del cliente: ").strip()
            apellido = input("Ingrese el apellido del cliente: ").strip()
            edad = input("Ingrese la edad del cliente: ").strip()
            genero = input("Ingrese el género del cliente: ").strip()
            telefono = input("Ingrese el teléfono del cliente: ").strip()
            email = input("Ingrese el email del cliente: ").strip()
            usuario = input("Ingrese el usuario del cliente: ").strip()
            contrasena = input("Ingrese la contraseña del cliente: ").strip()
            nuevo_cliente = Cliente(nombre, apellido, edad, genero, dni, telefono, email, usuario, contrasena)
            nuevo_cliente.guardarCliente()
            print(f"Cliente {nombre} {apellido} creado exitosamente con usuario {usuario}.")

        elif opcion == '2':
            dni = input("Ingrese el DNI del cliente: ").strip()
            nuevo_cliente = Cliente.cargarCliente(dni)  
            if nuevo_cliente is None:
                print(f"No existe el cliente con DNI {dni}.")
                continue
        elif opcion == '3':
            print("\nGracias por usar el sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")
            continue  
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("Opciones:")
            print("\n1. Mostrar datos del cliente")
            print("\n2. Cambiar contraseña del cliente")
            print("\n3. Volver al menú principal")
            opcion = input("\nSeleccione una opción: ")
            if opcion == '1':
                nuevo_cliente.imprimirDatos()
            elif opcion == '2':
                vieja = input("Ingrese la contraseña actual: ").strip()
                nueva = input("Ingrese la nueva contraseña: ").strip()
                nuevo_cliente.cambiarContrasena(vieja, nueva, nuevo_cliente.getUsuario())
            elif opcion == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Opción inválida, intente nuevamente.")
            


#Ejecuto la funcion principal
try:
    main()
except Exception as e:
    print(f"\nHa ocurrido un error inesperado: {e}")