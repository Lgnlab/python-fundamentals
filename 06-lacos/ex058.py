"""
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

tentativas = 0

sorteio = randint(0, 10)
while True:
    palpite = int(input("Escreva seu palpite de 0 a 10: "))
    tentativas += 1
    if palpite == sorteio:
        break

print(f"Você acertou com {tentativas} palpites.")