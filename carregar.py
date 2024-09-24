import csv
from cadastrar import usuarios

def carregarDados():
  '''
  Carrega os dados existentes no csv ao iniciar o programa
  '''
  try:
    with open("texto/dados.csv", mode="r") as arquivoCsv:
      reader = csv.DictReader(arquivoCsv)
      for linha in reader:
        usuarios.append(linha)
  except FileNotFoundError:
    pass