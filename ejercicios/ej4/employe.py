class Employee:
    def __init__(self,nombre,horasTrabajadas,priceHora):
        self.__nombre = self.verificarNombre(nombre)
        self.__horasTrabajadas = self.verificarHoras(horasTrabajadas)
        self.__priceHora = self.verificarPriceHora(priceHora)

    def __str__(self):
        return f"Nombre: {self.__nombre} Gano {self.__horasTrabajadas*self.__priceHora}€ en el mes"



    @property
    def horasTrabajadas(self):
        return self.__horasTrabajadas

    @property
    def nombre(self):
        return self.__nombre

    @property
    def priceHora(self):
        return self.__priceHora


    @staticmethod
    def verificarNombre(nombre):
        if not nombre == "" and not nombre.isnumeric():
            return nombre
        else: raise ValueError("Nombre no valido")

    @staticmethod
    def verificarHoras(horasTrabajadas):
        if 0 < horasTrabajadas <= 200 and isinstance(horasTrabajadas,int):
            return horasTrabajadas
        else: raise ValueError("Horas de Trabajo no validas")
    @staticmethod
    def verificarPriceHora(priceHora):
        if priceHora > 5 and isinstance(priceHora,int):
            return priceHora
        else:raise ValueError("Precio muy bajo")
