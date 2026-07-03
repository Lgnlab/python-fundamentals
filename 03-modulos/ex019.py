"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import random

nomes = []

for cont in range(1, 5):
    nomes.append(input(f"{cont} Nome: "))

print(f"O escolhido foi: {random.choice(nomes)}")