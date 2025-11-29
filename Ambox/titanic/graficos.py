import pandas as pd
import matplotlib.pyplot as plt

dataframe=pd.read_csv("C:\\Users\\HP\\Desktop\\PYTHON\\Ambox\\titanic\\Titanic_limpio.csv")
dataframe["Age"].hist(bins=20)
plt.title("Distribucion de edades")
plt.xlabel("Edad")
plt.ylabel("Cantidad")
plt.show()