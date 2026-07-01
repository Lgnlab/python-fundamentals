# Escreva um programa que converta uma temperatura digitada em °C e converta para °F

temperatura = float(input("Temperatura em °C: "))
convertendo = (temperatura * 9/5) + 32
print(f"{temperatura:.1f} °C -> {convertendo:.1f} °F")