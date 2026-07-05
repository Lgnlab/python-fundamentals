"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
"""

distancia = int(input("Informe a distância da viagem(km): "))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f"Valor da passagem de uma viagem de {distancia}km: R${passagem:.2f}")
else:
    passagem = distancia * 0.45
    print(f"Valor da passagem de uma viagem de {distancia}km: R${passagem:.2f}")