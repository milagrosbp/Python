#10-Realizar un programa que tras asignar 10 valores enteros en un array, determine
#las posiciones del array en las que se encuentran el máximo y el mínimo valor.

numeros = []
print("Introduce 10 números enteros: ")

for i in range(10):
    while True:
        try: 
            num = int(input(f"Número {i + 1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

max = max(numeros)
min = min(numeros)


print("\n--- Resultados ---")
print(f"El valor menor es: {min}, se encuentra posicionado en {numeros.index(min)+1}")
print(f"El valor mayor es: {max}, se encuentra posicionado en {numeros.index(max)+1}")