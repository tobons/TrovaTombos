# -*- coding: utf-8 -*-
"""suma de extremos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j_oQBbuy5suQ8caU7z4LGRV_Yh8f_AM2
"""

def suma(n1,n2): # O(log n)
  imp,par=0,0 # O(1)
  while(n1<=n2): # O(log n)
    if(n1%2==0): # O(log n)
      par+=n1 # O(log n)
    else: # O(log n)
      imp+=n1 # O(log n)
    n1+=1 # O(log n)
  print(imp) # O(1)
  print(par) # O(1)
#ecuación de la función: 7 O(log n) + 3 O(1)
suma(4,14) # O(log n)