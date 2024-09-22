def menu():
  '''
  Pergunta ao usuário a ação que ele quer fazer.
  
  A resposta do usuário do usuário deve ser um número entre 0 e 4.
  
  Se for uma resposta com um tipo de dado incompatível mostra uma mensagem de erro e pergunta novamente
  '''
  print("0 - Sair")
  print("1 - Cadastrar")
  print("2 - Listar")
  print("3 - Consultar")
  print("4 - Excluir")
  
  while True:
    try:
      a = int(input("Insira o número do que você quer fazer: "))
      if a >= 0 and a <= 4:
        return a
      else:
        print("Escolha um número de 0 a 4!")
    except ValueError or TypeError:
      print("Insira somente números!")