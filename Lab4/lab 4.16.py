#Python: date (Third exercise)
#Write a Python program to calculate two date difference in seconds.

from datetime import datetime

time1 = datetime(2025, 2, 1, 14, 0, 0)

time2 = datetime(2025, 2, 1, 14, 2, 30)

difference = time2 - time1 #Екі уақыттың айырмашылықты табу.

seconds = difference.total_seconds() #Айырмашылықты секундпен көрсету. 

print(seconds)