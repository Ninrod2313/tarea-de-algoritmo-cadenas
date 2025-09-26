nombre = input("escribe tu nombre:")
nombreenmayusculas = nombre.upper()
cantidad_letras = len(nombre.replace(" ", ""))
print(f"{nombreenmayusculas} tiene {cantidad_letras} letras")