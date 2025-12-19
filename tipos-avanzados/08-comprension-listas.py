usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# Esto es feo:{
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# }

# Esto sí está bonito:

# Esto es una transformación de datos:
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# Esto es filtrar datos:
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# Esto es filtrar y transformar datos:
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

# Esto es "map" y es exactamente lo mismo que trasformar datos, ambos están bien:
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# Esto es "filter" y es exactamente lo mismo que filtrar datos, ambos están bien:
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
