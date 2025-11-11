def temp_media(minima,maxima):   
    return (maxima+minima)/2



dias = int(input("Cuantos dias quieres? "))


for dias in range(dias):
    temp_min = int(input("Introduce la temperatura minima: "))
    temp_max = int(input("Introduce la temperatura maxima: "))
    print("La temperatura media es: ",temp_media(temp_min,temp_max))
