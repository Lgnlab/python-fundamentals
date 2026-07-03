"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import random

nomes = []

for cont in range(1, 5):
    nomes.append(input(f"Nome {cont}: "))

random.shuffle(nomes)
print(f"Ordem de apresentação: {nomes}")