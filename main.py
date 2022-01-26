import os
import sys
import numpy as np

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
wygrana = False
poprawnyRuch = False
lista = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
lista2 = ["  ","  ","  ","  ","  ","  ","  ","  ","  ",]
def pokaz():
  clearConsole()
  print("    1    2    3")
  print(" ")
  print("A   "+lista2[0]+" | "+lista2[1]+" | "+lista2[2])
  print("    —— | —— | ——")
  print("B   "+lista2[3]+" | "+lista2[4]+" | "+lista2[5])
  print("    —— | —— | ——")
  print("C   "+lista2[6]+" | "+lista2[7]+" | "+lista2[8])
while wygrana == False:
  poprawnyRuch = False
  while poprawnyRuch == False:
    poprawnyRuch = False
    pokaz()
    print("")
    nrPola = input("Podaj Nr Pola: ")
    if nrPola == "A1":
      if lista[0] == "A1":
        lista2[0] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
        cos = False
      else:
        print("COs nie ten teges")
    if nrPola == "A2":
      if lista[1] == "A2":
        lista2[1] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("Cos nie ten teges")
    if nrPola == "A3":
      if lista[2] == "A3":
        lista2[2] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if nrPola == "B1":
      if lista[3] == "B1":
        lista2[3] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if nrPola == "B2":
      if lista[4] == "B2":
        lista2[4] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if nrPola == "B3":
      if lista[5] == "B3":
        lista2[5] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if nrPola == "C1":
      if lista[6] == "C1":
        lista2[6] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if nrPola == "C2":
      if lista[7] == "C2":
        lista2[7] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if nrPola == "C3":
      if lista[8] == "C3":
        lista2[8] = "O "
        lista = np.array(lista)
        lista = np.where(lista == nrPola, 'O ', lista)
        poprawnyRuch = True
      else:
        print("COs nie ten teges")
    if lista[1] == lista[2] == lista[0] or lista[3] == lista[4] == lista[5] or lista[6] == lista[7] == lista[8] or lista[0] == lista[3] == lista[6] or lista[1] == lista[4] == lista[7]or lista[2] == lista[5] == lista[8] or lista[0] == lista[4] == lista[8] or lista[2] == lista[4] == lista[6]:
      print("")
      print("Wygrywa O")
      wygrana = True
      sys.exit()
    if poprawnyRuch == True:
      poprawnyRuch = False
      while poprawnyRuch == False:
        pokaz()
        if wygrana != True:
          print("")
          nrPola = input("Podaj Nr Pola: ")
          if nrPola == "A1":
            if lista[0] == "A1":
              lista2[0] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "A2":
            if lista[1] == "A2":
              lista2[1] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("Cos nie ten teges")
          if nrPola == "A3":
            if lista[2] == "A3":
              lista2[2] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "B1":
            if lista[3] == "B1":
              lista2[3] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "B2":
            if lista[4] == "B2":
              lista2[4] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "B3":
            if lista[5] == "B3":
              lista2[5] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "C1":
            if lista[6] == "C1":
              lista2[6] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "C2":
            if lista[7] == "C2":
              lista2[7] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if nrPola == "C3":
            if lista[8] == "C3":
              lista2[8] = "X "
              lista = np.array(lista)
              lista = np.where(lista == nrPola, 'X ', lista)
              poprawnyRuch = True
            else:
              print("COs nie ten teges")
          if lista[1] == lista[2] == lista[0] or lista[3] == lista[4] == lista[5] or lista[6] == lista[7] == lista[8] or lista[0] == lista[3] == lista[6] or lista[1] == lista[4] == lista[7]or lista[2] == lista[5] == lista[8] or lista[0] == lista[4] == lista[8] or lista[2] == lista[4] == lista[6]:
            print("")
            pokaz()
            print("Wygrywa X")
            wygrana = True
            sys.exit()


      
