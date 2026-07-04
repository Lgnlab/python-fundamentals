"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas e minúsculas.
-Quantas letras ao todo (sem considerar espaços).
-Quantas letras tem o primeiro nome.
"""

nome = str(input("Nome Completo: "))
separando = nome.split()
total_letras = "".join(separando)
print(f"Nome em letras maiúsculas: {nome.upper()}\nNome em letras minúsculas: {nome.lower()}\nTotal de letras: {len(total_letras)}\nTotal de letras do primeiro nome: {len(separando[0])}")