# -*- coding: utf-8 -*-
"""Factorielle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_6FqrzGC_X9MbA3tzIfTU2_rY3JBlQ_a

**Fonction Factorielle**
"""

# b. Implimenter la fonction factorielle 
def factorielle(n):
  if n == 0: #Condition si n = 0
    return 1
  else: 
    Facteur = 1
    for k in range(2,n+1): #Demander d'itérer les valeurs de 1 à n pour appliquer la multiplication
      Facteur = Facteur * k
    return Facteur

factorielle(5)