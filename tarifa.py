# la categoria de la voleta es:
# General : 50.000
# VIP : 100.000
# Segun la edad se dan descuentos:
# Menor de 12 años, recibe un 50% de descuento
# Mayor o igual a 60 años, recibe un 30% de descuento

# Pide al usuario su nombre, edad y la categoría y calcula el precio final de su entrada.

def catergoria(c):
    if c == "General":
        return int(50000)
    else:
        return int(100000)


def descuento(D):   # ver cuanto % de descuento tiene la persona
    if D < 12:
        return "50%"
    elif D >= 60:
        return "30%"
    else:
        return "0%"


def precio_segun_descuento(d, v):   # calcular los valores con descuento
    if d == "50%":
        return v * 0.50
    elif d == "30%":
        return v * 0.70
    else:
        return v


def resultados(N, C, P):
    return f"el usuario {N} con su categoria {C} paga un total de {P}"


nombre_usuario = input("Cual es tu nombre?")   

edad_usuario = int(input("Cual es tu edad?"))

Categoria_voleta = input("General o VIP?")

precio_segun_categoria = catergoria(Categoria_voleta)

descuento_edad = descuento(edad_usuario)

precio_total = precio_segun_descuento(descuento_edad, precio_segun_categoria)

resultado = resultados(nombre_usuario, Categoria_voleta, precio_total)

print (resultado)