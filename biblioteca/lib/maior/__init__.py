def maior(lista):
    maiorValor = 0
    for contador in range(0, len(lista)):
        if contador == 0:
            maiorValor = lista[contador]
        else:
            if lista[contador] > maiorValor:
                maiorValor = lista[contador]
    return maiorValor



def menor(lista):
    menorValor = 0
    for contador in range(0, len(lista)):
        if contador == 0:
            menorValor = lista[contador]
        else:
            if lista[contador] < menorValor:
                menorValor = lista[contador]
    return menorValor
