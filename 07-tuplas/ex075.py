"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""
valores = ()

for contador in range(4):
    numero = int(input(f"{contador+1}ª Número: "))
    lista = list(valores)
    lista.append(numero)
    valores = tuple(lista)

print("Números pares digitados: ")
for i, v in enumerate(valores):
    if v % 2 == 0:
        print(v, end=" ")
print()

for indice, valor in enumerate(valores):
    if valor == 3:
        print(f"O número 3 foi digitado no índice {indice}")


print(f"Tupla completa: {valores}\nO número 9 apareceu {valores.count(9)} vez(es)")