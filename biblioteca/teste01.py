from biblioteca.lib.maior import *


listaNumeros = []
for contador in range(0, 5):
    listaNumeros.append(int(input(f'{contador+1}º valor: ')))


print(f'O maior valor é {maior(listaNumeros)}')
print(f'O menor valor é {menor(listaNumeros)}')
