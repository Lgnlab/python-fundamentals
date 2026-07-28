"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em lista,já na posição correta de inserção.No final, mostre a lista ordenada na tela.
"""

lista_numeros = []

for contador in range(1,6):
    lista_numeros.append(int(input(f"Informe o {contador}ª valor: ")))

lista_numeros.sort()
print(f"Lista ordenada: {lista_numeros}")