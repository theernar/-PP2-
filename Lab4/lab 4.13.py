#Python: date (First exercise)
#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta
import datetime

x = datetime.datetime.now()   #Дәл қазіргі уақытты анықтау үшін. 
print("Дәл қазіргі уақыТ: ", x)
y = timedelta(days=5)
result = x-y
print("5 күнді алып тастағаннан кейінгі уақыт: ", result)