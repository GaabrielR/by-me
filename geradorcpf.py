from random import randint

numero = str(randint(100000000, 999999999))
acumulador1 = 0
acumulador2 = 0

indice = 0
for num, r in enumerate(range(10, 1, -1)):
    acumulador1 += int(numero[indice]) * r
    indice += 1

if 11 - (acumulador1 % 11) > 9:
    acumulador1 = 0
else:
    acumulador1 = (11 - (acumulador1 % 11))

numero = numero + str(acumulador1)

indice = 0
for num, r in enumerate(range(11, 1, -1)):
    acumulador2 += int(numero[indice]) * r
    indice += 1

if 11 - (acumulador2 % 11) > 9:
    acumulador2 = 0
else:
    acumulador2 = (11 - (acumulador2 % 11))

numero = numero + str(acumulador2)

print(numero[0:3] + '.' + numero[3:6] + '.' + numero[6:9] + '-' + numero[9:])
