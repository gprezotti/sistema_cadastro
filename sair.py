from cadastrar import usuarios
import csv

def sair():
  '''
  Salva todas as alteração feitas pelo usuário em um arquivo .csv
  
  Quando o usuário escolhe essa opção, o código é interrompido após a execução da função
  '''
  atributos = ["Nome", "Idade", "Email"]
  
  with open("texto/dados.csv", "w", newline="") as arquivoCsv:
    writer = csv.DictWriter(arquivoCsv, fieldnames=atributos)
    writer.writeheader()
    writer.writerows(usuarios)
    print("Dados salvos em 'texto/dados.csv' com sucesso!")