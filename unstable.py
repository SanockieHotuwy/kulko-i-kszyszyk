import os

import numpy as np

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
wygrana = False
lista = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
lista2 = ["  ","  ","  ","  ","  ","  ","  ","  ","  ",]
def pokaz():
  clearConsole()
  print("1    2    3")
  print("A   "+lista2[0]+" | "+lista2[1]+" | "+lista2[2])
  print("—— | —— | ——")
  print("B   "+lista2[3]+" | "+lista2[4]+" | "+lista2[5])
  print("—— | —— | ——")
  print("C   "+lista2[6]+" | "+lista2[7]+" | "+lista2[8])
  

while wygrana != True:
  pokaz()
  print("")
  nrPola = input("Podaj Nr Pola: ")
  if nrPola == "A1":
    lista2[0] = "O "
  if nrPola == "A2":
    lista2[1] = "O "
  if nrPola == "A3":
    lista2[2] = "O "
  if nrPola == "B1":
    lista2[3] = "O "
  if nrPola == "B2":
    lista2[4] = "O "
  if nrPola == "B3":
    lista2[5] = "O "
  if nrPola == "C1":
    lista2[6] = "O "
  if nrPola == "C2":
    lista2[7] = "O "
  if nrPola == "C3":
    lista2[8] = "O "
  lista = np.array(lista)
  lista = np.where(lista == nrPola, 'O ', lista)
  pokaz()
  if lista[1] == lista[2] == lista[0] or lista[3] == lista[4] == lista[5] or lista[6] == lista[7] == lista[8] or lista[0] == lista[3] == lista[6] or lista[1] == lista[4] == lista[7]or lista[2] == lista[5] == lista[8] or lista[0] == lista[4] == lista[8] or lista[2] == lista[4] == lista[6]:
    print("")
    print("Wygrywa O")
    wygrana = True
  if wygrana != True:
    print("")
    nrPola = input("Podaj Nr Pola: ")
  if nrPola == "A1":
    lista2[0] = "X "
  if nrPola == "A2":
    lista2[1] = "X "
  if nrPola == "A3":
    lista2[2] = "X "
  if nrPola == "B1":
    lista2[3] = "X "
  if nrPola == "B2":
    lista2[4] = "X "
  if nrPola == "B3":
    lista2[5] = "X "
  if nrPola == "C1":
    lista2[6] = "X "
  if nrPola == "C2":
    lista2[7] = "X "
  if nrPola == "C3":
    lista2[8] = "X "
    lista = np.array(lista)
    lista = np.where(lista == nrPola, 'X ', lista)
    if lista[1] == lista[2] == lista[0] or lista[3] == lista[4] == lista[5] or lista[6] == lista[7] == lista[8] or lista[0] == lista[3] == lista[6] or lista[1] == lista[4] == lista[7]or lista[2] == lista[5] == lista[8] or lista[0] == lista[4] == lista[8] or lista[2] == lista[4] == lista[6]:
        print("")
        print("Wygrywa X")
        wygrana = True
  



