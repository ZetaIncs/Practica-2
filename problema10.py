meses = [
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]

fecha = input("Ingrese una fecha en formato mes/día/año o mes,día,año: ")

if "/" in fecha:
  partes = fecha.split("/")
else:
  partes = fecha.split(",")

if partes[0] in meses:
  partes[0] = str(meses.index(partes[0]) + 1)

if " " in partes[1]:
  partes[1] = partes[1].strip()

partes = [int(p) for p in partes]

fecha_nueva = f"{partes[2]:04}-{partes[0]:02}-{partes[1]:02}"

print(fecha_nueva)
