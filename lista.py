lista_de_compras = []

while True:
    adicionar = input('voce gostaria de adicionar itens? se não, digite "sair". Se sim, digite-os: ')
    
    if adicionar.strip().lower() == 'sair':
        print('Voce saiu.')
        break
        
    if adicionar:
        itens_novos = adicionar.split(',')
        for item in itens_novos:
            item_limpo = item.strip()
            lista_de_compras.append(item_limpo)
        print(f'sua lista de compras atual é {lista_de_compras}')

while True:
    deletar = input('voce gostaria de deletar algum item da sua lista? se não, digite "sair". Se sim, digite-os: ')
    
    if deletar.strip().lower() == 'sair':
        print('voce saiu')
        break
        
    if deletar:
        itens_deletados = deletar.split(',')
        for item in itens_deletados:
            item_limpo = item.strip()
            try:
                lista_de_compras.remove(item_limpo)
                print(f'o item {item_limpo} foi removido com sucesso')
            except ValueError:
                print(f'o item que voce digitou nao esta na lista')
    print(f'a sua lista atual é {lista_de_compras}')

while True:
    listar = input('voce gostaria que os itens na sua lista fossem enumerados? Se não. digite "sair". Se sim, digite "sim": ')
    
    if len(lista_de_compras) == 0:
        print('sua lista esta vazia')
        
    if listar.strip().lower() == 'sair':
        print('voce saiu')
        break
        
    if listar.strip().lower() == 'sim':
        print('a sua lista enumerada é:')
        for indice, item in enumerate(lista_de_compras, start=1):
            print(f'{indice}: {item}')
        break
    else:
        print('escreva apenas uma das duas opcoes')
        continue

print(f'a sua lista atual é {lista_de_compras}')