"""
Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,respectivamente.Ao final, mostre o conteúdo das três listas geradas.
"""

lista_numeros = []
pares = []
impares = []

while True:
    lista_numeros.append(int(input("Informe um número: ")))
    sair = str(input("Quer continuar[S/N]? ")).strip().upper()[0]
    if sair == "N":
        break

for lista in lista_numeros:
    if lista % 2 == 0:
        pares.append(lista)
    else:
        impares.append(lista)

print(f"Lista completa: {lista_numeros}\nLista Ímpares: {impares}\nLista pares: {pares}")