import itertools

dado = range(1,7)

conteo = 0

for x,y in itertools.product(dado,dado):
    suma = x+y
    if suma<=6:
        conteo +=1

print(conteo)