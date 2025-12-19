# El constructor es una función que nosotros podemos definir dentro de cada una
# de las clases de absolutamente todas las clases que creas y este se va a ejecutar
# siempre absolutamente siempre que crees una nueva instancia de la clase:

# SELF es una palabra reservada que se encuentra dentro de todas las clases que hay
# en python y se utilizan para referenciar las instancias de las clases
class MiPerro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

# Este código es antes de transformar el string a string formateado (el del segundo método)
# mi_perro = MiPerro("Chanchito")
# mi_perro2 = MiPerro("Felipe")
# print(mi_perro.nombre)
# print(mi_perro2.nombre)


mi_perro = MiPerro("Chanchito", 1)
mi_perro.habla()
