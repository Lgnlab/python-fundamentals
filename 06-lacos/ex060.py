"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

numero = int(input("Informe um número para ver o fatorial: "))
fatorial = 1
multiplicando = 1

while numero >= fatorial:
    multiplicando *= numero
    if numero > 1:
        print(numero, end="x")
    else:
        print(numero, end="=")
    numero -= 1
print(f"{multiplicando}")