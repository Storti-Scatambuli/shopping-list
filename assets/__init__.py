class ListadeCompras():
    lista = {}
    arquivo = ''
    
    def __init__(self):
        print('Qual arquivo de lista deseja utilizar?')
        self.arquivo = input('Nome ou caminho do arquivo: ')
        try:
            with open(self.arquivo, 'r') as arq:
                itens = arq.readlines()
            for item in itens:
                item = item.strip().split('.')
                self.lista[item[0]] = item[-1]
        except:
            arq = open(self.arquivo, 'x')
            arq.close()
            
    def atualizarLista(self, item=''):
        item = item.strip().capitalize().split(':')
        self.lista[item[0]] = item[1]
        
    def salvaLista(self):
        try:
            with open(self.arquivo, 'w') as arq:
                for item in self.lista:
                    arq.write(f'{item:.<50}{self.lista[item]}\n')
        except:
            print('Erro ao salvar a lista :(')
        else:
            print('Sua lista foi salva com sucesso!')
                
    def mostrarLista(self):
        for item in self.lista:
            print(f'{item:.<20}{self.lista[item]}')


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