import numpy as np
import time
#generar 100mil valores entren 0 y 10
x = np.linspace(0, 10, 100000)
#Inicio conteo de tiempo
start= time.time()
#calcular f(x) vectorizado 
y=np.exp(-x) * np.sin(x)
#Calcular tiempo
end=time.time()
print("Tiempo de calculo vectorizado: ", end-start, "segundos")
