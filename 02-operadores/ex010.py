""" 
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$1,00 = R$5,18
"""

reais = float(input("Valor em reias(R$) "))
dolares = reais / 5.18
print(f"Você consegue comprar US${dolares:,.2f}")
