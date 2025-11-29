import pandas as pd
alumnos= pd.DataFrame({
    "ID":[1, 2, 3],
    "Nombre":["Ana","Luis","Maria"],
    "Edad":[20, 22, 21]
})

notas=pd.DataFrame({
    "ID":[1,2,3,1],
    "Materia":["MATEMATICA","HISTORIA","INGLES", "HISTORIA"],
    "Notas":[9, 7, 8, 10]
})

consolidado = pd.merge(alumnos, notas, on="ID", how="inner")
print(consolidado)

alumnos_nuevos1= pd.DataFrame({
    "ID":[4, 5],
    "Nombre":["Pedro","Lucia"],
    "Edad":[23, 20]
})

alumnos_nuevos2= pd.DataFrame({
    "ID":[6, 7],
    "Nombre":["Jorge","Sofia"],
    "Edad":[24, 22]
})

#concatenar todos los alumnos
alumnos_total=pd.concat([alumnos, alumnos_nuevos1, alumnos_nuevos2])
print(alumnos_total)