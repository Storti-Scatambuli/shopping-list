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
        self.lista[item[0]]