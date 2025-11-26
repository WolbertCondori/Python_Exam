#Quiniela a saber que es eso#
from random import randint
local=["Equipo local 1","Equipo local 2","Equipo local 3",
       "Equipo local 4","Equipo local 5","Equipo local 6"]
invitado=["Equipo invitado 1","Equipo invitado 2","Equipo invitado 3",
          "Equipo invitado 4","Equipo invitado 5","Equipo invitado 6"]
resultados=[]
def quinuela(respuestas):
    for i in range(len(local)):
        print("1 Para el equipo Local, 2 Para el equipo Visitante y X para el empate")
        print(f"{local[i]} vs {invitado[i]}")
        resultados.append(input("¿Quien gana?\n"))
    for i in range(len(resultados)):
        print(f"{local[i]} vs {invitado[i]} respuesta {resultados[i]}")

quinuela(print("quinuela"))