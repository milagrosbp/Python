#Escribir un programa que indica cuantos valores positivos, negativos o 0 fueron
#ingresados por el teclado de un conjunto de 10 datos (utilizar estructura se control for).

contador = 0
positivo = 0
negativo = 0
cero = 0

while contador !=10:

    for i in range(10):
        valorNumero = int(input(f"Introduce el valor {i+1}: "))
        contador = contador + 1


        if(contador == 0):
            positivo = valorNumero
            negativo = valorNumero
            cero = valorNumero
        elif(valorNumero< 0):
            negativo= negativo + 1
        elif(valorNumero>0):
            positivo = positivo+1
        elif(valorNumero == 0):
            cero = cero + 1
    else:
        print("\n\n===============================")
        print(f"| Positivos: {positivo}")
        print(f"| Negativos: {negativo}")
        print(f"| Cero: {cero}")
        print("====================================\n\n")
    