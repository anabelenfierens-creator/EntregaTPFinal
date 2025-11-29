import numpy as np

ejercicio=np.array([4, 8, 15, 16, 23, 42])
print("Suma del array: ", np.sum(ejercicio))
print("promedio: ", np.mean(ejercicio))
print("Desviacion estandar: ", np.std(ejercicio))
print("-----------")
#Calcular cada elemento elevado al cuadrado y luego sacar la raiz cuadrada
print("Elevado al cuadrado: ", ejercicio**2)
print("---------------")
print("Raiz cuadrada: ", np.sqrt(ejercicio))