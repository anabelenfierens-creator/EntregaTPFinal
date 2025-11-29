import pandas as pd
dataframe =pd.DataFrame({
    "Nombre" : ["Ana", "Juan", "Pedro", "Belen", "Jorge"],
    "Edad" : [20, 35, 21, 15, 50],
    "Salario" : [300000, 610000, 400000, 700000, 524855]
})
print(dataframe) 

print("--------")

ingrese_edad=int(input("Ingrese la edad que busca: "))

mayor30=dataframe[dataframe["Edad"]>ingrese_edad]
print("Personas con edad mayor a", ingrese_edad, ":")
print(mayor30["Nombre"])

print("------")

Salario=dataframe[dataframe["Salario"]>500000]
print(Salario[["Nombre", "Salario"]])
