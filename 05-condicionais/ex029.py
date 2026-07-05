"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
"""

velocidade = int(input("Velocidade(km/h): "))

if velocidade > 80:
    limite_ultrapassado = velocidade - 80
    multa = limite_ultrapassado * 7
    print(f"Você ultrapassou {limite_ultrapassado}km/h da velocidade permitida que é de 80km/h\nMulta: R${multa:.2f}")
else:
    print("Continue seguindo a velocidade recomendada")