from Clases.Persona import Persona
import json

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, edad, genero, dni, telefono, email, usuario, contrasena):
        super().__init__(nombre, apellido, edad, genero, dni)
        self.telefono = telefono
        self.email = email
        self.usuario = usuario
        self.contrasena = contrasena
                
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad}, Teléfono: {self.telefono}, Email: {self.email}, Usuario: {self.usuario}"
    
    ## Getters y Setters de la clase cliente

    def getTelefono(self):
        return self.telefono
    
    def getEmail(self):
        return self.email
    
    def getUsuario(self):
        return self.usuario
    
    def getContrasena(self):
        return self.contrasena
    
    def setTelefono(self, telefono):
        self.telefono = telefono
        
    def setEmail(self, email):
        self.email = email
        
    def setUsuario(self, usuario):  
        self.usuario = usuario
        
    def setContrasena(self, contrasena):
        self.contrasena = contrasena
        
    ## Metodo para verificar si el cliente existe en el archivo JSON
    def verificarCliente(self, dni):
        try:
            with open('Clases/clientes.json', 'r') as file:
                for line in file:
                    cliente_data = json.loads(line.strip())
                    if cliente_data['dni'] == dni:
                        return True
            return False
        except Exception as e:
            print(f"\nError al verificar el cliente: {e}")
            return False
        
    ## Metodo para imprimir los datos del cliente
        
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}, \nApellido: {self.apellido}, \nEdad: {self.edad}, \nGénero: {self.genero}, \nDNI: {self.dni}, \nTeléfono: {self.telefono}, \nEmail: {self.email}, \nUsuario: {self.usuario}")
        
    ## Metodo para cargar un cliente desde un archivo JSON 
    @classmethod   
    def cargarCliente(cls, dni):
        try:
            with open('Clases/clientes.json', 'r', encoding='utf-8') as file:
                for line in file:
                    cliente_data = json.loads(line.strip())
                    if cliente_data['dni'] == dni:
                        print(f"\nCliente {cliente_data['nombre']} {cliente_data['apellido']} cargado exitosamente.")
                        return cls(
                            cliente_data['nombre'],
                            cliente_data['apellido'],
                            cliente_data['edad'],
                            cliente_data['genero'],
                            cliente_data['dni'],
                            cliente_data['telefono'],
                            cliente_data['email'],
                            cliente_data['usuario'],
                            cliente_data['contrasena']
                        )
            return None
        except Exception as e:
            print(f"\nError al cargar el cliente: {e}")
            return None
    ## Metodo para cambiar la contraseña del cliente
    
    def cambiarContrasena(self, viejaContrasena, nuevaContrasena, usuario):
        if self.usuario != usuario:
            print("\nUsuario incorrecto. No se puede cambiar la contraseña.")
            return
        elif self.contrasena != viejaContrasena:
            print("\nContraseña incorrecta. No se puede cambiar la contraseña.")
            return
        elif self.contrasena == nuevaContrasena:
            print("\nLa nueva contraseña no puede ser igual a la actual.")
            return
        self.contrasena = nuevaContrasena
        # Guardar el cambio en el archivo JSON
        try:
            with open('Clases/clientes.json', 'r+') as file:
                data = file.readlines()
                file.seek(0)
                for line in data:
                    cliente_data = json.loads(line.strip())
                    if cliente_data['usuario'] == self.usuario:
                        cliente_data['contrasena'] = self.contrasena
                    file.write(json.dumps(cliente_data) + '\n')
                file.truncate()
        except Exception as e:
            print(f"\nError al actualizar la contraseña: {e}")
            return
        
        print("\nLa contraseña ha sido cambiada")
        
    ## Metodo para guardar el cliente en un archivo JSON
    
    def guardarCliente(self):
        usuarioJson = self.__cliente_to_json__()
        try:
            with open('Clases/clientes.json', 'a', encoding='utf-8') as file:
                json.dump(usuarioJson, file)
                file.write('\n')
        except IOError as e:
            print(f"\nError al guardar el cliente: {e}")
        
    ## Metodo Privado para convertir el cliente(con todos los datos) a JSON
        
    def __cliente_to_json__(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "genero": self.genero,
            "dni": self.dni,
            "telefono": self.telefono,
            "email": self.email,
            "usuario": self.usuario,
            "contrasena": self.contrasena
        }  