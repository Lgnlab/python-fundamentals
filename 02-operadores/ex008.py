# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Distância em metros: "))
print(f"{medida}m para centímetros: {medida * 100:.0f}cm\n{medida}m para milímetros: {medida * 1000:.0f}mm")