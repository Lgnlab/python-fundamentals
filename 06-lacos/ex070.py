"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1.000
C) Qual é o nome do produto mais barato
"""
total_compra = produtos_mil = 0
produto_barato = " "
barato = caro = contador = 0

while True:
    nome_produto = str(input("Nome do produto: "))
    valor_produto = float(input("Valor do produto: R$"))
    total_compra+= valor_produto
    contador+= 1
    if valor_produto > 1000:
        produtos_mil+= 1
    if contador == 1:
        barato = valor_produto
        produto_barato = nome_produto
    else:
        if valor_produto < barato:
            barato = valor_produto
            produto_barato = nome_produto

    sair = str(input("Quer continuar[S/N]? ")).strip().upper()[0]
    if sair == "N":
        break

print(f"Total: R${total_compra:.2f}\n{produtos_mil} produto(s) custam mais de R$1.000\nNome do produto mais barato: {produto_barato}")