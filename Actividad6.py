def Actividad(uno,dos):
        suma=str(uno+dos)
        if suma.endswith(suma[0]) and len(suma)>=2:
            print(f"la suma de tus numeros da {suma} y su primer y ultimo numero son iguales")
        else:
            print(f"la suma de tus dos numeros es {suma} y su primer y ultimo numero no son iguales \n"
                  f"o solo hay un dijito")
Actividad(uno=int(input("dime el primer numero\n")), dos=int(input("dime el segundo numero\n")))