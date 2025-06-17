# Clase base 1
class Flyer:
    def fly(self):
        return "Puede volar."

# Clase base 2


class Swimmer:
    def swim(self):
        return "Puede nadar."

# Clase hija que hereda de ambas


class Duck(Flyer, Swimmer):
    def quack(self):
        return "Hace: ¡Cuac!"


# Uso
mi_pato = Duck()
print(mi_pato.fly())   # Puede volar.
print(mi_pato.swim())  # Puede nadar.
print(mi_pato.quack())  # Hace: ¡Cuac!
