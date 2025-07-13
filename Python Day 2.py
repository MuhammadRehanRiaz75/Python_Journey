# Data types,Numbers,Operations,Type Conversion,f-Strings
# Data types
# String: 
# A combination of characters.We create strings with double quotes or single quotes.
# Subscripting:
# Pulling out a particular character from string.
print("Hello"[4])
# Also a string.
"123"
print("123"+"345")
# Integer:
# Whole numbers,numbers without any decimal places.
a=123
b=345
print("Sum:",a+b)
a=123_456_789
b=1
print("Sum:",a+b)
# When we write large numbers 123456789,we can replace commas with underscores.
# 123,456,789=123_456_789
# Float:
# Numbers with decimal places e.g: 3.14159 and 3141.59
a=3.14159
b=2.14159
print("Sum:",a+b)
# Boolean:
# True or False
# Type error,Type checking and Type conversion
# Type error:
# len(4837)
# TypeError: object of type 'int' has no len()
# len function doesn't like working with integers.
num=len(input("What is your name? "))
# print("Your name has " + num + " characters")
# We cannot concatenate strings with integers.
# Type checking:
print(type(num))
# Type conversion or Type Casting:
# Changing one data type to another.
new_num=str(num)
print("Your name has " + new_num +" characters")
# Before converting to string.
a=123
print(type(a))
# After converting to string
a=str(123)
print(type(a))
# or
# a=123
# b=str(a)
# print(type(b))
# Converting integer to float
a=float(123)
print(type(a))
# Converting string to float
print(70+float("100.5"))
# Converting integer to string
print(str(70)+str(100))
# Coding exercise to add first digit to the second digit
num=input("Enter a two digit number: ")
# The data type of num is string.
print(type(num))
digit1=int(num[0])
digit2=int(num[1])
print("Sum:",digit1+digit2)
# Mathematical Operations
# 3+5
# 7-4
# 3*2
# 6/3
print(type(6/3))
# Division always give a float number.
# Exponential 2**3
print(2**3)
# PEMDAS
# Parentheses ()
# Exponents **
# Multiplication * Division / On the left side will be prioritized.
# Addition + Subtraction - On the left side will be prioritized.
print(3*3+3/3-3)
print(3*(3+3)/3-3)
# 1.(3+3) 2.6*3 3.18/3 4.6-3 5.3
# Coding exercise to calculate BMI
height=float(input("Enter your height in meters: "))
weight=float(input("ENter your weight in kg: "))
bmi=int(weight/(height**2))
print("Your BMI is: ",bmi)
# Number manipulation and F strings in python
# Rounding off numbers
print(round(8/3))
# Rounding off to 2 decimal places
print(round(2.66666,2))
# Floor division
print(8//3)
print(type(8//3))
# Manipulate a value based on its previous value
result=4/2
result/=2
print(result)
score=0
score+=1
print(score)
# F strings
# In python,we can use f-strings to combine different data types in a single string.
score=1
height=1.8
isWinning=True
print(f"Your score is {score}\nYour height is {height}\nYou are winning is {isWinning}")
# Coding exercise to calculate remaining days,weeks and monhs of your life
age=int(input("Enter your age: "))
years_left=90-age
months_left=years_left*12
rem_days=years_left*365
rem_weeks=years_left*52
message=f"You have {rem_days} days, {rem_weeks} weeks and {months_left} months"
print(message)
# Tip calculator
print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill? $"))
tip=float(input("What percentage tip would yiou like to give? 10,12 or 15? "))
num_people=float(input("How many people to split the bill? "))
tip_amount=bill*(tip/100)
total_bill=bill+tip_amount
bill_per_person=total_bill/num_people
final_amount="{:.2f}".format(bill_per_person)
message=f"Each person shoul pay: ${final_amount}"
print(message)



