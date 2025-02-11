#W3SCHOOL: PYTHON ITERATORS
#In this file i will solve problems from W3SCHOOL and analyze teory informations.

#TEORY INFORMATIONS: 
#Итераторлар — деректердің жиынтығын (lists, tuples, strings және т.б.) бір элементтен
#екіншісіне өту арқылы қайталайтын Python-ның негізгі құралдарының бірі.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) #Iter функциясы бұл жерде әр элементті айнымалыға тіркеп отырады. 

print(next(myit)) #Next бұл жерде әр элементті бірінен кейін бірін шығарып отырады. 
print(next(myit))
print(next(myit))

myword = "Programming"
myitword = iter(myword)
print(next(myitword)) #Next арқылы әр элементті бірінен кейін бірін шығарамыз. Бұл жердегі элементтер ол әріптер. 
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))
print(next(myitword))

myset = ["BMW", "Mercedes", "Honda"]
myitset = iter(myset)
print(next(myitset))
print(next(myitset))
print(next(myitset))

mytuple1 = ("BMW", "Mercedes", "Honda")
for x in mytuple1:
    print(x)
    
    
class MyNumbers: #MyNumbers деген класс аштық. 
  def __iter__(self): #Self - белгілі бір енгізетін мәніміз. 
    self.a = 1 #Әдіс ішінде self.a = 1 деп a атты айнымалыға бастапқы мән ретінде 1 беріледі.
    return self

  def __next__(self): #Келесі итераторларға өту үшін next қолданамыз. 
    x = self.a #Әр рет next() шақырылған кезде, self.a мәні x айнымалысына беріледі.
    self.a += 1 #Кейін self.a += 1 арқылы мәні біреуге өседі.
    return x

myclass = MyNumbers() #Барлығына жауап беретін MyNumbers() классы myclass айнымалысына берілді. 
myiter = iter(myclass) #Iter арқылы сандар келесіне өтіп отырады. 

print(next(myiter)) #Next арқылы әр сан шақыраылады. Бұл жерде 5 рет next қолданып отырмыз, сондықтан 1-5 аралығында сан шығады. Негізі бұл шексіз жалғасады. 
print(next(myiter)) 
print(next(myiter))
print(next(myiter))
print(next(myiter))



#STOP ITERATION ҚОЛДАНУ: 
class MyNum:
    def __init__(self):
        self.a = 1

    def __iter__(self):  # __iter__ әдісін анықтау қажет
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

mycode = MyNum()
for num in mycode:  # Тікелей for арқылы итерация
    print(num)


