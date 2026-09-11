"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
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


def resumo(preço=0, taxa=10, taxa2=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preço)}")
    print(f"Dobro do preço: \t{dobro(preço, True)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"{taxa}% aumento: \t{aumentar(preço, taxa, True)}")
    print(f"{taxa2}% redução: \t{diminuir(preço, taxa2, True)}")
    print("-" * 30)