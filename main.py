import assets

lista = assets.ListadeCompras()

while True:
    entrada = assets.menu('LISTA DE COMPRAS', ['Ver lista', 'Mudar lista', 'Salvar lista', 'Sair'])
    
    if entrada == 0:
        lista.mostrarLista()
        
    if entrada == 1:
        print('Digite o nome do item, seguido por : e logo sua quantidade com unidade, exemplo: Arroz: 20KG.\nDigite SAIR para sair.')
        while True:
            lista.mostrarLista()
            entradaLista = input('>>> ').strip().upper()
            if entradaLista == 'SAIR':
                break
            elif ':' not in entradaLista:
                print('Modo incorreto de item')
            else:
                lista.atualizarLista(entradaLista)
                
    if entrada == 2:
        lista.salvaLista()
            
    if entrada == 3:
        print('Você escolheu sair')
        break