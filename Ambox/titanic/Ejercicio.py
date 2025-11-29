import pandas as pd
dataframe= pd.read_csv("C:\\Users\\HP\\Desktop\\PYTHON\\Ambox\\titanic\\titanic.csv")
print(dataframe.head())
#exploracion inicial
print(dataframe.info())
print(dataframe.describe())
print(dataframe.columns)
print("----------------------")
print("----------------------")
print(dataframe.isnull().sum())
print("----------------------")
print("----------------------")
#limpiar columnas que no necesitamos para nada
dataframe=dataframe.drop(columns=["Cabin", "Ticket", "Name"])
print(dataframe.columns)
print("----------------------")
print("----------------------")
#rellenar datos faltantes con la media
dataframe["Age"] = dataframe["Age"].fillna(dataframe["Age"].median())
dataframe["Embarked"]=dataframe["Embarked"].fillna("Unknow")
print(dataframe.isnull().sum())
print("----------------------")
print("----------------------")
#Analisis estadistico: taza superviviencia
#una vez todo limpio ya se puede hacer esto
#de esta manera vemos el porcentaje, por eso usamos el normalize
print(dataframe["Survived"].value_counts(normalize=True))
# 1 es vivo y 0 es muerto
#de esta manera vemos el total de vivos y muertos
print(dataframe["Survived"].value_counts())
print("----------------------")
print("----------------------")
#edad promedio
print(dataframe["Age"].mean())
print("----------------------")
print("----------------------")
#eadd promedio de fallecidos
print("Sigo aca")
print(dataframe[dataframe["Survived"]==0]["Age"].mean())
print("----------------------")
print("----------------------")
#supervivencia por sexo
print(dataframe.groupby("Sex")["Survived"].mean())
print("----------------------")
print("----------------------")
#supervivencia por clase social
print(dataframe.groupby("Pclass")["Survived"].mean())
print("----------------------")
print("----------------------")
dataframe.to_csv("C:\\Users\\HP\\Desktop\\PYTHON\\Ambox\\titanic\\Titanic_limpio.csv", index=False)



