"""
Faça um programa que leia nome e média de um aluno,guardando também a situação em um dicionário.No final,mostre o conteúdo da estrutura na tela.
"""

dados = {}

dados["nome"] = str(input("Nome: "))
dados["media"] = float(input("Média: "))
if dados["media"] >= 7:
    dados["situação"] = "Recuperação"
elif 5 <= dados["media"] < 7:
    dados["situação"] = "Recuperação"
else:
    dados["situação"] = "Reprovado"

for k, v in dados.items():
    print(f"  - {k} é igual a {v}")