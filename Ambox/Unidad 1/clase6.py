import pandas as pd

data={
    "Nombre": ["Juan", "Ana", "Pedro","Juan", None],
    "Edad":[25, 30, None, 25, 40],
    "Ciudad":["Bs AS", "Cordoba", " Mendoza", "Bs As", "La Plata"]
}

dataframe=pd.DataFrame(data)
#Ver valores nulos
print(dataframe.isnull())

#Borrar datos nulos
dataframe_sin_nulos=dataframe.dropna()
print(dataframe_sin_nulos)

#Reemplazar datos nulos es lo correcto para no borrar los datos juntados

dataframe["Edad"].fillna(dataframe["Edad"].mean(),inplace=True)
print(dataframe)

#Reemplazar el nombre por anonimo
dataframe["Nombre"].fillna("Anonimo",inplace=True)
print(dataframe)


