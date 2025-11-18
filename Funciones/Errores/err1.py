def dividir(a,b):
    resul = a / b
    return resul
try:
    num = int(input("Dime un numero: "))
    num2 = int(input("Dime otro numero: "))
    total = dividir(num,num2)

except ValueError:
# Se ejecuta SÓLO si int(num_str) falla
    print("Error: Debes introducir un NÚMERO entero.")

except ZeroDivisionError:
# Se ejecuta SÓLO si intentas dividir por 0
    print("Error: No se puede dividir por cero.")
except Exception as e:
# 'Exception' es una captura genérica (siempre al final)
# 'as e' guarda el error en la variable 'e'
    print(f"Ha ocurrido un error inesperado: {type(e).__name__} -> {e}")
else:
    print(total)