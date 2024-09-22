from cadastrar import usuarios

def excluir():
  '''
  Exclui um usuário informado pelo usuário.
  
  Caso o índice digitado pelo usuário não exista, gera um erro e pergunta novamente.'''
  while True:
    a = int(input("\nInsira o índice do usuário que quer excluir: "))
    try:
      usuarios.remove(usuarios[a])
      print("Usuário excluído com sucesso!\n")
      break
    except IndexError:
      print("Digite um índice existente (lembre-se: a faixa númerica vai de 0 até n - 1): ")