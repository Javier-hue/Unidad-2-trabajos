longitud = int(input("Ingresa la cantidad de nombres que deseas agregar: "))

dicc = {}

for i in range(longitud):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    dicc[f"nombre_{i + 1}"] = nombre

print("\nNombres ingresados:")
for clave, valor in dicc.items():
    print(f"{clave}: {valor}")

def eliminar(dicc, clave):
    if clave in dicc:
        del dicc[clave]
        print(f"Elemento eliminado: {clave}")
    else:
        print(f"La clave '{clave}' no existe en el diccionario.")

while True:
    print("\nContenido actual del diccionario:")
    for clave, valor in dicc.items():
        print(f"{clave}: {valor}")
    
    opcion = input("\n¿Deseas eliminar algún nombre? (si/no): ").lower()
    if opcion == "no":
        break
    elif opcion == "si":
        clave = input("Ingresa la clave del nombre que deseas eliminar (por ejemplo, nombre_1): ")
        eliminar(dicc, clave)
    else:
        print("Opción no válida. Intenta de nuevo.")

print("\nDiccionario final:")
for clave, valor in dicc.items():
    print(f"{clave}: {valor}")