# Definimos una función para pedir los datos de un alumno
def pedir_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    # Pedimos las tres notas del alumno
    for i in range(1, 4):
        while True:
            try:
                nota = int(input(f"Ingrese la nota {i} del alumno: "))
            except ValueError:
                print("Por favor, ingrese una nota válida.")
                continue
            notas.append(nota)
            break
    return {"Alumno": nombre, "Notas": notas}

# Definimos una función para mostrar el listado de alumnos
def mostrar_listado(listado):
    print("Listado de alumnos y sus notas")
    for alumno in listado:
        print(f"{alumno['Alumno']}: {alumno['Notas']}")

listado = []

# Pedimos al usuario que ingrese el número de alumnos
n = int(input("Ingrese el número de alumnos: "))

for i in range(n):
    listado.append(pedir_alumno())

mostrar_listado(listado)
