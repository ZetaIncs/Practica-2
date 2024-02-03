# Función para contar la cantidad de veces que un dígito aparece en un número entero
def contar_digito(numero, digito):
    numero = str(numero)
    digito = str(digito)
    cantidad = numero.count(digito)
    return cantidad

# Ejemplo de uso de la función
numero = input("Ingrese el número a evaluar:")
digito = input("Ingrese el digito a contar en el numero:")
cantidad = contar_digito(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero} es: {cantidad}")
