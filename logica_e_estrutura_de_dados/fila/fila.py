from collections import deque

fila = deque() #  cria uma fila onde o primeiro a entrar é o primeiro a sair (FIFO)

fila.append("Lucas")

fila.append("João")

fila.append("Maria")

print(fila.popleft()) # remove e retorna o primeiro elemento da fila (o que estava mais à esquerda).