class Colas:
    def __init__(self):
        self.lista = [] 

    def agregar(self, elemento):
        self.lista.append(elemento)  

    def front(self):
        if self.lista:
            return self.lista[0] 
        else:
            return None  

    def back(self):
        if self.lista:
            return self.lista[-1] 
        else:
            return None  

cola = Colas()
cola.agregar(10)
cola.agregar(20)
cola.agregar(30)

print("Primer elemento:", cola.front())
print("Último elemento:", cola.back())  