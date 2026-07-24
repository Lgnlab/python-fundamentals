"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

import random 

numeros = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:")
for t in numeros:
    print(t, end=" ")
print()
print(f"Maior número gerado: {max(numeros)}\nMenor número gerado: {min(numeros)}")