from functools import reduce

from food import Food

try:
    f1 = Food("leche",50,500)
    f2 = Food("dona",250,150)
    foods = [f1,f2]
    vgaCaloris = reduce(lambda cont,food:(food.calorias*food.cantidad)/100,foods)
    print(vgaCaloris)
except ValueError as e:
    print(e)