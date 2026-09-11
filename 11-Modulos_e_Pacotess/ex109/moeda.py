"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por eles vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato == False else moeda(preço)


def diminuir(preço, taxa, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato == False else moeda(preço)


def dobro(preço, formato=False):
    res = preço * 2
    return res if formato == False else moeda(preço)


def metade(preço, formato=False):
    res = preço / 2
    return res if formato == False else moeda(preço)


def moeda(preço = 0, moeda = "R$"):
    return f"{moeda}{preço:.2f}".replace(".", ",")