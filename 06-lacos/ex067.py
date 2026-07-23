"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    numero = int(input("Informe um número para ver sua tabuada: "))
    if numero < 0:
        break
    else:
        for contador in range(1, 11):
            print(f"{numero} x {contador} = {numero * contador}")
            