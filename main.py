import assets

lista = {}

assets.abreLista(lista)

while True:
    entrada = assets.menu('LISTA DE COMPRAS', ['Ver lista', 'Mudar lista', 'Salvar lista', 'Sair'])
    
    if entrada == 0:
        assets.mostraItens(lista)
    if entrada == 1:
        assets.atualizarItem(lista)
    if entrada == 2:
        assets.salvaLista(lista)
    if entrada == 3:
        print('Obrigado, volte sempre.')
        break
    