#Thirteen exercise: Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. 
#This is how it should work when run in a terminal:


import random
def secret_number():
    print("Сәлем. Сенің есімің кім?")
    name = input()
    secret_number = random.randint(1, 20) #Please choose a random number's code:
    print("Мен 1-20 аралығында бір сан ойлап отырмын.")
    guesses_taken = 0

    while True: #This loop continues until the number is correct, stopping in the loop if the number is incorrect.
        guess = int(input("Ойымдағы санды тауып көр: ")) #The user enters a number
        guesses_taken += 1 #We add numbers to our capabilities(попытки)
        if guess < secret_number:
            print("Сенің енгізген саның менің ойымдағы санымнан төмен")
        elif guess > secret_number:
            print("Сенің енгізген саның менің ойымдағы санымнан жоғары")
        else:
            print("Жарайсың! Ойымдағы санды таптың")
            break  

secret_number()