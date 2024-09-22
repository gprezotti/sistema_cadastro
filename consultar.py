from cadastrar import usuarios

def consultar():
  '''
  Mostra todos os dados de um usuário informado pelo usuário.
  
  Caso o índice informado pelu usuário não exista, gera um erro e pergunta novamente.
  '''
  while True:
    a = int(input("\nInsira o índice do usuário que quer consultar: "))
    try:
      print(f"{usuarios[a]}\n")
      break
    except IndexError:
      print("Digite um índice existente (lembre-se: a faixa númerica vai de 0 até n - 1): ")