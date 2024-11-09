class Stack:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def apilar(self, item):
        self.pila.append(item)

    def mostrar_pila(self):
        print("Elementos en la pila:")
        for elemento in self.pila:
            print(elemento)

if __name__ == "__main__":
    stack = Stack()

    while True:
        opcion = input("Ingrese una opción:\n1. Agregar un número\n2. Mostrar la pila\n3. Salir\n")

        if opcion == '1':
            numero = int(input("Ingrese un número: "))
            stack.apilar(numero)
        elif opcion == '2':
            if stack.esta_vacia():
                print("La pila está vacía")
            else:
                stack.mostrar_pila()
        elif opcion == '3':
            break
        else:
            print("Opción inválida")