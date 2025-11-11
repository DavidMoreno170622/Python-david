def EscribirCentrado(texto):
    longitud=len(texto)
    res = " " * round((80-longitud)/2) 
    sub = longitud * "="
    print(res,texto)
    print(res,sub)

texto = input("Dime algo: ")
EscribirCentrado(texto)