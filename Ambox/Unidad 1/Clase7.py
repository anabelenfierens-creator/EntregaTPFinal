import pandas as pd
dataframe=pd.DataFrame({
    "nombre":["Ana", "Juan","Luis", "Ana"],
    "edad":[23, 45, 31, 28],
    "salario":[4000, 6500, 5200, 4100]
})
#Filtrar personas mayores de 30
print(dataframe[dataframe["edad"]>30])
#Filtrar con multiples condiciones
print(dataframe[(dataframe["edad"]>30) & (dataframe["salario"]>6000)])
#Usando loc
print(dataframe.loc[dataframe["nombre"]=="Ana"])
#Nombre y salario de mayores de 30
print(dataframe.loc[dataframe["edad"]>30, ["nombre","salario"]])
#Usando query
print(dataframe.query("edad > 30 and salario > 6000"))

#agrupar por nombre y sacar promedio de salario
print(dataframe.groupby("nombre")["salario"].mean())
print(dataframe.groupby("edad")["salario"].mean())

#agrupar por nombre y contar cuantas veces aparece
print(dataframe.groupby("nombre").size())

#agregar por nombre y multiples funciones
print(dataframe.groupby("nombre")["salario"].agg(["mean", "min", "max"]))