"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 25 anos: SÊNIOR
-Acima: MASTER
"""

from datetime import date 

ano_atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = ano_atual - nascimento

if idade <= 9:
    print(f"{idade} anos - Atleta MIRIM")
elif idade <= 14:
    print(f"{idade} anos - Atleta INFANTIL")
elif idade <= 19:
    print(f"{idade} anos - Atleta JUNIOR")
elif idade <= 25:
    print(f"{idade} anos - Atleta SÊNIOR")
else:
    print(f"{idade} anos - Atleta MASTER")
    