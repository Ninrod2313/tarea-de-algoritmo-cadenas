telefono = input("Escribe tu número de teléfono (por ejemplo +34-123456789-33): ")
separado = telefono.split("-")
sin_prefijo = separado [1]
print(f"el numero sin el prefijo ni la extencio es: {sin_prefijo}")