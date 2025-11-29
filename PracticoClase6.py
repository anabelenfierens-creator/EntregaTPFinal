import pandas as pd

data={
    "Nombre": ["Juan", "Ana", "Pedro","Juan", None],
    "Edad":[25, 30, None, 25, 40],
    "Ciudad":["Bs As", "Cordoba", " Mendoza", "Bs As", "La Plata"]
}

dataframe=pd.DataFrame(data)

dataframe["Nombre"].fillna("Anonimo",inplace=True)
print(dataframe)
dataframe["Edad"].fillna(dataframe["Edad"].mean(),inplace=True)
print(dataframe)
print(dataframe.duplicated())
dataframe_sin_dupli=dataframe.drop_duplicates()
print(dataframe_sin_dupli)
dataframe["Ciudad"]=dataframe["Ciudad"].replace("Bs As", "Buenos Aires")
print(dataframe)
dataframe["Nombre"]=dataframe["Nombre"].str.lower().str.strip()
print(dataframe)
dataframe["Ciudad"]=dataframe["Ciudad"].str.lower().str.strip()
print(dataframe)
dataframe["Edad"]=dataframe["Edad"].astype(int)
print(dataframe)