class Perro:
    def __init__(self, nombre, raza):
        self.__nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.__nombre} está ladrando.")

    def comer(self, comida):
        print(f"{self.__nombre} está comiendo {comida}.")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


mi_perro = Perro("Rex", "Labrador")  # Perro.__init__(Rex, Labrador)
# print(mi_perro.nombre)
mi_perro.comer("croquetas")  # Imprime: Rex está comiendo croquetas.
mi_perro.ladrar()  # Imprime: Rex está ladrando.


# print(mi_perro.__raza)

print(mi_perro._Perro__nombre)
mi_perro._Perro__nombre = "Rocky"
# print(mi_perro.nombre)
# print(mi_perro.__nombre)

print(mi_perro.get_nombre())   # Acceso a la variable privada __raza
mi_perro.set_nombre("Max")  # Cambiando el nombre del perro
print(mi_perro.get_nombre())


######################################################################

class Animal:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.__especie = especie

    def comer(self, comida):
        print(f"{self.nombre} está comiendo {comida}.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def hacer_sonido(self):
        print(f"{self.nombre} está haciendo un sonido.")

    def respirar(self):
        print(f"{self.nombre} está respirando.")


class Gato(Animal):

    def __init__(self, nombre, color):
        super().__init__(nombre, "Gato")
        self.color = color

    def hacer_sonido(self):
        print(f"{self.nombre} está maullando.")

    def rascar(self):
        print(f"{self.nombre} está rascando el sofá.")


class Perro(Animal):

    def __init__(self, nombre, raza):
        super().__init__(nombre, "Perro")
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} está ladrando.")


class Pajaro(Animal):

    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)

    def hacer_sonido(self):
        print(f"{self.nombre} está cantando.")


mi_animal = Animal("Luna", "Perro")
mi_animal.comer("hueso")  # Imprime: Luna está comiendo hueso.
mi_animal.dormir()  # Imprime: Luna está durmiendo.
mi_animal.hacer_sonido()  # Imprime: Luna está haciendo un sonido.


mi_gato = Gato("Manchitas", "Gris")
mi_gato.comer("pescado")  # Imprime: Miau está comiendo pescado.
mi_gato.dormir()  # Imprime: Miau está durmiendo.
mi_gato.hacer_sonido()  # Imprime: Miau está maullando.
mi_gato.rascar()  # Imprime: Miau está rascando el sofá.
mi_gato.respirar()  # Imprime: Miau está respirando.
print(mi_gato.color)  # Imprime: Manchitas
