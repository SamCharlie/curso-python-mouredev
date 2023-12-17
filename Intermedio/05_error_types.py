### Error Types ###

# SyntaxError

#print "Hello World"
print("Hello World") # SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World")?

# NameError

name = "Calos" 
print(name) 
#print(name2) # NameError: name 'name2' is not defined

# indexError

my_list = [1,2,3,4,5]
#print(my_list[6]) # IndexError: list index out of range

# moduleNotFoundError

#import my_module # ModuleNotFoundError: No module named 'my_module'

# attributeError

my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)
#my_list.append(6,7) # AttributeError: 'list' object has no attribute 'append'   
