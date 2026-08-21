"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

import datetime

def voto(nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - nascimento
    if idade < 16:
        return f"Com {idade} anos: NEGADO"
    elif idade <= 17 or idade >= 70:
        return f"Com {idade} anos: OPCIONAL"
    else:
        return f"Com {idade} anos: OBRIGATÓRIO"


ano = int(input("Em que ano você nasceu? "))
print(voto(ano))