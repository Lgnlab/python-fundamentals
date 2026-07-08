"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal 
-25 até 30: Sobrepeso
-30 até 40: Obsidade 
-Acima de 40: Obsidade mórbida
"""

peso = float(input("Peso(kg): "))
altura = float(input("Altura: "))
imc = peso / (altura **2)

if imc < 18.5:
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif imc <= 25:
    print(f"IMC: {imc:.2f} - Peso ideal")
elif imc <= 30:
    print(f"IMC: {imc:.2f} - Sobrepeso")
elif imc <= 40:
    print(f"IMC: {imc:.2f} - Obsidade")
else:
    print(f"IMC: {imc:.2f} - Obsidade mórbida")