print("WELCOME TO ENDYS QUIZ GAME 2024")
user='Before we begin this game we would like to know more about you your name\nyour age and where you come from\n'
print(user)
user=input("ARE YOU READY?: " )
if user.upper() == "YES":
   print("OKAY LETS GO!")
   score = 0
else:
   print("OKAY SEE YOU LATER BYEE")
   quit()
user=input("CAN WE KNOW YOUR NAME:? ")
print("HI NICE MEETING YOU " + str(user))
from datetime import date
today_date = date.today().strftime("%Y")
birth_date=int(input("CAN WE KNOW YOUR YEAR OF BIRTH?: "))
current_age = ("YOUR CURRENT AGE IS", int(today_date)-birth_date)
print(current_age)
print("welcoem to the game user,the time and Date now is: ")
import datetime as today
now= today.datetime.now()
print(now)
print("MAIN GAME")
print("IT QUESTIONS AND ANSWERS")
user = input("Q1.WHAT IS THE USE OF A MOUSE? ")
if user.lower() == "clicking":
   print("correct")
   score +=1
else:
   print("incorrect")
user = input("Q1.WHAT IS THE USE OF A CPU? ")
if user.lower() == "helps makes the computer run":
   print("orrect")
   score +=1 
else:
   print("incorrect")
user = input("Q1.WHAT IS THE USE OF A KEYBOARD? ")
if user.lower() == "for typing":
   print("correct")
   score +=1 
else:
   print("incorrect")
user = input("Q1.WHAT IS THE USE OF A PENDRIVE? ")
if user.lower() == "a storage device":
   print("correct")
   score +=1 
else:
   print("incorrect")

print("YOU GOT " + str(score) + " QUESTIONS RIGHT")
print("YOU GOT " + str(score * 100) + "% QUESTIONS RIGHT")
                                                                                                                                     