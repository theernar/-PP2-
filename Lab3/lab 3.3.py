#Python: Classes and Objects

#What is the classes and objects? I asked from AI and answer in kazakh: 
#Класс – белгілі бір типтегі объектілерді жасауға арналған шаблон немесе үлгі.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age  

    def introduce(self):
        print(f"Менің атым {self.name}, жасым {self.age}.")

person1 = Person("Erlan", 20)
person1.introduce()  # Нәтиже: Менің атым Erlan, жасым 20.


class KBTU: 
    def __init__(self, lessons, lecturer):
        self.lessons = lessons #There are lessons in KBTU
        self.lecturer = lecturer #There are teachers of lessons 
        
    def university(self):
        print(f"Lessons is: {self.lessons}, lecturer: {self.lecturer}")
        
information = KBTU(["PP1", "PP2", "OOP"], "Tamiris Abildayeva")
information.university()

#Explain my code:

#First of all: i created new class that save informations about KBTU. Name of class is: KBTU
#Second: Through the constructor (__init__ method), you accept the necessary information when an object is created and store it in the object attributes.

class name: 
    def __init__(self, name, surname):
        self.firstname = name
        self.lastname = surname
    
    def myfunction(self):
        print(self.firstname + " " + self.lastname)
        
x = name("Yernar", "Abdizhaleluly")
y = name("Tamiris", "Abildayeva")
z = name("Islam", "Menlidai")
x.myfunction()
y.myfunction()
z.myfunction()