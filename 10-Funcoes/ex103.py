"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:o nome de um jogador e quantos gols ele marcou.O programa deverá ser capaz de mostrar a ficha do jogador,mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(nome = "<desconhecido>", gols = 0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


jogador = str(input("Nome do jogador: "))
gols_feitos = str(input("Número de Gols: "))
if gols_feitos.isnumeric():
    gols_feitos = int(gols_feitos)
else:
    gols_feitos = 0
if jogador.strip() == '':
    ficha(gols=gols_feitos)
else:
    ficha(jogador, gols_feitos)