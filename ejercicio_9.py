fecha_de_nacimiento = input("Escribe tu fecha de nacimiento (por ejemplo dd/mm/aaaa ): ")
separados = fecha_de_nacimiento.split("/")
dia = separados[0]
mes = separados[1]
año = separados[2]
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")