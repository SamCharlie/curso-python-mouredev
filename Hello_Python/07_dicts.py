# DICTIONARIES

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre":"Carlos", "Apellido":"Salazar", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Carlos", 
    "Apellido":"Salazar", 
    "Edad":35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.75
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

my_dict["Calle"] = "Chanchito"
print(my_dict["Calle"])

del my_dict["Calle"]
print(my_dict)

print("Carlos" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Salazar", "Carlos"))
print(my_new_dict)