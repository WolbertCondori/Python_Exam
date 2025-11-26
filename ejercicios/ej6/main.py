from functools import reduce
from random import randint

from activity import Activity
from user import User

users=[]
activitis=[]
users.append(User("pepe123","pepe@gmail.com",19))
users.append(User("pro333","promax@gmail.com",15))
users.append(User("juan666","juan@gmail.com",23))
for user in users:
    tipos=["login", "compra", "comentario"]
    activitis.append(Activity(user,tipos[randint(0,len(tipos)-1)],randint(5,25)))
usuariosActivos = list(filter(lambda activity:activity.user.active,activitis))
durationActivitis = list(map(lambda activity:activity.duration,activitis))
totalMinutos = reduce(lambda cont,activity:cont+activity.duration,activitis,0)
print(usuariosActivos)
print(durationActivitis)
print(totalMinutos)