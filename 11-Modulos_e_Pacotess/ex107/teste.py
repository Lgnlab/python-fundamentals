import moeda

preço = float(input("Digite o preço: R$"))
print(f"A metade de R${preço:.2f} é R${moeda.metade(preço):.2f}")
print(f"O dobro de R${preço:.2f} é R${moeda.dobro(preço):.2f}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preço, 10):.2f}")
print(f"Diminuindo 10%, temos R${moeda.diminuir(preço, 10):.2f}")