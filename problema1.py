numeros = []

for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        numeros.append(n)

print(numeros)
