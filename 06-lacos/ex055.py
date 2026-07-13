"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior_peso = menor_peso = 0

for contador in range(1, 6):
    peso = float(input(f"{contador}ª Peso: "))
    if contador == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
        
print(f"Maior peso digitado: {maior_peso:.1f}kg\nMenor peso digitado: {menor_peso:.1f}kg")