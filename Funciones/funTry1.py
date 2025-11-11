# Crea una función contar_palabras que reciba un texto y devuelva:
# cuántas palabras hay
# la palabra más larga
# la palabra más corta

print("PRUEBA1")

def contar_palabras(texto):
    lista = list(texto)
    contador = len(lista)
    corta = min(lista, key=len)
    larga = max(lista, key=len)
    return contador,larga,corta

frase = input("Dime nombres: ").split()

conta,primer,ultim = contar_palabras(frase)

print(f"Hay {conta} palabras")
print(f"Esta es el primer nombre {primer}")
print(f"Esta es el ultimo nombre {ultim}")

print("PRUEBA2")

#Crea una función calcular que reciba un operador ("+", "-", "*", "/") y cualquier cantidad de números con *args.

