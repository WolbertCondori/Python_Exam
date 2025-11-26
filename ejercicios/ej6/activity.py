from user import User


class Activity:
    def __init__(self,user,tipe,duration):
        self.__user=self.validarUser(user)
        self.__tipe=self.validarType(tipe)
        self.__duration = self.validarduration(duration)

    def __str__(self):
        return f"“Actividad: {self.__tipe} — Usuario: {self.__user} — Duración: {self.__duration} min”"

    @property
    def duration(self):
        return self.__duration
    @property
    def user(self):
        return self.__user

    @duration.setter
    def duration(self,duration):
        self.__duration=duration

    @staticmethod
    def validarUser(user):
        if type(user) == User:
            return user
        else:raise ValueError("Usuario no valido")

    @staticmethod
    def validarType(tipe):
        types = ["login", "compra", "comentario"]
        if tipe in types:
            return tipe
        else:
            raise ValueError("tipo no valido")

    @staticmethod
    def validarduration(duration):
        if duration > 0:
            return duration
        else:
            raise ValueError("duracion no valido")

