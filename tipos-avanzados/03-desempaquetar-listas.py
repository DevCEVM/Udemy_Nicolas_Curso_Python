numeros = [1, 2, 3]

# Esto es feo!!:
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Esto es bonito!!:
creo, que, ya = numeros

print(creo, que, ya)

creo, *otros = numeros
print(creo, otros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
veremos, esto, no,  *otros, va, funcionar, sisale = numeros
print(veremos, esto, no,  va, funcionar, sisale, otros)
