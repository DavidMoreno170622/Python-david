def es_multiplo(numero, multiplo):

    if numero % multiplo == 0:
        return True
    else:
        return False

numero = input("Dime el primer numero: ")
multiplo = input("Dime el segundo numero: ")

if numero.isnumeric() and multiplo.isnumeric():

    numero=int(numero)
    multiplo=int(multiplo)
    mult = es_multiplo(numero,multiplo)
    if mult == True:
        print("Son multiplos")
    else:
        print("No son multiplos")
else:
    print("Los numeros tienen que ser enteros")
