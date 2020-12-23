lista = []
maiorValor = menorValor = 0

#Insercao de dados na lista e fazendo comparaçoes entre os valores para encontrar o maior e o menor valor da lista
for contador in range(0, 5):
    lista.append(int(input(F'{contador+1}º valor: ')))
    if contador == 0:
        maiorValor = menorValor = lista[contador]
    elif lista[contador] > maiorValor:
        maiorValor = lista[contador]
    elif lista[contador] < menorValor:
        menorValor = lista[contador]

print('=' * 30)
print(f'Voce digitou os seguintes valores {lista}')
print(f'O maior valor digitado foi {maiorValor} nas posições ', end='')

#Percorrer  vetor a procura do indice do maior valor
for indice, valor in enumerate(lista):
    if valor == maiorValor:
        print(f'{indice+1}º', end='')
print()
print(f'O menor valor digitado foi {menorValor} nas posições ', end='')

#Percorrer vetor a procura do indice do menor valor
for indice, valor in enumerate(lista):
    if valor == menorValor:
        print(f'{indice+1}', end='')
print()
print('Fim!')
