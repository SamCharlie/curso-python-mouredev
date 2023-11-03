# SETS

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario

my_other_set = {"Carlos", "Salazar", 27}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Samitas")
print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("Samitas")
print(my_other_set) # un set no admite datos repetidos

print("Carlos" in my_other_set)
print("Carlo" in my_other_set)

my_other_set.remove("Carlos")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set

my_set = {"Carlos", "Salazar", 27}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"java", "C#"}))

print(my_new_set.difference(my_set))