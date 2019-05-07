
from functools import reduce

def doble(c):
    return c+c

lista = [1, 3, -1, 15, 9, 2]


listaDobles = map(lambda x: x*2, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)

listaReduc = reduce(lambda x,y: x + y, lista)

print(listaPares)

