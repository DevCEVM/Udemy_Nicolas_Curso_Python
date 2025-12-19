numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
fir, sec, *otros = numeros
print(fir, sec, otros)
for n in numeros:
    print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "Esto no es muy elegante"
print(listaNumeros)
