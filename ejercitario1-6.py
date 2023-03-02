"""
Se desea un programa para convertir metros a pies y pulgadas
(1 metro = 39.37 pulgadas, 1 pie = 12 pulgadas)
"""
metro = float(input("Introduce tu número de metros a convertir: "))
pulgadas = 39.37 * metro
pie = pulgadas / 12

print("De",metro," metros es igual a", pulgadas,"pulgadas y a",pie, "pies")