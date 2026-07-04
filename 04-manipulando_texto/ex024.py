"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

inicio = False
cidade = str(input("Informe o nome da cidade: ")).lower()
procurando = cidade.find("santo")
if procurando == 0:
    inicio = True
    print(f"A cidade começa com a palavra 'santo'? {inicio}")
else:
    print(f"A cidade começa com a palavra 'santo'? {inicio}")