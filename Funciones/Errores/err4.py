def sumar_lista(lista):
    total = 0
    try:
        for i in lista:
            total += i

    except TypeError:
        print("Error: La lista contenía un tipo de dato no numérico.")
        return None

    else:
        print("Suma completada con éxito.")
        return total

print(sumar_lista([1, 2, 4]))