class MiPerro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


MiPerro.habla()
perro1 = MiPerro("Chanchito", 2)
perro2 = MiPerro("Felipe", 3)
perro3 = MiPerro.factory()
print(perro3.edad, perro3.nombre)
