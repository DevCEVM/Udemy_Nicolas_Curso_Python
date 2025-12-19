numeros = [2, 45, 56, 4, 41, 50, 7, 39, 155]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


usuarios.sort(key=lambda el: el[1])
print(usuarios)
