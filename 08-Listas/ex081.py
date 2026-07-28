"""
Crie um programa que vai ler vários números e colocar em uma lista.Depois disso mostre:
A) Quantos números foram digitados
B) A lista dos valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista
"""

lista_numeros = []
cinco = False

while True:
    lista_numeros.append(int(input("Informe um número: ")))
    sair = str(input("Quer adicionar outro valor[S/N]: ")).strip().upper()[0]
    if sair == "N":
        break
if 5 in lista_numeros:
    cinco = True
lista_numeros.sort(reverse=True)

print(f"Foram digitados {len(lista_numeros)} números\nLista ordenada de forma decrescente {lista_numeros}\nO valor 5 está na lista: {cinco}")