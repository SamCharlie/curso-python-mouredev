### Regular Expressions ###

import re 

#match

my_string = "Esta es la leccion número 7: Expresiones regulares"
my_other_string = "Esta no es la leccion número 6: Manejo de ficheros"

match = re.match("Esta es la leccion",my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

# match = print(re.match("Esta es la leccion", my_other_string))
# if match == None:
#     print(match)
#     start, end = match.span()
#     print(my_string[start:end])

print(re.match("Expresiones regulares",my_string))

#search

search = re.search("Esta es la leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

#findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

#split

print(re.split(":", my_string))

#sub

print(re.sub("Expresiones regulares", "RegEx", my_string))

#Patterns 

pattern = r"[lL]eccion"
print(re.findall(pattern), my_string)