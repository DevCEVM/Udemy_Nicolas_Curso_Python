class MiPerro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


mi_perro = MiPerro("Chanchito", 1)
mi_perro.habla()
