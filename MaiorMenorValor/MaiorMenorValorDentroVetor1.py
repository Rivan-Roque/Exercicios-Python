lista = []
maiorValor = menorValor = 0

#Insercao dos 5 valores na lista
for contador in range(0, 5):
    lista.append(int(input(f'Digite o {contador+1}º valor: ')))

print('=' * 30)
print(f'Voce digitou os seguintes valores: {lista}')

#Fazendo comparaçoes com todos dos dados da lista para encontrar o maior e o menor valor da lista
for indice, valor in enumerate(lista):
    if indice == 0:
        maiorValor = menorValor = lista[indice]
    elif lista[indice] > maiorValor:
        maiorValor = lista[indice]
    elif lista[indice] < menorValor:
        menorValor = lista[indice]

#Fazendo a comparacao de todos os valores da lista para a procura do indice do maior e menor valor
for indice, valor in enumerate(lista):
    if valor == maiorValor:
        print(f'O maior valor informado foi {maiorValor} na posiçao {indice+1}')
    if valor == menorValor:
        print(f'O menor valor informado foi {menorValor} na posicao {indice+1}')
