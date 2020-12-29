# Maior valor a ser procurado na lista
def maior(lista):
    """
    Funcao que percorre uma lista do incico ao fim a procura do maior elemento.
    :param lista: Lista informado pelo usuario
    :return: o maior elemento da lista
    Funcao criado por Rivan Roque 29/12/2020
    """
    maiorValor = 0
    for contador in range(0, len(lista)):
        if contador == 0:
            maiorValor = lista[contador]
        elif lista[contador] > maiorValor:
            maiorValor = lista[contador]
    return maiorValor


# Menor valor a ser procurado na lista
def menor(lista):
    """
        Funcao que percorre uma lista do incico ao fim a procura do menor elemento.
        :param lista: Lista informado pelo usuario
        :return: o menor elemento da lista
        Funcao criado por Rivan Roque 29/12/2020
        """
    for indice, valor in enumerate(lista):
        if indice == 0:
            menorValor = lista[indice]
        elif lista[indice] < menorValor:
            menorValor = lista[indice]
    return menorValor


# Soma de todos valores da lista
def somaTotal(lista):
    """
    Função que calculo a soma de todos os elementos da lista
    :param lista: Lista de valores informados pelo usuario.
    :return: a soma total
    Funcao criado por Rivan Roque 29/12/2020
    """
    soma = 0
    for valor in lista:
        soma += valor
    return soma


# Tamanho total da lista passada
def tamanho(lista):
    comprimentoLista = 0
    for valor in lista:
        comprimentoLista += 1
    return comprimentoLista


# Media dos valores dentro da lista
def media(lista):
    mediaLista = somaTotal(lista)/tamanho(lista)
    return mediaLista


#Mostrar os dados na tela para o usuario
def mostrarDados(lista):
    return lista