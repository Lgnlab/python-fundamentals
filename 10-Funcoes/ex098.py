"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:inicio, fim e passo.Seu programa tem que realizar três contagens através da funçao criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada
"""

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if inicio < fim and passo < 0:
        passo = abs(passo) # abs = valor absoluto
    if inicio > fim and passo > 0:
        passo = -passo

    print("-" * 30)
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:")

    if passo > 0:
        fim_ajustado = fim + 1
    else:
        fim_ajustado = fim - 1

    for i in range(inicio, fim_ajustado, passo):
        print(f"{i} ", end="", flush=True)  # flush=True -> exibe a saída na tela de imediato
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)

print("-" * 30)
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim:    "))
pas = int(input("Passo:  "))

contador(ini, fim, pas)