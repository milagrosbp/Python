#Escribir un programa que lea por teclado 10 números y muestre en pantalla
#el más grande, el más pequeño y la media de N los números ingresados

valorMayor = 0
valorMenor = 0
valorMedia = 0
contador = 0

while contador != 10:

    for i in range(10):
        valorNum = int(input("Digite un número: "))
        contador = contador + 1

        if(contador == 1):
            valorMayor = valorNum
            valorMenor = valorNum

        elif(valorNum > valorMayor):
            valorMayor = valorNum

        elif(valorNum < valorMenor):
            valorMenor = valorNum

        valorMedia = valorMedia + valorNum
    else:
        valorMedia = round(valorMedia/contador)
        print("\n\n===============================")
        print(f"| El mas grande es: {valorMayor}")
        print(f"| El mas pequeño es: {valorMenor}")
        print(f"| La media es: {valorMedia}")
        print("====================================\n\n")
    