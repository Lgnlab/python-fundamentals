"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.No final, mostre os valores pares e ímpares em ordem crescente.
"""

valores = [[], []]
contador = 1

while contador <= 7:
    numero = int(input(f"{contador}ª valor: "))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
    contador+= 1

valores[0].sort()
valores[1].sort()
print()
print(f"Todos os valores: {valores}\nPares: {valores[0]}\nÍmpares: {valores[1]}")