def obtener_indice_seguro(secuencia, indice_a_buscar):

    try:
        if type(indice_a_buscar) is not int:
            raise TypeError ("El índice debe ser un entero.")
        secuencia[indice_a_buscar]
    
    except IndexError:
        print("Error: Índice fuera de rango.")

    except TypeError:
        print("ERROR: El índice debe ser un entero.")
    
    else:
        print(secuencia[indice_a_buscar])
    finally:
        print(" --- Búsqueda de índice finalizada ---")

mi_tupla = ("a", "b", "c")
obtener_indice_seguro(mi_tupla, 1)
obtener_indice_seguro(mi_tupla, 10)
obtener_indice_seguro(mi_tupla, "dos")