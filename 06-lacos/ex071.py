"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

saque = int(input("Informe o valor a ser sacado: R$"))
montante = saque
cedula = 50
total_cedula = 0

while True:
    if montante >= cedula:
        montante-= cedula
        total_cedula+= 1
    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if montante == 0:
            break