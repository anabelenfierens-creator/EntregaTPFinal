#un millon de numeros aleatorios entre cero y 100
#clacular media, max, min, desviacion estandar
#filtrar numeros mayores a la media y contar cuantos son, sin bucles
import numpy as np
datos=np.random.uniform(0, 100, 1000000)
print(datos)
print("---------------")
#Calcular estadisticas
media=np.mean(datos)
maximos=np.max(datos)
minimos=np.min(datos)
destandar=np.std(datos)
print("Media: ",media)
print("Maximo: ",maximos)
print("Minimios: ", minimos)
print("Desvio estandar: ", destandar)

#valores mayores a la media
valores_mayores=datos[datos>media]
print("Valores mayores a la media: ", valores_mayores)
print("Cantidad de valores mayores a la media: ", len(valores_mayores))
print("---------------")
