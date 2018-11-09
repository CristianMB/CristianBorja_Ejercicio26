import numpy as np
import matplotlib.pyplot as pyplot
import os

#Leer Archivo
PI = open("archivo.txt",'r')
#Extraer Valores
vals = PI.read()
PI.close()

def SPLIT(n_splits):
  New_Size = len(vals)//n_splits            #Defino nuevo tamaño de sub-archivos
  OutDoc = 'Split_' + str(n_splits) + '.txt'
  OUT = open(OutDoc,'w')
  OUT.write(vals[int(np.random.random()*10):New_Size])
  OUT.close()

split = np.array([10,20,50,100])
for i in split:
    SPLIT(i)
