import pandas as pd
data={
    "Nombre": ["Juan", "Ana", "Pedro","Juan", "Jorge", "Jorge", "Jorge"],
    "Edad":[25, 30, 29, 25, 40, 40, 40],
    "Ciudad":["Bs As", "Cordoba", "Bs As", "Bs As", "La Plata", "La Plata", "La Plata"]
}
dataframe=pd.DataFrame(data)

#Metodo duplicado
print(dataframe.duplicated())

dataframe_sin_duplicados=dataframe.drop_duplicates()
print(dataframe_sin_duplicados)

#Hacer que la columna sea mas legibles para cualquiera que lea la tabla
dataframe["Ciudad"]=dataframe["Ciudad"].replace("Bs As", "Buenos Aires")
print(dataframe)

#Pasar todos los nombrss a minuscula
dataframe["Nombre"]=dataframe["Nombre"].str.lower()
print(dataframe)
#Pasarlos a mayuscula
dataframe["Nombre"]=dataframe["Nombre"].str.upper()
print(dataframe)
#Cambiar nombre a las columnas
dataframe.rename(columns={
    "Nombre":"nombre",
    "Edad":"edad",
    "Ciudad":"ciudad"
},inplace=True)
print(dataframe)


