#FUNCTIONS

def my_dunction ():
    print("Esto es una funcion")

my_dunction()

def sum_two_vaules (first_number, secund_number):
    print(first_number + secund_number)

sum_two_vaules(5, 7)
sum_two_vaules("5", "7")
sum_two_vaules(6545, 5566)
sum_two_vaules(1.6, 5.1)

def sum_two_vaules_with_return (first_vaule, secund_vaule):
    return first_vaule + secund_vaule

my_result = sum_two_vaules_with_return(10, 5)
print(my_result)

print(sum_two_vaules_with_return(10, 10))

my_result = sum_two_vaules(5, 7)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print("Carlos", "Salazar")
print_name(surname = "Salazar", name = "Carlos")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Carlos", "Salazar", "Samcharlie")
print_name_with_default("Carlos", "Salazar")

def print_upper_text(*texts):
    for text in texts:
        print(text.upper())


print_upper_text("Hola")
print_upper_text("Hola", "Hola2")
print_upper_text("Hola", "Hola2", "Hola3")