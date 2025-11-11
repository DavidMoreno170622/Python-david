def calcularMaxMin(lista):
    if not lista:
        print("Pon algo")
    else:
        return min(lista),max(lista)

num1="1"

numeros=[]

while True:
    if num1.isnumeric():
        seguir = input("Me dices un numero? (s/n): ")
        if seguir == "s":
            num1 = input("Dime numeros: ")
            numeros.append(num1)
            print(numeros)
        if seguir == "n":
            print("Chao")
            minimo,maximo=calcularMaxMin(numeros)
            print("El numero mas pequeño es: ",minimo)            
            print("El numero mas grande es: ",maximo)
            break
        elif seguir == "n" and numeros == "":
            print("Esta vacio")
        else:
            print("Tiene que ser (s/n)")
    else:
        print("Tiene que ser un numero")
        break


