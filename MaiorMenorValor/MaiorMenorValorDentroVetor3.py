lista = []
maiorValor = menorValor = 0

#Insercão de dados na lista e fazendo comparaçoes
# entre os valores para encontrar o maior e o menor valor da lista
for contador in range(0, 5):
    lista.append(int(input(f'{contador+1}º valor: ')))
    if contador == 0:
        maiorValor = menorValor = lista[contador]
    elif lista[contador] > maiorValor:
        maiorValor = lista[contador]
    elif lista[contador] < menorValor:
        menorValor = lista[contador]

print('_' * 30)
print(f'Valores digitados: {lista}')

#Percorrer  vetor a procura do indice do maior e menor valor
for indice, valor in enumerate(lista):
    if valor == maiorValor:
        print(f'O maior valor digitado foi {maiorValor} na posição {indice+1}')
    if valor == menorValor:
        print(f'O menor valor digitado foi {menorValor} na posição {indice+1}')
print('Fim do Programa!')
print('Feliz Natal')
