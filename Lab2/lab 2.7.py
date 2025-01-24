# Python: Dictionaries!
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

mydict = {"Name": "Yernar", "Age": 18, "City": "Kyzylorda"}
print(mydict) #Result: {'Name': 'Yernar', 'Age': 18, 'City': 'Kyzylorda'}

mydict = {"Name": "Yernar", "Age": 18, "City": "Kyzylorda"}
print(mydict["Name"]) #Result is: Yernar

#Duplicate not allowed: 
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    "City": "Almaty"
    }
print(mydict) #Programm will delete random if have duplicate informations. In this code "City" is written two times.

#Length of dictionaries: 
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    }
print(len(mydict)) 


#TYPE OF DICTIONARIES: 
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    }
print(type(mydict)) #Result: <class 'dict'>

#To make a dictionary:
mydict = dict(name = "Yernar", age = 18, country = "Kazakhstan")
print(mydict)

#REMOVING ITEMS FROM THE DICTIONARY: 
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    }
mydict.pop("Age")
print(mydict)

#REMOVING THE LAST ELEMENT:
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    }
mydict.popitem()
print(mydict) #This opreation will delete the last element of the dictionary

#REMOVING ELEMENTS FROM THE DICTIONARY WITH CLEAR:
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    }
mydict.clear()
print(mydict)

#LOOP IN DICTIONARIES: 
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
    }

for x in mydict: 
    print(x)
    
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
}

for x in mydict:
    print(mydict[x]) #Элементтерді шығару үшін: Yernar, Kyzylorda, 18
    
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
}

for x in mydict.values():
    print(x) #'Yernar', 'Kyzylorda', 18
    
for x in mydict.keys():
    print(x) #'Name', 'City', 'Age'

for x, y in mydict.items():
    print(x,y) #For print both of them
    
#COPY DICTIONARIES: 
mydict = {
    "Name": "Yernar",
    "City": "Kyzylorda",
    "Age": 18,
}
x = mydict.copy()
print(x)