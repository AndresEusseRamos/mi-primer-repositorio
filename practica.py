edades = [13,16,11,10,0,18,25,42]
for elemento in edades:
    if elemento == 0:
        print ("ERROR")
    elif elemento < 18:
        print ("Menor de edad")
    else:
        print ("Mayor de edad")