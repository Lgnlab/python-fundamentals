"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.Caso o número já exista lá dentro, ele não será adicionado.No final, serão exibidos todos os valores únicos digitados,em ordem crescente.
"""

lista_numeros = []

while True:
    numero = int(input("Digite um valor: "))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adiconar...")
    sair = str(input("Quer continuar? [S/N] "))
    if sair in "Nn":
        break

lista_numeros.sort()
print(f"Você digitou os valores {lista_numeros}")