def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        # Encontrar el índice del elemento más pequeño en el resto de la lista
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiar el elemento más pequeño encontrado con el primer elemento no ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

lista_original = [7, 9, 2, 3, 5]
lista_ordenada = ordenamiento_seleccion(lista_original)
print("Lista original:", lista_original)
print("Lista ordenada:", lista_ordenada)
