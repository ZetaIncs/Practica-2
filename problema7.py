def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    raiz = int(n ** 0.5)
    for i in range(3, raiz + 1, 2):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

