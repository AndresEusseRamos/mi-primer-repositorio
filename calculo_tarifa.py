# miramos si la persona aplica o no descuento
def descuento(horas):
    if horas >= 5:
        return "Aplica descuento"
    else:
        return "No aplica descuento"


# multiplicamos segun si es moto o carro
def clase_vehiculo(clase, h):
    if clase == "Moto":
        return h * 2000
    else:
        return h * 4000


# si aplica descuento sacamos el 10%
def totalidad_con_descuento(totalidad, p):
    if totalidad == "Aplica descuento":
        return p * 0.90
    else:
        return p


# damos la informacion completa
def cobro_tarifa (nombre, tipo, aplica, pago):
    return f"el usuario {nombre} con vehiculo de tipo {tipo} {aplica} y paga un total de {pago}"


nombre_usuario = input("nombre de usuario?")
tipo_vehiculo = input("Moto o Carro?")
horas_registradas = int(input("horas registradas?"))


aplicacion_descuento = descuento(horas_registradas)   # aqui me dice si si aplica o no

pago_usuario = clase_vehiculo(tipo_vehiculo, horas_registradas) # aqui si es moto o carro dice cuanto paga segun las horas

pago_descuento = totalidad_con_descuento(aplicacion_descuento, pago_usuario) # aqui aplica el descuento si hace falta

resultado = cobro_tarifa(nombre_usuario, tipo_vehiculo, aplicacion_descuento, pago_descuento)

print(resultado)