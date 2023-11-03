# LOOPS

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("El bucle a terminado")

while my_condition < 20:
    my_condition += 2

    if my_condition == 16:
        print("Se detiene la ejecucion")
        break

    print(my_condition)

print("El bucle a terminado")

# FOR

my_list = [35, 25, 65, 74, 15, 65, 14, 53]

for element in my_list:
    print(element)

    if element == 15:
        break
else:
    print("El bucle for a finalizado")

my_dict = {
    "Nombre":"Carlos", 
    "Apellido":"Salazar", 
    "Edad":35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.75
}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionaria a terminado")

print("La ejecucion continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue  #Continua deteniedo desde aqui y empezando desde el for
else:
    print("El bucle for para diccionaria a terminado")