from concurrent.futures.process import _chain_from_iterable_of_lists


suma = 0
num = 4
for i in range(num):
    calificacion = float(input())
    suma = suma + calificacion
