def siguiente_fibonacci(a, b):
    c = a + b
    return c

# Definimos una función para mostrar la serie de Fibonacci entre 0 y 50
def mostrar_fibonacci():
    a = 0
    b = 1

    print(a)
    while b <= 50:
        print(b)
        c = siguiente_fibonacci(a, b)
        a = b
        b = c

mostrar_fibonacci()
