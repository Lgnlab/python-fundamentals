"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostar o tempo que falta ou que passou do prazo.
"""

from datetime import date 

ano_atual = date.today().year
ano_nascimento = int(input("Informe o ano de nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}")

if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    print(f"Você ainda não tem 18 anos. Ainda faltam {18 - idade} anos para o alistamento")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos")