class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def insertar(self, elemento, prioridad):
        self.cola.append((prioridad, elemento))
        self.cola.sort(reverse=True)  # Ordenar la lista por prioridad en orden descendente

    def eliminar(self):
        if self.cola:
            return self.cola.pop(0)[1]  # Eliminar y devolver el elemento con la mayor prioridad
        return None

    def __str__(self):
        return str(self.cola)

cp = ColaPrioridad()

# Insertar 5 elementos con sus prioridades
cp.insertar("Elemento 1", 3)
cp.insertar("Elemento 2", 1)
cp.insertar("Elemento 3", 4)
cp.insertar("Elemento 4", 2)
cp.insertar("Elemento 5", 5)

print("Cola de prioridad después de insertar 5 elementos:")
print(cp)

# Eliminar 5 elementos
print("\nEliminando elementos:")
for _ in range(5):
    elemento = cp.eliminar()
    if elemento:
        print(f"Elemento eliminado: {elemento}")
    else:
        print("La cola está vacía")

print("\nCola de prioridad después de eliminar 5 elementos:")
print(cp)
