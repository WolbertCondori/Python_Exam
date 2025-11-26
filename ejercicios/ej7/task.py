class Task:
    def __init__(self,title,priority,completed=False):
        self.__title=self.validarTitle(title)
        self.__priority=self.validarPriority(priority)
        self.__completed=completed

    def __str__(self):
        return f"{self.__title} — Prioridad: {self.__priority} — Estado: {"Pendiente" if not self.__completed else "Completado"}"

    def mark_done(self):
        self.__completed=True



    @staticmethod
    def validarTitle(title):
        if title != "":
            return title
        else:raise ValueError("Titulo no valido")

    @staticmethod
    def validarPriority(priority):
        if 0<priority>=5:
            return priority
        else:raise ValueError("La Prioridad salio del rango")