#Variables

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funciones del sistema
print(len(my_variable)) #cuenta cuantos caracteres tiene un str

#Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Carlos", "Salazar", "SamCharlie", 27
print("Me llamo", name, surname, "mi edad es:", age, "y mi alias es:", alias)

#Imputs
'''
name = input('Cual es tu nombre: ')
age = input('Cuantos años tienes?: ')

print(name)
print(age)
'''

#Cambiamos de tipo
name = 123
age = "Salazar"

print(name)
print(age)

#Forzamos el tipo
address: str = "Mi direccion"
# address = 56 
print(type(address))