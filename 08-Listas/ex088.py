"""
Faça um programa que ajude um jogador da mega sena a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,cadastrando tudo em uma lista composta.
"""

import random

jogos = int(input("Quantos jogos você quer gerar? "))
sorteio = []

for contador in range(1, jogos+1):
    sorteio.append(sorted(random.sample(range(1, 61), 6)))

print("Palpites gerados:")
for lista in sorteio:
    print(lista)