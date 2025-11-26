#ORGANIGRAMA
from calendar import month
from datetime import datetime, timedelta
def diasiguiente(fecha):
    fecha2 = fecha+timedelta(days=1)
    print(f"mañana sera {fecha2.strftime("%d-%m-%Y")}")
fecha = datetime(year=int(input("Escriba el año\n")),month=int(input("Escribe el mes\n")),day=int(input("Escribe el dia\n")))
diasiguiente(fecha)