# from mi_primer_paquete.modulo2 import hola_mundo, hola_mundo2
from mi_primer_paquete.modulo2 import hola_mundo, hola_mundo2


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def metodo1(self):  # nombre y funcionalidad a elección
        pass

    def metodo2(self):  # nombre y funcionalidad a elección
        pass
