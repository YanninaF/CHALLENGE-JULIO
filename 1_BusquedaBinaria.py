def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return True
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False


lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


numeros_a_buscar = [5, 10, 15, 20]

# búsqueda
for numero in numeros_a_buscar:
    if busqueda_binaria(lista_ordenada, numero):
        print(f"El número {numero} está en la lista.")
    else:
        print(f"El número {numero} no está en la lista.")
