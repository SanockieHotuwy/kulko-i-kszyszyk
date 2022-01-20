import os
import numpy as np

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

lista = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
def pokaz():
  clearConsole()
  print(lista[0]+" | "+lista[1]+" | "+lista[2])
  print("—— | —— | ——")
  print(lista[3]+" | "+lista[4]+" | "+lista[5])
  print("—— | —— | ——")
  print(lista[6]+" | "+lista[7]+" | "+lista[8])
  
while 1 == 1:
  pokaz()
  print("")
  nrPola = input("Podaj Nr Pola: ")
  lista.index(nrPola) = "X"
lista = np.array(my_lista)
lista = np.where(my_lista == 'nrPola, 'Green', my_list)
print(my_list)
