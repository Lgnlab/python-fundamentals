"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

while True:
    sexo = str(input("Informe o sexo[M/F]:")).strip().upper()[0]
    if sexo in "MF":
        break