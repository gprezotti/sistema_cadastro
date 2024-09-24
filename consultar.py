from cadastrar import usuarios

def consultar():
  '''
  Mostra todos os dados de um usuário informado pelo usuário.
  
  Caso o índice informado pelu usuário não exista, gera um erro e pergunta novamente.
  '''
  email = str(input("\nInsira o email do usuario que deseja consultar: "))
  encontrado = False
  for usuario in usuarios:
    if usuario["Email"] == email:
      print(f"Nome: {usuario["Nome"]}, Idade: {usuario["Idade"]}, Email: {usuario["Email"]}\n")
      encontrado = True
      break
  if not encontrado:
    print("Usuário não encontrado. Por favor verifique se o emial digitado está correto e de que o usuário desejado está cadastrado!")