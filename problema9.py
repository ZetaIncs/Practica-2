texto = input("Ingrese una cadena de texto: ")

nuevo_texto = ""

for c in texto:
    c = c.lower()
    if c in "aeiou":
        continue
    else:
        nuevo_texto = nuevo_texto + c

print("El texto sin vocales es:", nuevo_texto)
