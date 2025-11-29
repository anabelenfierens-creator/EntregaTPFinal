#Crear un dataframe a partir de un diccionario

import pandas as pd
#Datos como diccionario
datos={
    "Nombre":["Ana", "Juan", "Pablo", "Lucia", "Carlos","Jorge","Emilio", "Ivan", "Isabel", "Belen"],
    "Edad":[25, 18, 40, 31, 52, 40, 42, 2, 4, 38],
    "Ciudades":["Berazategui", "Quilmes","Avellaneda", "Florencio Varela", "Lanus","Liniers","Ciudadela","Mataderos","Flores","Lugano"],
    "Salarios":[3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

}
print(datos)
#crear dataframe
dataframe = pd.DataFrame(datos)
print(dataframe)

print("---------------")
#Explorar el dataframe
#Muestra las primeras 5 filas
print(dataframe.head())
print("---------------")
#Mostrar las ultimas 5 filas
print(dataframe.tail())
print("---------------")
#Mostrar la cantidad de filas y columnas
print(dataframe.shape)
print("---------------")
#Mostrar informacion sobre el dataframe
print(dataframe.info())
print("---------------")
#acceder a columnas
print(dataframe["Ciudades"])
print("---------------")
#acceder a una fila
print(dataframe.iloc[4])
print("---------------")
#Describir datios estadisticos
#estadisticas generales de columnas numericas
print(dataframe.describe())
print("---------------")
#promedio de salarios
print(dataframe["Salarios"].mean())
print("---------------")
#Edad maxima
print(dataframe["Edad"].max())
print("---------------")
#Modificar datos agregar columna nueva
dataframe["Años de experiencia"] =[2, 5, 7, 8, 15, 20, 3, 8, 9, 10]
print(dataframe)
print("---------------")
#aumento del 10%a todos los empleados
dataframe["Salarios"]=dataframe["Salarios"]*1.1
print(dataframe)
print("---------------")
#Filtrar datos
#mayores a 30
mayores_30=dataframe[dataframe["Edad"]>30]
print(mayores_30)
print("---------------")
#dejar fuera un dato, por ejemplo no quiero gente de liniers
sin_liniers=dataframe[dataframe["Ciudades"]!="Liniers"]
print(sin_liniers)
print("---------------")
