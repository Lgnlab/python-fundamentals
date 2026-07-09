"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0 

for contador in range(1, 7):
    numeros = int(input(f"{contador} Número: "))
    if numeros % 2 == 0:
        soma += numeros
print(f"Soma dos números PARES digitados: {soma}")