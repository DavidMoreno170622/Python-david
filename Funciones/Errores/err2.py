def convertir_a_numeros(lista_str):
    numeros = []
    for i in lista_str:
        try:
            num = int(i) 
            

        except ValueError:
            print(f"Error: {i} no es un número válido.")

        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {type(e).__name__} -> {e}")
        
        else:
            numeros.append(num)
    return numeros



final = convertir_a_numeros(["hola","10", "20", "tres", "40", "-5", "j"])

print(final)