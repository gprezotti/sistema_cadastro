import menu, cadastrar, listar, consultar, sair, excluir, carregar

carregar.carregarDados()

while True:
  opcao = menu.menu()
  if opcao == 0:
    sair.sair()
    break
  elif opcao == 1:
    cadastrar.cadastrar()
  elif opcao == 2:
    listar.listar()
  elif opcao == 3:
    consultar.consultar()
  else:
    excluir.excluir()