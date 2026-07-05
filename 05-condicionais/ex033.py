"""
Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
"""

numero_1 = int(input("Primeiro número: "))
numero_2 = int(input("Segundo número: "))
numero_3 = int(input("Terceiro número: "))

menor = numero_1

if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
elif numero_3 < numero_2 and numero_3 < numero_1:
    menor = numero_3 

maior = numero_1

if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
elif numero_3 > numero_2 and numero_3 > numero_1:
    maior = numero_3

print(f"Maior: {maior}\nMenor: {menor}")
