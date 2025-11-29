import pandas as pd
#Datos como diccionario
datos={
    "Nombre":["Ana", "Juan", "Pablo", "Lucia", "Carlos","Jorge"],
    "Edad":[25, 18, 40, 31, 52, 40],
    "Ciudades":["Berazategui", "Quilmes","Avellaneda", "Florencio Varela", "Flores","Lugano"],
    "Salarios":[3000, 4000, 5000, 6000, 7000, 8000],
    "Puestos":["Analista", "Desarrollador","Gerente", "Analista","Desarrollador","Diseñador"]
}

dataframe_empleados=pd.DataFrame(datos)
print("Data Frame creado")
print(dataframe_empleados)
print("---------")
#Mostrar primeras 3 filas
print(dataframe_empleados.head(3))
print("---------")
#Mostrar cantidad filas y columnas
print(dataframe_empleados.shape)
print("---------")
#Resumen estadistico
print(dataframe_empleados.describe())
print("---------")
#Analisis estadistico
salario_promedio=dataframe_empleados["Salarios"].mean()
edad_mini=dataframe_empleados["Edad"].min()
edad_maxi=dataframe_empleados["Edad"].max()
salario_maximo=dataframe_empleados["Salarios"].max()
print("El salario promedio")
print(salario_promedio)
print("La edad minima")
print(edad_mini)
print("La edad maxima")
print(edad_maxi)
print("El salario maximo")
print(salario_maximo)
print("---------")
#Modificar datos
dataframe_empleados["Años de experiencia"]=[1, 2, 3, 4, 5, 6,]
print(dataframe_empleados)
print("-----------")
dataframe_empleados["Salarios"]=dataframe_empleados["Salarios"]*1.07
print(dataframe_empleados)
print("-----------")
#cambiar de puesto a un empleado
dataframe_empleados.loc[dataframe_empleados["Nombre"]== "Lucia","Puestos"]="Jefa de proyecto"
print(dataframe_empleados)
print("-----------")
#Filtrar datos
salariopro=dataframe_empleados[dataframe_empleados["Salarios"]>5000]
print(salariopro)
print("-----------")
ciudad=dataframe_empleados[dataframe_empleados["Ciudades"]=="Lugano"]
print(ciudad)
print("-----------")
labor=dataframe_empleados[dataframe_empleados["Puestos"]=="Analista"]
print(labor)
print("-----------")
#guardar datos
dataframe_empleados.to_csv("nuevo_dataframe.csv",index=false)
