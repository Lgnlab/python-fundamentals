# A LISTA PRECISA ESTAR ORDENADA 

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio  # Retorna a posição do item
        elif lista[meio] < alvo:
            esquerda = meio + 1  # Olha na metade da direita
        else:
            direita = meio - 1   # Olha na metade da esquerda

    return -1  # Retorna -1 se não achar o item


# Exemplo de uso:
numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
resultado = busca_binaria(numeros, 23)
print(resultado)  # Saída: 5 (posição do número 23)
