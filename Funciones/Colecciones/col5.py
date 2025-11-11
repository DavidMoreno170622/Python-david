lista_marcas = ["Lenovo", "HP", "Dell"]
pasillotup = ("A",4)
items = {"raton","teclado", "webcam"}

inventario = {
    "Portatiles" : lista_marcas,
    "Ubicacion_almacen" : pasillotup,
    "Componentes_extra" : items
}

print(inventario)

inventario["Portatiles"].append("Asus")

print(inventario)
