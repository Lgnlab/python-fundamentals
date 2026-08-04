"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.No final, mostre:
A) Quantas pessoas cadastradas
B) A média de idade
"""

dados = {}
lista = []
cadastro = idade = 0

while True:
    dados["nome"] = str(input("Nome: "))
    dados["sexo"] = str(input("Sexo[M/F]: ")).strip().upper()[0]
    dados["idade"] = int(input("Idade: "))
    idade+= dados["idade"]
    cadastro+= 1
    lista.append(dados)
    sair = str(input("Quer cadastrar outra pesso[S/N]? ")).strip().upper()[0]
    if sair == "N":
        break

print(f"Pessoas cadastradas: {cadastro}\nMédia de idade: {idade / len(lista)}")