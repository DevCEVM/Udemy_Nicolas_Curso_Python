# Esto es como utilizar la implementación de una lista solamente que estamos
# trabajando de forma lógica para que funcione como pila, y para que lo haga
# tenemos que utilizar el método de "append" y el método "pop"

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])
pila.pop()
pila.pop()
if not pila:
    print("pila vacía")
