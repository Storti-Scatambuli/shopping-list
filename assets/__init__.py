def titulo(texto, caracter='='):
    tamanho = len(texto) + 4
    print(caracter*tamanho)
    print(f'{texto:^{tamanho}}')
    print(caracter*tamanho)

def menu(titulo_texto, opcoes=[]):
    titulo(titulo_texto)
    for i, opcao in enumerate(opcoes):
        print(f'{i:.<{len(titulo_texto)+4}}{opcao}')
    print()
    while True:
        try:
            decisao = int(input())
        except:
            print('Insira um valor válido')
        else:
            if decisao < len(opcoes) and decisao >= 0:
                break
            else:
                print('Digite um valor dentro do intervalo das opções')
    return decisao

def mostraItens(itens_dicionario):
    for item in itens_dicionario:
        print(f'{item:.<20}{itens_dicionario[item]}')
        
def atualizarItem(itens_dicionario):
    print('Digite o nome do produto seguido por : e logo insira o valor que queira adicionar.\nNão se preocupe caso o item não esteja sendo exibido, digite o nome e ele será criado.\nDigite sair para voltar ao menu anterior e salvar as alterações.')
    print()
    itens_copia = itens_dicionario
    while True:
        mostraItens(itens_copia)
        entrada = input('').strip().upper()
        if entrada == 'SAIR':
            break
        elif ':' not in entrada:
            print('Favor, digite um valor correto')
        else:
            entrada = entrada.split(':')
            itens_copia[entrada[0]] = entrada[1]
    
def abreLista(dicionario, arquivo='lista.txt'):
    try:
        with open(arquivo, 'r') as arq:
            itens = arq.readlines()
        for item in itens:
            item_lista = item.strip().split('.')
            dicionario[item_lista[0]] = item_lista[-1]
    except:
        arq = open(arquivo, 'x')
        arq.close()
     
def salvaLista(dicionario, arquivo='lista.txt'):
    with open(arquivo, 'w') as arq:
       for item in dicionario:
           arq.write(f'{item:.<50}{dicionario[item]}\n') 