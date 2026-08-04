"""
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
time = list()
dados = {}
partidas = []
while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    tot = int(input(f"Quantas partidas {dados["nome"]} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"   Quantos gols na partida {c}? ")))
    dados["gols"] = partidas[:]
    dados["total"] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == "N":
        break
print("-=" * 30)
print("cod ", end="")
for i in dados.keys():
    print(f"{i:<15}", end="")
print()
print("-" * 40)