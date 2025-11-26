numeros =[]
numPares=[]
numInpares=[]
def operacion(numeros):
    for i in range(10):
        numeros.append(int(input(f"Ingrese el numero que ira en la posicion {i}\n")))
        if (len(numeros)-1)%2==0:
            numPares.append(numeros[i])
        else:
            numInpares.append(numeros[i])
    print(f" la media de las posiciones pares serian {sum(numPares)//len(numPares)}")
    print(f"la media de las posiciones inpares seria {sum(numInpares)//len(numInpares)}")
operacion(numeros)