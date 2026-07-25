import bisect

lista = [10,20,30,40]

indice = bisect.bisect_left(lista,20)

print(indice)