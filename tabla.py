#Tabla de multiplicar

while True:
    try:
        numero = int(input("Introduce un número entero: "))
        limite = int(input("Introduce hasta qué número deseas multiplicarlo (límite): "))
        if limite < 1:
            print("Por favor, introduce un número mayor o igual a 1.")
        break
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")


print(f"\nTabla de multiplicar del {numero}:")
print("-" * 30)

for i in range(1, limite+1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("-" * 30)
print("¡Finalizado!")