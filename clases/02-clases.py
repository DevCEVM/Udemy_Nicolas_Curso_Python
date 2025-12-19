# el nombre de la clase siempre va en CamelCase
# las funciones dentro de una clase ya no se llaman funciones y se llaman métodos
# El primer parametro siempre SIEMPRE tiene que ser SELF

class MiPerro:
    def habla(self):
        print("Guau!")


mi_perro = MiPerro()
# El resultado del siguiente print es la especificación de que es una clase
# se llama "MiPerro" y es del módulo "main" (los módulos son de otra clase más adelante)
print(type(mi_perro))

# Más adelante te explican el por qué? pero así se imprime el método de una clase
# (Sin argumentos) sólamente se le pasan más argumentos si también se los pusiste en los
# parametros del método además del SELF (y a esto se le llama Instancia de la clase,
# que en este caso es MiPerro):
mi_perro.habla()

# Aquí podemos verificar si este objeto que creamos es instancia de alguna clase?:
# isinstance recibe 2 argumentos, el primero es el objeto y el segundo la clase
print(isinstance(mi_perro, MiPerro))
