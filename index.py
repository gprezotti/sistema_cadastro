import menu
import cadastrar
import listar
import consultar
import sair
import excluir


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