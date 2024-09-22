usuarios = []

def cadastrar():
  '''
  Pergunta ao usuário os dados necessários para cadastrar um usuário e armazena os valores um dicionário 'usuario'.
  
  Após, adiciona o dicionário 'usuario' à lista 'usuarios'.
  '''
  nome = str(input("\nInisira o nome: "))
  idade = int(input("Insira a idade: "))
  email = str(input("Inisira o email: "))
  
  usuario = {
    "Nome": nome,
    "Idade": idade,
    "Email": email
  }
  
  usuarios.append(usuario)
  print("Usuário cadastrado com sucesso!\n")