"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = str(input("Informe seu nome completo: ")).lower().strip()
print(f"Seu nome tem Silva? {'silva' in nome}")