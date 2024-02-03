maximo = int(input("Numero de asteriscos maximo por fila :"))

for i in range(1, maximo + 1):
    print("* " * i)

for i in range(maximo - 1, 0, -1):
    print("* " * i)