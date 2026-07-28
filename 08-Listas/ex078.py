"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
numeros = []

for contador in range(1, 6):
    numeros.append(int(input(f"Informe o {contador}ª valor: ")))

maior_valor = max(numeros)
menor_valor = min(numeros)

print(f"Maior valor: {maior_valor} no índice {numeros.index(maior_valor)+1}\nMenor valor: {menor_valor} no índice {numeros.index(menor_valor)+1}")