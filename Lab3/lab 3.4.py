#Python: inheritance
#Inheritance in kazakh is "мұрагерлік"

# Ата-аналық класс: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Менің атым {self.name}, жасыма {self.age}.")

#New class. We take inheritance from Person class
class Student(Person):
    def __init__(self, name, age, student_id):
        #using super class we call the init method
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        # Person классының introduce әдісін шақырамыз
        super().introduce()
        # Содан кейін студентке тән ақпаратты қосамыз
        print(f"Менің студенттік нөмірім: {self.student_id}")

#Creating object
student1 = Student("Ayan", 19, "S12345")
student1.introduce()
