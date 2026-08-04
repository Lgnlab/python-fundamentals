"""
Crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero,o dicionário receberá também o ano de contratação e o salário.Calcule e acrescente,além da idade,com quantos anos a pessoa vai se aposentar.
"""
from datetime import date 

dados = {}

dados["nome"] = str(input("Nome: "))
ano_nascimento = int(input("Ano de nascimento: "))
dados["idade"] = date.today().year - ano_nascimento
dados["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("Ano de contratação: "))
    dados["salário"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - date.today().year)
print("-=" * 30)
for k, v in dados.items():
    print(f"  - {k} tem o valor {v}")
    