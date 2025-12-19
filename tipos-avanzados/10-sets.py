# set significa grupo o conjunto

Primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)


# LO SIGUIENTE TE SERVIRÁ CUANDO TE DIGAN "CALCULA LA xxx ENTRE 2 SETS"

# Este operador se conoce como "Unión":
print(Primer | segundo)

# Este operador se conoce como "Intersección":
print(Primer & segundo)

# Este operador se conoce como"Diferencia":
print(Primer - segundo)

# Este operador se conoce como "Diferencia Simetrica":
print(Primer ^ segundo)

# En los sets no podemos acceder a los elementos en concreto como "segundo[0]"
# Pero sí puedo preguntarle si tiene un valor específico?:

if 7 in segundo:
    print(True)
else:
    print(False)
