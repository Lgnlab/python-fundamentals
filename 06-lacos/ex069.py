"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
"""
maior_idade = homens = mulhres_vinte = 0

while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]
    if idade > 18:
        maior_idade+= 1
    if sexo == "M":
        homens+= 1
    if idade < 20 and sexo == "F":
        mulhres_vinte+= 1
    sair = str(input("Quer continuar cadastrando[S/N]? ")).strip().upper()[0]
    if sair == "N":
        break

print(f"Pessoas maiores de 18 anos: {maior_idade}\nHomens cadastrados: {homens}\nMulheres com menos de 20 anos: {mulhres_vinte}")