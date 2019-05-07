
from functools import reduce

def doble(c):
    return c+c

def esPar(x):
    return x % 2 == 0

lista = [1, 3, -1, 15, 9]


listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 =map(esPar,lista)

sumatorio = reduce(lambda x,y: x + y, lista)
sumaDoble = reduce(lambda x,y: x + y * 2, lista)

sumaCien = reduce(lambda x,y : x + y, range(101))



print(list(listaDobles))
print(list(listaDobles))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumaDoble)

print(sumaCien)