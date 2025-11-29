#Usando listas de python

lista=[1,2,3,4,5]
resultado_lista=[x*2 for x in lista]
print(resultado_lista)
print("----------------")

#Lo mismo de antes pero usando numpy

import numpy as np

arr=np.array([1,2,3,4,5])
resultado_np=arr*2
print(resultado_np)
print("-------------------")
#Array bidimensional
matriz=np.array([[1,2,3,],[4,5,6]])
print(matriz)

#Acceder a lo lugares del array

print("Primer elemento: ", arr[0])
print("----------------------")
print("Imprimir elementos del indice 1 al 3: ", arr[1:4])#el indice 4 no lo toca, por eso imprimelos numeros 2, 3 y 4. 
print("----------------------")
print("Elemento fila 2, columna 3: ", matriz[1, 2])
print("----------------------")

#ejercicio:

list = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print("Elementos desde el 3 indice al 7mo: ", list[3:8])
bidi=np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print("Elementon central:") 
print(bidi[1,1])
print("----------------")

#Ejercicio 2:

