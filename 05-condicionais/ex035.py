"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta_1 = int(input("Reta 1: "))
reta_2 = int(input("Reta 2: "))
reta_3 = int(input("Reta 3: "))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print("Um triângulo pode ser formado!")
else:
    print("Um triângulo não pode ser formado!")