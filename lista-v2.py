lista_de_compras = []

while True:
   print("\n--- MENU DE COMPRAS ---")
   print("[1] Adicionar itens")
   print("[2] Deletar itens")
   print("[3] Listar itens")
   print("[4] Sair")
   opcao = input("Escolha uma opção: ").strip()

   if opcao == '1':
       adicionar = input('Digite os itens separados por vírgula: ')
       if adicionar:
           itens_novos = adicionar.split(',')
           for item in itens_novos:
              lista_de_compras.append(item.strip())
           print(f'Sua lista de compras atual é {lista_de_compras}')

   elif opcao == '2':
       deletar = input('Digite os itens para deletar separados por vírgula: ')
       if deletar:
           itens_deletados = deletar.split(',')
           for item in itens_deletados:
               item_limpo = item.strip()
               try:
                   lista_de_compras.remove(item_limpo)
                   print(f'O item [{item_limpo}] foi removido com sucesso')
               except ValueError:
                   print(f'Ops! O item [{item_limpo}] não está na lista')
           print(f'A sua lista atual é {lista_de_compras}')

   elif opcao == '3':
       if len(lista_de_compras) == 0:
           print('Sua lista está vazia.')
       else:
           print('A sua lista enumerada é:')
           for indice, item in enumerate(lista_de_compras, start=1):
               print(f'{indice}: {item}')

   elif opcao == '4':
       print("Você encerrou o programa!")
       print(f'A sua lista final é: {lista_de_compras}')
       break

   else:
       print("Opção inválida. Digite 1, 2, 3 ou 4.")