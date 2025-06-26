registros = []
while True:
    nombre = input("Ingresa el nombre: ")
    if nombre.lower() == "salir":
        break

    telefono = input("Ingresa el teléfono: ")
    if telefono.lower() == "salir":
        break

    semestre = input("Ingresa el semestre: ")
    if semestre.lower() == "salir":
        break

    registros.append([nombre, telefono, semestre])

print("\n DATOS RECOLECTADOS:")
for registro in registros:
    print(registro)
