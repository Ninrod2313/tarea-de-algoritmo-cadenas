productos = input("Escribe los nombres de los productos separados por comas: ")
lista = productos.split(",")
for producto in lista:
    print(producto.strip())