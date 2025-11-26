from employe import Employee

try:
    e1 = Employee("juan", 100, 20)
    e2 = Employee("rodix", 20, 15)
    e3 = Employee("pepe", 125, 10)
    empleados = [e1, e2, e3]
    salarios = list(map(lambda emp:emp.priceHora*emp.horasTrabajadas ,empleados))
    print(salarios)
except ValueError as e:
    print(e)

