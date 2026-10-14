#Realice un programa que indique si la suma de dos valores es positiva, negativa o cero.
import os

os.system("cls")

try:
    primerValor = float(input("Introduce el primer valor: "))
    segundoValor = float(input("Introduce el segundo valor: "))
    operacionS = primerValor + segundoValor

    if(operacionS == 0):
        print(f"La suma es igual a: -> {operacionS}")
    elif(operacionS < 0):
        print(f"La suma es n12egativa -> {operacionS}")
    else:
        print(f"La suma es positiva -> {operacionS}")
except ValueError:
    print("Error: Número entero no válido.")




