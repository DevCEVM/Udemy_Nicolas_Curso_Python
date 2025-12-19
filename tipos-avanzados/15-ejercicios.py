from pprint import pprint

string = "Hola mundo este es mi string"


def no_space(texto):
    return [char for char in texto if char != " "]


def conteo(lista):
    char_dict = {}
    for char in lista:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = no_space(string)
cuenta_caracteres = conteo(sin_espacios)
ordenados = ordena(cuenta_caracteres)
Tupla_maxima = mayores_tuplas(ordenados)
mensaje = crea_mensaje(Tupla_maxima)
print(mensaje)
