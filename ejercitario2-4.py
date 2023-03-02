"""
Un individuo desea invertir su capital en un banco y
desea saber cuánto dinero ganará después de un
mes, si el banco paga a 2% de interés mensual
"""
capital = int(input("Ingrese su depósito de capital: "))
interes = 2/100
ganancia = capital * interes
print("""
Hola, tu ganancia es de""", ganancia,"""al cabo de un mes
En total tienes """, (ganancia + capital))
