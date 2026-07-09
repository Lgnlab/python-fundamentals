"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

tabuada = int(input("Informe um número para ver sua tabuada: "))

for contador in range(1, 11):
    print(f"{tabuada} x {contador} = {tabuada * contador}")