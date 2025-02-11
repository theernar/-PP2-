#Python: iterator and generator (second exercise)
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_number (n): #We opened function - even_numbers
    for i in range (0,n+1): #for loop для iterations
        if i % 2 == 0:
            yield str(i) #yield functions is like return and print. We need str for using join operator
             
n = int(input("Enter a number: "))
result = ",".join(even_number (n))
print("Even numbers: ", result)