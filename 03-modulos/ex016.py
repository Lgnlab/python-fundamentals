"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
"""

import math

numero = float(input("Informe um valor real: "))
print(f"{numero} -> {math.trunc(numero)}")