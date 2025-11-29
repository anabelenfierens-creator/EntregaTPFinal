"""
nombre =input("Ingresa tu nombre: ")
edad =int(input("Ingresa tu edad: "))
if type(int(edad)) == int: 
    if edad>=18:
        print(f"Hola {nombre} eres mayor de edad")
    else:
        print(f"Hola {nombre} eres menor de edad")
"""

"""
X = 5
Y = 10
suma= X+Y
print ("la suma es: ", suma)
"""
"""
#listas:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[4]) #ese 4 indica la posicion, por lo que el resultado es 5, recordar que lasposiciones se cuentan a partir de 0
frutas = ["banana", "manzana", "durazno", "kiwi", "naranja", "mandarina"]
print(frutas[3])
#lista adentro de una lista
saludos = ["hola", "hello", "bye", "chau", [1,2,3,4,5,6,7,8]]
#podemosmcitar las ubicaciones de cada una
print(saludos[4][3]) #el 4 me lleva a la sublista, ya que su iubicacion es 4 y el segundo corchete me arroja el numero 4 ya que se encuentra en la posicion 3
#si escribo print (saludos[3][3]) me muestra la letra u de la palabra chau, ya que le pedi la posicion 3 de la posicion 3
"""
"""
Verduras = ["lechuga", "tomate","berenjena"]
print (Verduras)
Verduras.append ("zanahorias")
print (Verduras)
Verduras.remove("tomate")
print (Verduras)
print(len(Verduras))
"""

"""
ciudades = ["berazategui", "florencio varela", "quilmes", "la plata"]
print (ciudades)
ciudades.append ("lanus")
print (ciudades)
ciudades.remove ("berazategui")
print (ciudades)
"""
"""
#metodo subslicing
print(Verduras[1:3])
"""
"""
#Tuplas:
Verduras = ("tomate","zanahoria", "papas", "cebolla", "ajo")
print(Verduras[1])
"""

#diccionario
personas = {"Nombre": "Ana", "Edad":25, "Ocupacion": "estudiante"}
print(personas)
print(personas["Edad"])

