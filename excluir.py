from cadastrar import usuarios

def excluir():
  '''
  Exclui um usuário informado pelo usuário.
  
  Caso o índice digitado pelo usuário não exista, gera um erro e pergunta novamente.
  '''
  while True:
    email = str(input("\nInsira o email do usuário que quer excluir: "))
    for i, usuario in enumerate(usuarios):
      if usuario["Email"] == email:
        del usuario[i]
        print("Usuário excluído com sucesso!\n")
        return
      else:
        print("Usuário não encontrado. Por favor verifique se o emial digitado está correto e de que o usuário desejado está cadastrado!")