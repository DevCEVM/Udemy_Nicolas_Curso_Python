# El valor de la izquierda es la llave y sólo pueden ser Strings
# la derecha puede ser lo que sea y van separados por ":"
punto = {"x": 25, "y": 50}
print(punto)
print(punto["y"])


punto["z"] = 45
print(punto["z"])

# Esto lo haces para preguntar si existe la llave el diccionario que estás imprimiendo:
if "lala" in punto:
    print(punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# Esto es algo que de verdad verías en una empresa:
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:
    print(usuario["nombre"])
