pregunta = input("el precio de un producto en euros con dos decimales: ")
euros, centimos = pregunta.split(".")
print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")