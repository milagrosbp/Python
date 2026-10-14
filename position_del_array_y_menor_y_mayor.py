#8- Realizar un programa que, tras ingresar seis números enteros en un array,
#determine la posición del array en la que se encuentra el máximo valor

numeros = []
print("Introduce 6 números enteros: ")

for i in range(6):
    while True:
        try: 
            num = int(input(f"Número {i + 1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")
max = max(numeros)
posicion = numeros.index(max)

print("\n--- Resultados ---")
print(f"Lista ingresada: {numeros}")
print(f"El valor máximo es: {max}")
print(f"Se encuentra en el índice: {posicion} (posición {posicion + 1})")