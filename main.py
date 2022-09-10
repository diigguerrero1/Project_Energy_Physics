# Esta libreria nos permite manipular el Sistema Operativo
import os

# Este modulo tiene los objetos matematicos que usaremos para obtener la energia cinetica y la altura.
from math_objects import Energia_cinetica, Altura_sacada_de_energia_potencial



# Esta funcion inicializa el programa:

def beggining():
    print("""Bienvenido a este conversor de velocidad, valore su vida.""")

    masa = int(input("Ingrese su peso en kg: "))
    velocidad = int(input("Ingrese la velocidad en Km/h: "))

    return masa, velocidad


if __name__ == "__main__":
    os.system("clear")

    masa, velocidad = beggining()
    energia = Energia_cinetica(velocidad, masa)
    altura = Altura_sacada_de_energia_potencial(energia=energia.energia_cinetica, masa=masa)

    msj_salvacion = "¡Te salvaste!"
    msj_muerte = "¡Game Over!"
    if altura.altura < 5:
        print(f'Si te estrellas a {velocidad} km/h, tendras una energia potencial de {round(energia.energia_cinetica, 2)} Julios. Esto equivale a caer de un edificio de {altura.altura} metros de altura: {msj_salvacion}')
    else:
        print(f'Si te estrellas a {velocidad} km/h, tendras una energia potencial de {round(energia.energia_cinetica, 2)} Julios. Esto equivale a caer de un edificio de {altura.altura} metros de altura: {msj_muerte}')
