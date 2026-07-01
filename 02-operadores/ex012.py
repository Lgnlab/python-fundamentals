# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input("Valor do produto R$"))
desconto = produto - (produto * 0.05)
print(f"O produto custava R${produto:.2f} e vai ter 5% de desconto: R${desconto:.2f}")