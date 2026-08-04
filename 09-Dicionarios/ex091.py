"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.Guarde esses resultados em um dicionário.No final,coloque esse dicionário em ordem,sabendo que o vencedor tirou o maior número no dado.
"""
import random

dicionario = {}

for contador in range(1, 5):
    dicionario[f"jogador {contador}"] = random.randint(1, 6)

dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1]))

for k, v in dicionario_ordenado.items():
    print(f"{k} - {v}")