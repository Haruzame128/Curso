from mi_primer_paquete.modulo2 import hola_mundo, hola_mundo2
from mi_primer_paquete.modulo1 import Persona
from mi_primer_paquete.modulo1 import *
from mi_primer_paquete.modulo2 import *
from mi_primer_paquete import modulo1
from mi_primer_paquete import modulo2


modulo2.hola_mundo()

persona1 = modulo1.Persona("Juan", "Perez", 30)
print(persona1)


hola_mundo()
hola_mundo2()
persona1 = Persona("Juan", "Perez", 30)


def hola_mundo():
    print("¡Hola, mundo desde el main")


hola_mundo()
hola_mundo2()
persona1 = Persona("Juan", "Perez", 30)
print(persona1)
