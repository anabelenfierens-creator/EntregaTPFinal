import numpy as np

arr=np.array([10, 20, 30, 40, 50, 60])
print("Array original: ", arr)
print("---------------")
print("Array sumado: ",arr+5)
print("---------------")
print("Array multiplicado * 2: ", arr*2)
print("---------------")

#Funciones estadisticas
#Sumar todos los elementos del array:
print("Sumar todos los elementos, resultado: ", np.sum(arr))
print("---------------")
#Media, suma todos los elementos y los divide por la cantidad
print("La media es: ", np.mean(arr))
print("---------------")
print("Desviacion estandar: ", np.std(arr))
print("---------------")
print("Devuelve el valor minimo: ", np.min(arr))
print("Devuelve el valor maximo: ", np.max(arr))
print("---------------")





