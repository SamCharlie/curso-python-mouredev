#CLASES

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name= name
        self.surname = surname

my_person = Person("Carlos", "Salazar")
print(f"{my_person.name} {my_person.surname}")

class Person2:
    def __init__(self):
        self.name= "Carlos"
        self.surname = "Salazar"

my_person2 = Person2()
print(f"{my_person2.name} {my_person2.surname}")

class Person3:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name #Propiedad privada

    def get_name (self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} Esta caminando")

my_person3 = Person3("Carlos", "Salazar")
print(my_person3.full_name)
print(my_person3.get_name())
my_person3.walk()

my_other_person = Person3("Carlos", "Salazar", "Samcharlie")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de leon El loco de los perros"
print(my_other_person.full_name)