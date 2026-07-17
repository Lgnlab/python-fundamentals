"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura While.
"""

primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razão de uma PA: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1
print("FIM")