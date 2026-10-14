#Haz un programa que reciba un string y lo imprima carácter por carácter.
#Make a program that receives a string and prints it character by character.


import time
texto = input("Introduce una cadena de texto: ")

for i in texto:
    print(i)
    time.sleep(1)

