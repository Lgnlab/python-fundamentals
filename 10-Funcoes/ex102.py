"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(numero = 1, show = False):
    fat = 1
    for cont in range(numero, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat*=cont
    return fat


print(fatorial(5, show=True))