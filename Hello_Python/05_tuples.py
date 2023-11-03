# TUPLES

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (27, 1.75, "Carlos", "Salazar", "Salazar")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Salazar"))
print(my_tuple.index("Carlos"))
print(my_tuple.index("Salazar"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Samitas"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

