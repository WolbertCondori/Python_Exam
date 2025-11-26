class Food:
    def __init__(self,nombre,calorias,cantidad):
        self.__nombre=self.verificarNombre(nombre)
        self.__calorias=self.verificarCalorias(calorias)
        self.__cantidad=self.verificarCantidad(cantidad)

    def __str__(self):
        return f"Nombre: {self.__nombre} Calorias: {self.__calorias} Cantidad: {self.__cantidad}gm"


    @property
    def nombre(self):
        return self.__nombre

    @property
    def calorias(self):
        return self.__calorias

    @property
    def cantidad(self):
        return self.__cantidad


    @staticmethod
    def verificarNombre(nombre):
        if nombre != "":
            return nombre
        else:raise ValueError("nombre no valido")

    @staticmethod
    def verificarCalorias(calorias):
        if calorias>0:
            return calorias
        else:raise ValueError("Calorias no validas")

    @staticmethod
    def verificarCantidad(cantidad):
        if 10 <= cantidad <= 500:
            return cantidad
        else:raise ValueError("cantidad no valida")