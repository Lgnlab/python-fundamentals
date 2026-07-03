"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math

angulo = float(input("Informe o ângulo: "))
angulo_radianos = math.radians(angulo)
print(f"Seno: {math.sin(angulo_radianos):.2f}\nCosseno: {math.cos(angulo_radianos):.2f}\nTangente: {math.tan(angulo_radianos):.2f}")