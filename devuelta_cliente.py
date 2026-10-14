#Escribir un programa que calcule la devuelta que debe darse a un cliente luego de
#realizado una compra, los datos capturados deben ser positivos y tomar en cuenta
#que se captura el monto de la compra y el monto de pago dado por el cliente.

import os 

while True:
    os.system("cls")
    print("Bienvenidos al programa")
    valorCompra = float(input("Ingresar valor de la compra: "))
    valorPagado = float(input("Ingresa el valor pagado por el cliente: "))
    devuelta = valorPagado-valorCompra

    if(valorCompra < 0 or valorPagado < 0):
        print("Los valores ingresados son menores que 0. Debes de ingresar valores positivos.")
        valorCompra = 0
        valorPagado = 0
        os.system("pause")
    elif (valorCompra > valorPagado):
        print("El valor de compra sobrepasa el valor pagado.")
        os.system("pause")
    else:
        print(f"El valor pagado: {valorPagado}. Valor de la compra:{valorCompra}, devuelta es igual a: 400{devuelta}")
        break