# print()
# print("Hellow World")
# print()
# print("This is a simple Python program")
# print()
# print("It demonstrates basic syntax and output")
# print()
# print("You can run this program to see the output")
# print()
# print("Blank line \nin the middle of the string")
# print("Hellow")
# print("World")
# # or same thing another way

# print("Hellow \nworld")

# print("adding numbers")
# x = 42 + 206
# print("Performing divison")
# y = x / 0
# print("Math complete")

# name = input("What is your name? ")
# print("Hello")
# print(name)
#first_name = "Ras"
#last_name = "al Ghul"
# print ("Hello " + first_name + " " + last_name)
# modify a string
# sentence = "The dog is named Sammy"
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.count("a"))
# print(sentence.replace("dog", "cat"))
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# print("Hello " + first_name.capitalize() + " " + last_name.capitalize())

# custom string formatting

# output = "Hello, " + first_name + " " + last_name
# print(output)
# output = "Hello, {} {}".format(first_name, last_name)
# print(output)
# output = "Hello, {0} {1}".format(first_name, last_name)
# print(output)
# output = f"Hello, {first_name} {last_name}"
# print(output)   

#pi = 3.14159
# print(pi)
# first_num = "6"
# second_num = "2"
# print(first_num + second_num)
# print(first_num - second_num)
# print(first_num * second_num)
# print(first_num / second_num)
# print(first_num ** second_num)
#type conversion
# days_in_feb = 28
# print(str(days_in_feb) + " days in February")
# first_num = input("Enter the first number: ")
# second_num = input("Enter the second number: ")
# print(first_num + second_num)

# # data type conversion
# print(int(first_num) + int(second_num))
# print(float(first_num) + float(second_num))

#date// datetime library
## to get current date and time, we need to use the datetime library
# from datetime import datetime
# current_date = datetime.now()
# ## the now() function returns the current date and time as a datetime object
# print( "Today is : " + str(current_date))

# timedelta
# from datetime import datetime, timedelta
# today = datetime.now()
# print("Today is: " + str(today))    

# one_day = timedelta(days=1)
# yesterday = today - one_day
# print("Yeterday was: " + str(yesterday))

# from datetime import datetime
# current_date = datetime.now()
# print()
# print("Day: " + str(current_date.day))
# print()
# print("Month: " + str(current_date.month))
# print()
# print("Year: " + str(current_date.year))    
# print()
# from datetime import datetime, timedelta
# birthday = input("Enter your birthday (dd/MM/yyyy)? ")
# birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
# print()
# print("Your birthday : " + str(birthday_date.date()))
# print()
# one_day = timedelta(days=1)
# birthday_eve = birthday_date - one_day
# print("day before birthday : " + str(birthday_eve.date()))
# print()
# today = datetime.now()
# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print( "last_week : " + str(last_week.date()))
# print()

#formating to day, minute etc

# today = datetime.now()
# print()
# print( "Day : " + str(today.day))
# print()
# print( "Month : " + str(today.month))
# print()
# print( "Year : " + str(today.year))
# print()
# print( "Hour : " + str(today.hour))
# print()
# print( "Minute : " + str(today.minute))
# print()
# print( "Second : " + str(today.second))
# print()
##error type
#syntax error
#runtime error
#logical error
# try:
#     print(x / y)
# except ZeroDivisionError:
#     print("Sorry, something went wrong")
# except:
#     print("Something really went wrong")
# finally:
#     print("This always runs on success or failure")
# x = 42
# y = 0
# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     print("Not allowed to divide by zero")
# except:
#     print("Something else went wrong")
# finally:
#     print("This is our cleanup code ")
# print()
# price = float(input("Enter the price of the item: "))
# if price >= 1.00:
#     tax = .07
#     print(tax)
# else:
#     tax = 0
#     print(tax)  
# country = input( "where are you from?" )
# if country.lower() == "canada":
#     print("Oh look Canadian!")
# else:
#     print("You are not from Canada")    
# price = input ("How much you paid ? ")

# price = float(price)
# if price >= 1.00:
#     tax = .07
#     print(tax)
# else:
#     tax = 0
#     print("Tax rate is: " + str(tax))

# province = input("Enter the province: ")
# if province == "Alberta":
#     tax = 0.00
# elif province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.07
# print("Tax rate is: " + str(tax))


###or statement
# province = input("Enter the province: ")
# if province == "Alberta" \
#    or province == "Nunavut" :
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.07
# print("Tax rate is: " + str(tax))


#####in operator
# province = input("Enter the province: ")
# if province in ("Alberta", "Nunavut", "Yukon"):
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print("Tax rate is: " + str(tax))

##double nesting if statement and using lower case to make it less error prone
# country = input("Where are you from? ")
# if country.lower() == "canada":
#     province = input("Enter the province: ")
#     if province.lower() in ("alberta", "nunavut", "yukon"):
#         tax = 0.05
#     elif province == "Ontario":
#         tax = 0.13
#     else:
#         tax = 0.15
#     print("Tax rate is: " + str(tax))
#     print ()

#####and statement
# gpa = float(input("Enter your GPA: "))
# lowest_grade = float(input("Enter your lowest grade: "))
# if gpa >= 0.85 and lowest_grade >= 0.70:
#     print("Well done")


###### boolean variables flags

# gpa = float(input("Enter your GPA: "))
# lowest_grade = float(input("Enter your lowest grade: "))
# if gpa >= 0.85 and lowest_grade >= 0.70:
#     honor_roll = True
# else:
#     honor_roll = False
# if honor_roll:
#     print("Well done")

#####lists & array

###lists
# names = [ "Chris", "Susan"]
# scores = []
# scores.append(98)
# scores.append(99)
# print(names)
# print(scores)
# print(scores[1])

#### array
# from array import array
# scores = array("d")
# scores.append(97)
# scores.append(98)
# print(scores)
# print(scores[1])
# names = [ "Chris", "Susan"]
# print(len(names))
# names.insert(0, "Bill")
# print(names)
# names.sort()
# print(names)

#####ranges
# names = [ "Chris", "Susan", "Bill", "Adam", "Eve"]
# presenters = names[1:3]
# print(names)
# print(presenters)

####dictionary
# person = {"first": "Chris"}
# person["last"] = "Har"
# print(person)
# print(person["first"])

# chris = {}
# chris["first"] = "Chris"
# chris["last"] = "Har"

# susan = {}
# susan["first"] = "Susan"
# susan["last"] = "ibach"

# people = []
# people.append(chris)
# people.append(susan)
# people.append({"first": "Bill", "last": "Smith"})
# print(people)

#####loops
# for name in ["Chris", "Susan", "Bill", "Adam", "Eve"]:
#     print(name)

# for index in range(0,2):
#     print(index)


# names = [ "Chris", "Susan", "Bill", "Adam", "Eve"]
# index = 0
# while index < len(names):
#     print(names[index])
#     index = index + 1

# people = ["Chris",  "Susan"]
# print()
# for name in people:
#     print(name)

# index = 0
# while index < len(people):
#     print()
#     print(people[index])
#     index = index + 1

# print()


### primt timestamps
# import datetime
# first_name = "Susan"
# print()
# print("task completed")
# print(datetime.datetime.now())
# for x in range(0,10):
#      print(x)
# print("task completed")
# print(datetime.datetime.now())
# print()

# import datetime
# print()
# def print_time():
#     print("task completed")
#     print(datetime.datetime.now())
# first_name = "Susan"
# print_time()
# for x in range(0,10):
#      print(x)
# print_time()
# print() 
# from datetime import datetime
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
# first_name = "Susan"
# print_time("first name assigned")
# for x in range(0,10):
#      print(x)
# print_time("loop completed")
# print()

# first_name = input("What is your first name? ")
# first_name = first_name.capitalize()
# first_name_initial = first_name[0:1]
# last_name = input("What is your last name? ")
# last_name = last_name.capitalize()
# last_name_initial = last_name[0:1]
# print("Your initials are " + first_name_initial + " " + last_name_initial)

# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial
# first_name = input("What is your first name? ")
# first_name_initial = get_initial(first_name)
# last_name = input("What is your last name? ")
# last_name_initial = get_initial(last_name)
# print("Your initials are " + first_name_initial + " " + last_name_initial)

# ####another way of doing

# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# print("Your initials are " + get_initial(first_name)+ " " + get_initial(last_name))

###force uppercase

# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial
# first_name = input("What is your first name: ")
# first_name_initial = get_initial(first_name,False)
# print("Your initial is " + first_name_initial)


# def get_initial(name, force_uppercase = True):
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial
# first_name = input("What is your first name: ")
# first_name_initial = get_initial(force_uppercase=True,name=first_name)
# print("Your initial is " + first_name_initial)

# def error_logger(error_code, error_severity, log_to_db,error_message, source_module):
#     print( "oh no error: " + error_message)

#     #imagine code here to log the error to a database or file

# first_number = 10
# second_number = 5
# if first_number > second_number:
#     error_logger(error_code=45, error_severity=1, log_to_db=True, error_message="second number greater than first", source_module="my_math_method")
###import module as namespace
# import helpers
# helpers.display("Not a warning")

###import all into current namespace
# from helpers import *
# display("Not a warning")


####import specific items ino current namespace
# from helpers import display
# display("Not a warning")

#import helpers
# helpers.display("Sample message", True)

####or another way
# from helpers import display
# display("Sample message") 

####hiding key in apps
from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv("PASSWORD")
print()
print(password)
print()