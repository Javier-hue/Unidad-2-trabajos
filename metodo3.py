lista_compras = []

def mostrar_menu():
    print("\n--- Menú de Lista de Compras ---")
    print("1. Agregar artículo")
    print("2. Quitar artículo")
    print("3. Mostrar lista de compras")
    print("4. Salir")

def agregar_articulo(articulo):
    lista_compras.append(articulo)
    print(f'Artículo "{articulo}" agregado a la lista.')

def quitar_articulo(articulo):
    if articulo in lista_compras:
        lista_compras.remove(articulo)
        print(f'Artículo "{articulo}" eliminado de la lista.')
    else:
        print(f'El artículo "{articulo}" no está en la lista.')

def mostrar_lista():
    if lista_compras:
        print("\nLista de compras actual:")
        for i, articulo in enumerate(lista_compras, 1):
            print(f"{i}. {articulo}")
    else:
        print("\nLa lista de compras está vacía.")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        articulo = input("Escribe el nombre del artículo que deseas agregar: ")
        agregar_articulo(articulo)

    elif opcion == "2":
        articulo = input("Escribe el nombre del artículo que deseas quitar: ")
        quitar_articulo(articulo)

    elif opcion == "3":
        mostrar_lista()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor elige una opción entre 1 y 4.")