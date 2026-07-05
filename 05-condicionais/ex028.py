"""
Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint

sorteio = randint(0, 5)
palpite = int(input("Escreva seu palpite de 0 a 5: "))

if palpite == sorteio:
    print("Parabéns! Você acertou.")
else:
    print(f"Você perdeu. Tente novamente! (Número escolhido: {sorteio})")