def obtener_valor_dict(diccionario, clave):
    try:
        print(diccionario[clave])
    
    except KeyError:
        #Si la clave que pide no existe
        print("Error: La clave '{clave}' no existe.")
    except TypeError:
        #La clave intoducida es un tipo que no puede ser una clave, como una lista
        print("Error: La clave usada tiene un tipo no válido (ej. una lista).")    

mi_dict = {"nombre": "Ana", "edad": 25}
#Imprime 25
obtener_valor_dict(mi_dict, "edad")
#Error de clave
obtener_valor_dict(mi_dict, "apellido")
#Error de tipo
obtener_valor_dict(mi_dict, ["nombre"])