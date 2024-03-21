### Regular Expressions ###

import re 

my_string = "Esta es la leccion número 7: Expresiones regulares"
my_other_string = "Esta no es la leccion número 6: Manejo de ficheros"

match = re.match("Esta es la leccion",my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = print(re.match("Esta es la leccion",my_other_string))
print(match)
start, end = match.span()
print(my_string[start:end])

print(re.match("Expresiones regulares",my_string))