"""
Escriba un programa que lea un número negativo e imprima el
número y el positivo del mismo
"""
numero = float(input("Ingrese un número negativo: "))
if (numero >= 0):
    numero=float(input("No ingresaste un número negativo, ingresalo por favor: "))

if(numero < 0):
    positivo = numero * -1
    print("El valor ingresado es",numero,"y su positivo es",positivo)
else:
    print("No ingresaste un número negativo, programa finalizado")