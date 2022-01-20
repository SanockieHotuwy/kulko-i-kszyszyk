import os
import numpy as np

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
wygrana = False
lista = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
def pokaz():
  clearConsole()
  print(lista[0]+" | "+lista[1]+" | "+lista[2])
  print("—— | —— | ——")
  print(lista[3]+" | "+lista[4]+" | "+lista[5])
  print("—— | —— | ——")
  print(lista[6]+" | "+lista[7]+" | "+lista[8])
  
def wygrana(X, Y):
  if str(X[0]) == str(X[1]) == str(X[2]):
    Y = True
    print("wygrana")  
while wygrana != True:
  pokaz()
  print("")
  nrPola = input("Podaj Nr Pola: ")
  lista = np.array(lista)
  lista = np.where(lista == nrPola, 'O ', lista)
  pokaz()
  print("")
  nrPola = input("Podaj Nr Pola: ")
  lista = np.array(lista)
  lista = np.where(lista == nrPola, 'X ', lista)
  wygrana(lista, wygrana)



