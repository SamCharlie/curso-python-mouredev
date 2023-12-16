### HIHGER ORDER FUNCTIONS##

# Funciones que reciben como parámetro otra función

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, function):
    return function(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one)) 
print(sum_two_values_and_add_value(5, 2, sum_five))

### closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1) # add_closure es una función
print(add_closure(5)) # 16

print(sum_ten(5)(1)) # 16

### built-in higher order functions ###

numbers = [2, 5, 10, 21, 3, 30]

# map

def multiply_by_two(value):
    return value * 2

print(list(map(multiply_by_two, numbers))) # [4, 10, 20, 42]
print(list(map(lambda value: value * 2, numbers))) # [4, 10, 20, 42]

# filter

def filter_greater_than_ten(value):
    return value > 10

print(list(filter(filter_greater_than_ten, numbers))) # [21]
print(list(filter(lambda value: value > 10, numbers))) # [21]

# reduce

from functools import reduce

def sum_two_values(first_value, second_value): 
    print(f'{first_value} + {second_value}')
    return first_value + second_value

print(reduce(sum_two_values, numbers)) 