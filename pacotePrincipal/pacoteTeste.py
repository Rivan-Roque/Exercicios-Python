from pacotePrincipal.pacotemaior import *
#from pacotePrincipal import pacotemaior


valores = []

for contador in range(0, 5):
    valores.append(int(input(f'{contador+1}º valor: ')))

print('=' * 30)
print(f'Voce digitou os seguintes dados {mostrarDados(valores)}')
print(f'O maior valor digitado foi {maior(valores)}')
print(f'O menor valor digitado foi {menor(valores)}')
print(f'A soma de todos os valores da lista é {somaTotal(valores)}')
print(f'Foi digitado um total de {tamanho(valores)} valores.')
print(f'A media total é {media(valores):.2f}')


help(maior)
#print(f'O maior valor digitado foi {pacotemaior.maior(valores)}')