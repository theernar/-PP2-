#First exercise: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class StringManipulator: #the name of the class
    def getString(self): #getstring is the name of the function
        self.text = input("Мәтінді енгізіңіз: ") 

    def printString(self): #printString is the name of the function
        print("Бас әріптердегі мәтін:", self.text.upper())

manipulator = StringManipulator() #manipulator is just object. it can now use all functions (methods) in the StringManipulator class.
manipulator.getString() #To enter the string
manipulator.printString()  #To print the string with upper case characters