correo = input("Introduce tu correo electrónico: ")
nombre = correo.split('@')[0]
nuevo_correo = nombre + "@ceu.es"
print(f"Tu nuevo correo es: {nuevo_correo}") 