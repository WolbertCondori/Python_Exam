import random

def pintarcuadrado (longitud,simbolos):
    print(simbolos*longitud)
    for i in range(1,longitud-1):
        print(simbolos+" "*(longitud-2)+simbolos)
    print(simbolos*longitud)

pintarcuadrado(longitud=int(input("Escriba la longitud\n")),simbolos= chr(random.randint(169,223)))