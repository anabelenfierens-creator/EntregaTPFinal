import numpy as pd #aca lo que le estamos diciendo es que importe numpy como pd, es el nombre que se le esta dando
#por eso en la linea 5 se por que el array es pd.array 

#crear array 1dimensional
arr = pd.array([1, 2, 3, 4, 5])
print(arr)

#para multiplicar cada arreglo del array por 2 por ejemplo, hacemos lo siguiente

arr2= arr*2
print(arr2)


arrayEjercicio = pd.arange(1,11)
print(arrayEjercicio)

#suma total
sumaTotal=pd.sum(arrayEjercicio)
print("La suma total es ", sumaTotal)

#Calcular promedio
promedio=pd.mean(arrayEjercicio)
print("El promedio es ", promedio)

#mayores a 5
mayorCinco=arrayEjercicio[arrayEjercicio > 5]
print("Los numeros mayores a 5, son: ",mayorCinco)

