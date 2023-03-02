"""
Lee un número por teclado e indica si es divisible por
3. Si no lo es, también debemos indicarlo
"""
numero = int(input("Ingrese un número, le diré si es divisible o no por 3:"))

if(numero % 3 == 0):
    print("El número es divisible por 3!")
else:
    print("El número no es divisible por 3! 😞 ")