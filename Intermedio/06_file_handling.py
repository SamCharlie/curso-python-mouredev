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

# .json file 

import json

json_file = open("Intermedio/my_file.json", "w+")

json_test = {
    "name":"Carlos", 
    "surname":"Salazar", 
    "age":35, 
    "languages":["Python", "swift", "kotlin"],
    "website":"samitas.com"}

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("Intermedio/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv
csv_file = open("Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Carlos", "Salazar", 28, "Python", "samitas.com"])

csv_file.close()

with open("Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

#import xlrd # Debe instalarse el modulo

# .xml file

import xml 