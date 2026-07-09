"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

termo = int(input("Primeiro Termo: "))
razao = int(input("Razão de uma PA: "))
decimo = termo + (10 - 1) * razao

for contador in range(termo, decimo + razao, razao):
    print(f"{contador}", end=" -> ")
print("FIM")