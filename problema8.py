# Función para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        print("El número debe ser un entero no negativo.")
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

numero = int(input("Ingrese el numero a evaluar su factorial:"))
print(f"El factorial de {numero} es {factorial(numero)}.")
