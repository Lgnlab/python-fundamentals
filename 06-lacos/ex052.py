"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

numero = int(input("Informe um número inteiro: "))
cont_divisor = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        cont_divisor += 1

if cont_divisor > 2:
    print(f"{numero} NÃO É PRIMO!")
else:
    print(f"{numero} É PRIMO!")