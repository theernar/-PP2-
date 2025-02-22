#LAB 5: 
#Seventh exercise: Write a python program to convert snake case string to camel case string.

import re 
txt = input("Enter the snake case string: ")
result = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), txt) #Нижный пробелден кейінгі әріпті бас әріпке айналдырып отыру. 
result = result.capitalize() #Ең алғашқы әріпті бас әріпке айналдыру. 
print(result)