"""
CPF = 168.995.350-09
---------------------------------------------
1 * 10 = 10           #  1 * 11 = 11
6 * 9  = 54           #  6 * 10 = 60
8 * 8  = 64           #  8 * 9  = 72
9 * 7  = 63           #  9 * 8  = 72
9 * 6  = 54           #  9 * 7  = 63
5 * 5  = 25           #  5 * 6  = 30
3 * 4  = 12           #  3 * 5  = 15
5 * 3  = 15           #  5 * 4  = 20
0 * 2  = 0            #  0 * 3  = 0
                      #->0 * 2  = 0
         297          #           343
11 - (297 % 11) = 11  #  11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #  Digito 2 = 9
---------------------------------------------
"""

cpf = input("Digite seu CPF: ")
novo_cpf = ''
acumulador1 = 0
acumulador2 = 0

for num in cpf:
    if num.isnumeric():
        novo_cpf += num

if len(novo_cpf) == 11:
    indice = 0
    for num, r in enumerate(range(10, 1, -1)):
        acumulador1 += int(novo_cpf[indice]) * r
        indice += 1

    indice = 0
    for num, r in enumerate(range(11, 1, -1)):
        acumulador2 += int(novo_cpf[indice]) * r
        indice += 1

    if 11 - (acumulador1 % 11) > 9:
        acumulador1 = 0
    else:
        acumulador1 = (11 - (acumulador1 % 11))

    if 11 - (acumulador2 % 11) > 9:
        acumulador2 = 0
    else:
        acumulador2 = (11 - (acumulador2 % 11))

    if acumulador1 == int(novo_cpf[-2]) and acumulador2 == int(novo_cpf[-1]):
        print("O CPF digitado é válido.")
    else:
        print("O CPF digitado é inválido.")

else:
    print("Digite o CPF com 11 números.")
