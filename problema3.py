pares = 0
impares = 0

while True:
    numero = input("Ingrese un número o 'fin' para terminar: ")
    if numero == "fin":
        break
    try:
        numero = int(numero)
    except ValueError:
        print("Por favor, ingrese un número válido o 'fin' para terminar.")
        continue
    # Si el número es válido, comprobamos si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Imprimimos la cantidad de números pares e impares ingresados
print(f"Ha ingresado {pares} números pares y {impares} números impares.")