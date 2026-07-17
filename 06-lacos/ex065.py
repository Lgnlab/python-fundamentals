"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
soma = cont_numero = 0
maior = menor = 0

while True:
    numero = int(input("Informe um número: "))
    soma += numero
    cont_numero += 1
    if cont_numero == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    sair = str(input("Quer informar outro valor[S/N]? ")).strip().upper()[0]
    if sair == "N":
        break

print(f"Média dos valores digitados: {soma / cont_numero:.1f}\nMaior valor lido: {maior}\nMenor valor lido: {menor}")