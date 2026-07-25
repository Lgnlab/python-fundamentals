lista = [5, 3, 1]
houve_troca = True

# O código só roda enquanto a lista não estiver totalmente organizada
while houve_troca:
    houve_troca = False # Assume que a lista já está certa
    
    for j in range(len(lista) - 1):
        if lista[j] > lista[j+1]:
            # Faz a troca dos números
            lista[j], lista[j+1] = lista[j+1], lista[j]
            houve_troca = True # Avisa que precisou mexer, então repete o while

print(lista)
