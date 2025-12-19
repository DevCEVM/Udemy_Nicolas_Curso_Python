mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito", "Tifa", "Jaina", "Thrall"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas)
print(mascotas[2:])
print(mascotas[-2])
# Este es para número pares:
print(mascotas[::2])
# Este es para números inpares:
print(mascotas[1::2])
print(mascotas[1:4:2])


numeros = list(range(21))
print(numeros[1::2])

numeros = list(range(1, 21))
print(numeros[::2])
