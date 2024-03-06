### FILE HANDLING ###

# .txt file

import os

txt_file = open("Intermedio/my_file.txt", "w+") #Leer y escribir
txt_file.write("\nMi nombre es Carlos\nMi apellido es Salazar\n28 años\ny estoy eprendiendo Python")

#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nY tambien tengo hambre")

print(txt_file.readline())

txt_file.close()

with open("Intermedio/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY esposo")

#os.remove("Intermedio/my_file.txt")