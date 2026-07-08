"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: 10% de desconto
-À vista no cartão: 5% de desconto 
-Em até 2x no cartão: preço normal 
-3x ou mais no cartão: 20% de juros
"""

valor_produto = float(input("Preço do produto: R$"))
print("""
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto 
[ 3 ] Em até 2x no cartão: preço normal 
[ 4 ] 3x ou mais no cartão: 20% de juros
""")
escolha = int(input("Escolha a forma de pagamento: "))

if escolha == 1:
    calculo = valor_produto * 0.1 
    print(f"Total com 10% de desconto: R${valor_produto - calculo:.2f}")
elif escolha == 2:
    calculo = valor_produto * 0.05 
    print(f"Total com 5% de desconto: R${valor_produto - calculo:.2f}")
elif escolha == 3:
    calculo = valor_produto / 2
    print(f"Total: R${valor_produto:.2f}\nValor da parcela em 2x: R${calculo:.2f}")
elif escolha == 4:
    calculo = valor_produto * 0.2 + valor_produto
    print(f"Total com 20% de juros: R${calculo:.2f}\nValor da parcela em 3x: R${calculo / 3:.2f}")