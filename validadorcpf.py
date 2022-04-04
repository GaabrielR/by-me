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
