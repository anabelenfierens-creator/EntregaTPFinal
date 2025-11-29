import pandas as pd

#ESTE ES EL DATAFRAME 1 EMPLEADOS
df_empleados = pd.DataFrame({
    "ID":[1, 2, 3, 4],
    "NOMBRE":["Ana", "Juan", "Pedro", "Lucia"],
    "Departamento":["Ventas", "IT", "Marketing", "IT"]
})

#DATAFRAME 2 SALARIOS
df_salarios = pd.DataFrame({
    "ID":[1, 2, 3, 5],
    "Salario":[3000, 4000, 3500, 4500]
})

#Merge inner, devuelve solo filas coincidencias en ambas tablas
df_inner=pd.merge(df_empleados, df_salarios, on="ID", how"inner")
print(df_inner)

