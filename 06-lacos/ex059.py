"""
Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

maior = 0

valor_1 = int(input("Valor 1: "))
valor_2 = int(input("Valor 2: "))

while True:
    operacao = int(input("Escolha uma operação: "))

    if operacao == 1:
        soma = valor_1 + valor_2
        print(f"{valor_1} + {valor_2} = {soma}")
    elif operacao == 2:
        multiplicar = valor_1 * valor_2
        print(f"{valor_1} x {valor_2} = {multiplicar}")
    elif operacao == 3:
        if valor_1 > valor_2:
            maior = valor_1
        else:
            maior = valor_2
        print(f"Maior número digitado: {maior}")
    elif operacao == 4:
        valor_1 = int(input("Valor 1: "))
        valor_2 = int(input("Valor 2: "))
    elif operacao == 5:
        break