"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais 
-Escaleno: todos os lados diferentes
"""

reta_1 = int(input("Reta 1: "))
reta_2 = int(input("Reta 2: "))
reta_3 = int(input("Reta 3: "))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print("Um triângulo pode ser formado!")
    if reta_1 == reta_2 and reta_1 == reta_3:
        print("Triângulo EQUILÁTERO")
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print("Triângulo ISÓSCELES")
    elif reta_1 != reta_2 and reta_2 != reta_3:
        print("Triângulo ESCALENO")
else:
    print("Um triângulo não pode ser formado!")