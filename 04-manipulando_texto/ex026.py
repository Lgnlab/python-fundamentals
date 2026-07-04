"""
Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A".
-Em que posição ela aparece a primeira vez.
-Em que posição ela aparece a útima vez.
"""

frase = str(input("Informe uma frase: ")).strip().lower()
print(f"Total de letra(s) A: {frase.count('a')}\nA primeira letra A apareceu na posição: {frase.find('a')+1}\nA ultima letra A apareceu na posição: {frase.rfind('a')+1}")
