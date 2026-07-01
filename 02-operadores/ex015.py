""" 
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
"""

distancia = int(input("Km total percorrido: "))
dias = int(input("Quantos dias de aluguel? "))
total = (dias * 60) + (distancia * 0.15)
print(f"Valor total: R${total:.2f}")