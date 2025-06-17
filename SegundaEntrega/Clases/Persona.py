class Persona:
    def __init__(self, nombre, apellido, edad, genero, dni): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.dni = dni
         
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}" 
    
    ## Getters y Setters de la clase persona
    

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getEdad(self):
        return self.edad
       
    def getGenero(self):
        return self.genero
    
    def getDNI(self):
        return self.dni
    
    def setNombre(self, nombre):
        self.nombre = nombre    
        
    def setEdad(self, edad):
        self.edad = edad    
    
    def setGenero(self, genero):
        self.genero = genero    
    
    def setDNI(self, dni):
        self.dni = dni
    
    
