def multiplo(numero,i):
    salir="salir"
    ok=""
    while salir != ok:
        print(f"{numero} multiplicado por {i} es ?\n")
        respuesta = input("Escriba su respuesta\n")
        if (numero * i) != int(respuesta):
            print("Incorrecto, programa terminado")
            print(f"Conseguiste {i-1} puntos")
            break
        else:
            print("Correcto")
            i = i + 1
        ok=input("desea Salir ? escribe salir *\n")
multiplo(int(input("escribe un numero que quiera multiplicar\n"))
         ,int(input("desde donde quiere multiplicar ?\n")))