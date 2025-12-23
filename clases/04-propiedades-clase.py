class MiPerro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


MiPerro.patas = 3
mi_perro = MiPerro("Chanchito", 1)
mi_perro.patas = 5
mi_perro2 = MiPerro("Felipe", 1)
mi_perro2.patas = 8
print(MiPerro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
