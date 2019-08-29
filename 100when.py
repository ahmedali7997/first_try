# Project 1 - Ahmed Ali
# This project asks for your name and age, then tells you in what year you'll turn 100. It then asks how many times you want to repeat the previous statement, and repeats it by the given amount.


#get the current year
import datetime
now = datetime.datetime.now()

#inputs from user
name = input("What is your name?")
age = input("How old are you?")

#calculates when user will turn 100
hundred = 100-int(age)
hundred_year = now.year+hundred

#returns statement
statement = "Wow {}, you'll turn 100 years old in {} \n".format(name,hundred_year)
print(statement)

#asks for repititon and prints it
repeat = input("How many times do you want to repeat the previous message?")
print(statement*int(repeat))
