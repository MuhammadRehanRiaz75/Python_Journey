# Printing to the console
print("Hello World!")
# String manipulation and concatenation
# Use of \n to create a new line
print("Hello World\nHello World")
print("Hello"+" "+"Rehan")
# Debugging
# Syntax Error
print("Day 1 - String Manipulation")
# Use '' because with "" it will think there are two strings and will concatenate them
print('String Concatenation is done with the "+" sign.')
# Indentation Error
print('e.g. print("Hello " + "world")')
# Close the parenthesis
print("New lines can be created with a backslash and n.")
# Input function
input("What is your name? ")
print(input("Your favourite subject: "))
# Input function with concatenation or input function within the print function
# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello"+" "+input("What is your name? ")+"!")
# Calculate the length of the string
print(len(input("Tell me your city ")))
# Python variables
pname=input("Tell me name of your pet: ")
print(pname)
# Variable means it can be changed
name="Rehan"
print(name)
name="Farhan"
print(name)
# Simplifying the code with variables
hobby=input("What is you hobby: ")
length=len(hobby)
print(length)
# Switching values
a=input("a:")
b=input("b:")
c=a
a=b
b=c
print("a:"+a)
print("b:"+b)
# Rules for naming variables
# 1. Make your code readable
# 2. No space in between e.g: user name but user_name is correct
# 3. Numbers cannot be at the beginning of the variable name e.g: 1length is wrong
# 4. Do not use function names as variable name it might not give error but bad practice
# 5. Call the variable name correctly
# Final Project of Day 1
print("Welcome to the Band Name Generator.")
city=input("What's name of the city you grew up in?\n")
pet_name=input("What's your pet's name?\n")
print("Your band name could be "+ city+" "+pet_name)




