"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
"""
cont = 1

while cont <= 50:
    if cont % 2 == 0:
        print(cont, end=" ")
    cont += 1