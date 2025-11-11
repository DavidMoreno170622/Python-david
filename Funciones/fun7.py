def ConvertirEspacio(texto):
    acum=""
    for letra in texto:
        acum+=letra+" "
    return acum

nombre = input("Dime un nombre: ")

nomEsp=ConvertirEspacio(nombre)


print(nomEsp)

