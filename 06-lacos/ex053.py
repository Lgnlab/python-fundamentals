"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsidere os espaços.
"""

frase = str(input("Informe uma frase: ")).split().upper()
frase_junta = "".join(frase)
inverso = frase_junta[::-1]

if frase_junta == inverso:
    print(f"{frase_junta} e {inverso} são PALÍNDROMO!")
else:
    print(f"{frase_junta} e {inverso} NÃO É PALÍNDROMO!")