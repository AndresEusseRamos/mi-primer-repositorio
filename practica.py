def calcular_descuento(descuento):
    if descuento < 100:
        return "No aplica descuento"
    else:
        return "Aplica descuento"
descuento = int(input("cual es el valor del producto?"))
resultado = calcular_descuento(descuento)
print (resultado)