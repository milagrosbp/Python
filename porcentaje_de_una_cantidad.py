#Escribir un programa que calcula el porcentaje de una cantidad
import os

os.system("cls")

cantidad = float(input("Introduce el valor que deseas conocer el porcentaje: "))
porciento = float(input("Introduce el porciento en número (20)(30)(15) etc:"))

operacion = round((cantidad*porciento)/100)

print(f"El {porciento}% de {cantidad} es {operacion}")