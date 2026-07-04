"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos separados.
"""

numero = int(input("Informe um número de 0 a 9999: "))
transformando = str(numero)
print(f"Unidade: {transformando[3]} - Dezena: {transformando[2]} - Centena: {transformando[1]} - Milhar: {transformando[0]}")