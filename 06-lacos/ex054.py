"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

ano_atual = date.today().year
contador_maior = contador_menor = 0

for contador in range(1, 8):
    ano = int(input(f"Informe o {contador}ª ano de nascimento: "))
    idade = ano_atual - ano
    if idade >= 18:
        contador_maior += 1
    else:
        contador_menor += 1

print(f"{contador_maior} pessoa(s) já são maior(es) de idade e {contador_menor} pessoa(s) não atingiram a maioridade.")