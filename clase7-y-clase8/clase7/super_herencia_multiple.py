class Animal:
    def __init__(self, nombre, especie, peso):
        self.nombre = nombre
        self.especie = especie
        self.peso = peso

    def mover(self):
        return f"{self.nombre} se está moviendo."

    def dormir(self):
        return f"{self.nombre} está durmiendo."

    def alimentarse(self):
        return f"{self.nombre} está buscando comida."

    def __str__(self):
        return f"{self.nombre} es un {self.especie} que pesa {self.peso} kg."


class Mamifero(Animal):
    def __init__(self, nombre, especie, peso, pelaje="corto"):
        super().__init__(nombre, especie, peso)
        self.pelaje = pelaje

    def amamantar(self):
        return f"{self.nombre} está amamantando a sus crías."

    def __str__(self):
        return f"{self.nombre} es un mamífero de especie {self.especie}, tiene pelaje {self.pelaje}, y pesa {self.peso} kg."


class AnimalMarino(Animal):
    def __init__(self, nombre, especie, peso, habitat="océano"):
        super().__init__(nombre, especie, peso)
        self.habitat = habitat

    def nadar(self):
        return f"{self.nombre} está nadando en el {self.habitat}."

    def respirar(self):
        return f"{self.nombre} está respirando aire, aunque vive en el agua."

    def __str__(self):
        return f"{self.nombre} es un animal marino de especie {self.especie}, vive en {self.habitat}, y pesa {self.peso} kg."


class Cetaceo(Mamifero, AnimalMarino):
    def __init__(self, nombre, especie, peso, pelaje, habitat="océano", profundidad_maxima=1000, edad=10):
        # Inicializar Mamifero primero
        Mamifero.__init__(self, nombre, especie, peso, pelaje)
        # Luego inicializar AnimalMarino
        AnimalMarino.__init__(self, nombre, especie, peso, habitat)

        self.profundidad_maxima = profundidad_maxima
        self.edad = edad

    def comunicarse(self):
        return f"{self.nombre} emite sonidos para comunicarse."

    def bucear(self):
        return f"{self.nombre} puede bucear hasta una profundidad de {self.profundidad_maxima} metros."

    def reproducirse(self):
        return f"{self.nombre} está buscando pareja para reproducirse."

    def comparar_peso(self, otro_cetaceo):
        if self.peso > otro_cetaceo.peso:
            return f"{self.nombre} es más pesado que {otro_cetaceo.nombre}."
        elif self.peso < otro_cetaceo.peso:
            return f"{self.nombre} es más liviano que {otro_cetaceo.nombre}."
        else:
            return f"{self.nombre} y {otro_cetaceo.nombre} tienen el mismo peso."

    def __str__(self):
        return (
            f"{self.nombre} es un cetáceo de especie {
                self.especie}, tiene pelaje {self.pelaje}, "
            f"vive en el {self.habitat}, puede bucear a {
                self.profundidad_maxima} metros de profundidad, "
            f"pesa {self.peso} kg, y tiene {self.edad} años."
        )


# Instanciamos la clase Cetáceo
cetaceo1 = Cetaceo("Ballena", "Balaenidae", 40000, "grueso")
cetaceo2 = Cetaceo("Delfín", "Delphinidae", 200, "corto")

# Probamos los métodos
print(cetaceo1.mover())         # Heredado de Animal
print(cetaceo1.amamantar())     # Heredado de Mamífero
print(cetaceo1.nadar())         # Heredado de AnimalMarino
print(cetaceo1.comunicarse())   # Definido en Cetáceo
print(cetaceo1.bucear())        # Definido en Cetáceo
print(cetaceo1.dormir())        # Heredado de Animal
print(cetaceo1.alimentarse())   # Heredado de Animal

# Comparación de peso
print(cetaceo1.comparar_peso(cetaceo2))

# Reproducción
print(cetaceo1.reproducirse())  # Definido en Cetáceo

# Usamos __str__ para una representación amigable del objeto
print(cetaceo1)
print(cetaceo2)
