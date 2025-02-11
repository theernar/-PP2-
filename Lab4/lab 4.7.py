#Python: iterator and generator (first exercise)
#Create a generator that generates the squares of numbers up to some number

def square_generator(n): #We opened function - square generator
    for i in range(1, n + 1): 
        print(i ** 2)

num = int(input("Шек енгізіңіз: "))
square_generator(num)