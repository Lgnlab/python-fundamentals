"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode excerder 30% do salário ou então o empréstimo será negado.
"""
from rich import print


valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe o seu salário: R$"))
anos = int(input("Tempo de financiamento(anos): "))

meses = anos * 12
parcela_mensal = valor_casa / meses
analise = salario * 0.3

if parcela_mensal > analise:
    print(f"[red]NEGADO![/] O valor da parcela de R${parcela_mensal:.2f} excede 30%(R${analise:.2f})do seu salário R${salario:.2f}")
else:
    print(f"[green]APROVADO![/]\nValor da parcela mensal: R${parcela_mensal:.2f}")