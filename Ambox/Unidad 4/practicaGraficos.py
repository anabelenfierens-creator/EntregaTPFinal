import matplotlib.pyplot as plt
#Grafico de linea

x =[1, 2 ,3, 4, 5]
y=[10, 20, 25, 30, 40]

plt.plot(x,y)
plt.title("Crecimiento")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.savefig("Grafico-de-linea")
plt.show()


#Grafico de Barras

etiquetas = ["A", "B", "C"]
valores=[10, 25, 5]
plt.bar(etiquetas, valores)
plt.title("Comparación de valores")
plt.savefig("Grafico-de-barras")
plt.show()

#Grafico de torta

plt.pie([60, 30, 10], labels=["parte 1", "parte 2", "parte 3"], autopct='%1.1f%%')
plt.title("Distribucion de categorias")
plt.savefig("Grafico-de-torta")
plt.show()

#Grafico de histograma
import numpy as np
datos =np.random.normal(loc=50, scale=10, size=100)
plt.hist(datos, bins=10)
plt. title("Distribucion de datos")
plt.savefig("Histograma")
plt.show()

#dispersion

x = np.random.rand(50)
y = x+np.random.normal(0, 0.1, 50)
plt.scatter(x, y)
plt.title("Relacion entre variables")
plt.xlabel("Variable x")
plt.ylabel("Variable y")
plt.savefig("Dispersion")
plt.show()
