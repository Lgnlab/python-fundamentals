"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
soma = 0

while True:
    numero = int(input("Informe um número: "))
    if numero == 999:
        break
    else:
        soma+= numero
print(f"Soma dos números digitados: {soma}")