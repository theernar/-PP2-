#Python: iterator and generator (third exercise)
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def my_number(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield str(i)

n = int(input("Enter the number: "))
res = ",".join(my_number(n))
print(res)