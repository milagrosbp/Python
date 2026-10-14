#Escribir un programa que cree un diccionario simulando una cesta de la compra. El
#programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que
#el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y
#el coste total, con el siguiente formato


import os

carrito = {}
total = 0

while True:
    os.system("cls")
    producto = input("Introduce un producto: ")
    precio = float(input("Introduce el precio del producto: "))
    carrito[producto] = precio

    terminar = input("¿Quieres seguir añadiendo artículos a la lista (S/N)?").upper()

    if terminar == 'S':
        pass
    elif terminar == 'N':
        break
    else:
        print("Debes ingresar una opción válida.")
        input("Presiona Enter para continuar...")
    
print("Carrito de compras:")
for item, precio in carrito.items():
    print(f"{item} - ${precio}")
    total += precio
    
print(f"\nTotal a pagar: ${total:.2f}")
print("Finalizado.")