Usuarios = {}

def registrar_usuario(nombre, password):
    # Chequeo si el usuario ya existe
    # Si el usuario ya existe, no lo registro y retorno False
    if Usuarios.get(nombre):
        return False
    else:
        Usuarios[nombre] = password
        return True


def login(nombre, password):
    # Chequeo si el usuario existe y si la contraseña es correcta
    if Usuarios.get(nombre) == password:
        return True
    else:
        return False
    pass


def mostrar_datos():
    # Chequeo si hay usuarios registrados
    if not Usuarios:
        print("No hay usuarios registrados.")
        return
    print("\nUsuarios registrados:")
    # Muestro los usuarios y sus contraseñas y la cantidad de usuarios registrados
    for usuario, password in Usuarios.items():
        print(f"\nUsuario: {usuario}, Contraseña: {password}")
    print()
    print("-" * 30)
    print(f"Total de usuarios registrados: {len(Usuarios)}")
    print("-" * 30)

def main():
    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar datos de usuarios")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Capturo el nombre y la contraseña del usuario y lo convierto 
            # a minusculas para evitar problema de case-sensitivity
            nombre = input("Ingrese el nombre de usuario: ").lower() 
            password = input("Ingrese la contraseña: ").lower()
            if registrar_usuario(nombre, password):
                print(f"Usuario {nombre} registrado exitosamente.")
            else:
                print(f"ERROR DE REGISTRO: El nombre de usuario, {nombre}, ya existe en el sistema.")
        
        elif opcion == '2':
            # Capturo el nombre y la contraseña del usuario y lo convierto 
            # a minusculas para evitar problema de case-sensitivity
            nombre = input("Ingrese el nombre de usuario: ").lower()
            password = input("Ingrese la contraseña: ").lower()
            if login(nombre, password):
                print(f"\nUsuario {nombre} ha iniciado sesión.")
            else:
                print("\nERROR DE INICIO DE SESIÓN: Usuario o contraseña incorrectos.")
        
        elif opcion == '3':
            mostrar_datos()
        
        elif opcion == '4':
            print("\nGracias por usar el sistema.")
            break
        
        else:
            print("Opción inválida, intente nuevamente.")

main()