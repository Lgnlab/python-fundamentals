# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 

salario = float(input("Salário R$"))
aumento = salario * 0.15
print(f"Salário antigo: R${salario:.2f}\n15% de aumento: R${aumento:.2f}\nNovo salário: R${aumento + salario:.2f}")