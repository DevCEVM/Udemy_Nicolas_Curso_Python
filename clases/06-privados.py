class MiPerro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = MiPerro.factory()
perro1.habla()
print(perro1.get_nombre())

# Esto se supone que no debes hacerlo porque por algo estamos volviendo privadas las
# las propiedades y/o métodos, estos 2 guiones bajos son para hacerle saber tanto a
# compañeros como a nosotros mismos que estos valores son privados. pero si de plano
# quieres acceder a estas propiedades privadas de los objetos es así (Pero no lo hagas):
print(perro1.__dict__)
