perfect_studying_hours = 2
user_name = input("cual es tu nombre?")
work_hours = int(input("horas de trabajo?")) 
studying_hours = int(input("horas de estudio? ")) 
time = work_hours + studying_hours
print(f"hola {user_name} usas {time} horas en tu dia")
if studying_hours >= perfect_studying_hours:
    print ("muy buen trabajo")
else:
    print ("hay que mejorar")