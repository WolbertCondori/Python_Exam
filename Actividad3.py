def multiplo(numero,i):
    correcto = 1
    while correcto != 0:
            print(f"{numero} multiplicado por {i} es ?\n")
            respuesta = int(input())
            if numero * i != respuesta:
                print("Incorrecto, programa terminado")
                print(f"Conseguiste {i-1} puntos")
                break
            else:
                print("Correcto")
                i = i + 1
multiplo(numero=int(input("escribe un numero\n")),i=int(input("desde donde quiere multiplicar ?\n")))