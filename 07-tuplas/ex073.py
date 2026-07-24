"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Os 5 primeiros
B) Os últimos 4 colocados
C) Times em ordem alfabética 
D) Em que posição está o time da Chapecoense 
"""

times = ("Corinthias", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO")

print(f"Os 5 primeiros colocados: {times[0:5]}")
print(f"Os 4 últimos colocados: {times[16:]}")
print(f"Times em ordem alfabética: {sorted(times)}")
print(f"A chapecoense está na posição {times.index("Chapecoense")+1}")