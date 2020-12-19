from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar um nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Opcao de listar pessoas
        lerArquivo(arq)
    elif resposta == 2:
        #Opcao de cadastrar uma nova pessoas
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mOpcao Inválida!\033[m')
    sleep(1)
