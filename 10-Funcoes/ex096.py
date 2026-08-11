"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(largura = 0, comprimento = 0):
    calculo = largura * comprimento
    return calculo


larg = int(input("Informe a largura(metros): "))
compri = int(input("Informe o comprimento(metros): "))
print(f"Área: {area(larg, compri)}m²")