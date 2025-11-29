import pandas as pd
datos =[10, 20, 30, 40, 50]
series = pd.Series(datos)
print(series)
#LOS RESULTADOS VAN CON SU INDICE, ES LA COLUMNA JUNTO A SU INDICE, ESTO ES LO MAS IMPORTANTE PARA EL ANALISIS DE DATOS
#DATAFRAME EN PYTHON ES ESTRUCTURA DE DATOS BIDIMENSIONAL CON FILAS Y COLUMNAS
dataframe =pd.DataFrame({
    "Nombre":["Ana", "Pedro", "Jacintio", "Roman", "Felipe"],
    "Edad":[25, 18, 41, 29, 59],
    "Salario":[8000, 9000, 4000, 3000, 2000]
})
print(dataframe)
#como acceder a una columna
print(dataframe["Edad"])
#comoacceder a una fila
print(dataframe.iloc[1])
#acceder a fila especifica
print(dataframe.loc[[0,3]])
#obtener de una persona especifa
print(dataframe[dataframe["Nombre"]=="Felipe"])