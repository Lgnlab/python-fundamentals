"""
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista.No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
temp = []
dados = []
maior = menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso(kg): ")))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    sair = str(input("Quer cadastrar mais alguma pessoa[S/N]?  ")).strip().upper()[0]
    if sair == "N":
        break

print(f"Foram cadastradas {len(dados)} pessoa(s)\nO maior peso foi de {maior}Kg. Peso de ", end="")
for p in dados:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}Kg. Peso de ", end="")
for p in dados:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
print()