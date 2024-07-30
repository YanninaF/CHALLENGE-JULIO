def eliminar_duplicados(lista):
    lista_sin_duplicados = [] #creamos una lista vacia, donde se va guardar los elementos unicos

    
    for elemento in lista: # itera sobre cada elem de la listaoriginal
        if elemento not in lista_sin_duplicados:#si no esta en la lista de elem unico, entonces se añáde
            lista_sin_duplicados.append(elemento)

    return lista_sin_duplicados

lista_original = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print("Lista original:", lista_original)
print("Lista sin duplicados:", lista_sin_duplicados)
