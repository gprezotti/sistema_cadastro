from cadastrar import usuarios

def listar():
  '''
  Lista todos os usuários cadastrados pelo usuário.
  '''
  if usuarios:
    print("\nLista de usuários cadastrados:")
    for i, user in enumerate(usuarios):
      print(f"{i} - Nome: {user["Nome"]}, Idade: {user["Idade"]}, Email: {user["Email"]}\n")
  else:
    print("Nenhum usuário foi cadastrado ainda!\n")