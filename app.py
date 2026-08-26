nombre_usuario = input("Cual es tu nombre?")
edad_usuario = int(input("Cual es tu edad?"))
if edad_usuario <= 0:
    print ("EROR: Edad NO Valida")
elif edad_usuario < 18:
    print (f"HOLA {nombre_usuario}. eres menor de edad. !A seguir pracicando!")
else:
     print (f"HOLA {nombre_usuario}, acceso concedido al sistema backend")