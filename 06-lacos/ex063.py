"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
"""

numero = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
contador = 3
print(f"{t1} -> {t2}", end="") 

while contador <= numero:
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
    contador += 1
