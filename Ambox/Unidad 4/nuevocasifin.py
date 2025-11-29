import pandas as pd
import numpy as numpy
dataframe = pd.read_csv(r'C:\Users\HP\Downloads\InternationalVisitorArrivalsbyCountryofNationality.csv')
# AÑADE ESTA LÍNEA PARA VER LAS PRIMERAS FILAS:
print(dataframe.head())
media_por_pais=dataframe.groupby("con")["arv_count"].mean().sort_values(ascending=False)
print(media_por_pais)