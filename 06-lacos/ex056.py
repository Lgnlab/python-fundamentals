"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, moste:

-A média de idade do grupo
-Qual é o nome do homem mais velho
-Quantas mulheres têm menos de 20 anos
"""
soma = maior_idade = contador_mulheres = 0


for contador in range(1, 5):
    nome = str(input(f"Nome da {contador}ª pessoa: "))
    idade = int(input(f"Idade da {contador}ª pessoa: "))
    sexo = str(input(f"Sexo da {contador}ª pessoa[M/F]: ")).strip().upper()[0]
    soma += idade
    if idade < 20 and sexo == "F":
        contador_mulheres += 1
    if contador == 1 and sexo == "M":
        maior_idade = idade
        nome_maior = nome
    else:
        if idade > maior_idade and sexo == "M":
            maior_idade = idade
            nome_maior = nome


print(f"Média de idade: {soma / 4:.1f}\nO homem mais velhor tem {idade} anos e o se chama {nome_maior}\n{contador_mulheres} mulher(es) têm menos de 20 anos")
