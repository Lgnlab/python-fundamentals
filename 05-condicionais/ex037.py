"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal 
-3 para hexadecimal
"""

from rich import print

numero = int(input("Digite um número inteiro: "))
print("""
Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
""")
escolha = int(input("Sua opção: "))

if escolha == 1:
    conversao = bin(numero)
    tipo = "BINÁRIO"
    print(f"{numero} convertido para {tipo} é igual a {conversao[2:]}")
elif escolha == 2:
    conversao = oct(numero)
    tipo = "OCTAL"
    print(f"{numero} convertido para {tipo} é igual a {conversao}")
elif escolha == 3:
    conversao = hex(numero)
    tipo = "HEXADECIMAL"
    print(f"{numero} convertido para {tipo} é igual a {conversao[2:]}")
else:
    print("[red]OPÇÃO INVÁLIDA[/]. TENTE NOVAMENTE!")