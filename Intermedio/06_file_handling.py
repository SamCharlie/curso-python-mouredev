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

#os.remove("Intermedio/my_file.txt")