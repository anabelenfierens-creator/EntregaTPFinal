import pandas as pd

df1 =pd.DataFrame({
    "ID":[1,2],
    "NOMBRE":["Ana","Juan"]
})

df2 =pd.DataFrame({
    "ID":[3,4],
    "NOMBRE":["Pedro","Lucia"]
})

dataframe_concatenado = pd.concat([df1, df2], axis=0, ignore_index=True)
print(dataframe_concatenado)
print("------------------")

dataframe_concatenado = pd.concat([df1, df2], axis=1, ignore_index=True)
print(dataframe_concatenado)
print("------------------")