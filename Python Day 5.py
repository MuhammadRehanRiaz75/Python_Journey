# Python loops
# for loop
# Things have to happen over and over and over again.For this we use loops.The loop allows us to execute the same line of code multiple times.
# By using for loop we can go through each item in a list and perform action with each individual item.
fruits=["Apple","Banana","Peach"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
print(fruits)
# ☝️ print(fruits) is out of for loop and will be executed once after the for loop
# Average height exercise
students=input("Enter the height of students, separated by a comma ")
std_height1=students.split(",")
# Converting each string item of the list into int 
for n in range(0,len(std_height1)):
    std_height1[n]=int(std_height1[n])
print(std_height1)
# std_height=[int(height) for height in std_height1]
# print(std_height)
avg_height=0
for height in std_height1:
    avg_height+=height
num_students=0
for students in std_height1:
    num_students+=1
avg_height=round(avg_height/num_students)
print(avg_height)
# Highest Score Exercise
scores=input("Input a list of student scores, separated by a space\n").split(" ")
for n in range(0,len(scores)):
    scores[n]=int(scores[n])
print(scores)
highest_score=0
for score in scores:
    if score>highest_score:
        highest_score=score
print(f"The highest score in class is: {highest_score}")
# For loop with range function
for number in range(1,10):
    print(number)
# 10 will be not incuded
for number in range(1,11,3):
    print(number)
total=0
for number in range(1,101):
    total+=number
print(total)
# Adding evens exercise
sum=0
for number in range(1,101):
    if number%2==0:
        sum+=number
print(sum)
add=0
for number in range(2,101,2):
    add+=number
print(add)
# Fizz Buzz Exercise
for number in range(1,101):
    if(number%3==0 and number%5==0):
        print("FizzBuzz")
    elif(number%3==0):
        print("Fizz")
    elif(number%5==0):
        print("Buzz")
    else:
        print(number)
# Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy Level
# password=""
# for char in range(1,nr_letters+1):
#     random_char=random.choice(letters)
#     password+=random_char
# for sym in range(1,nr_symbols+1):
#     random_sym=random.choice(symbols)
#     password+=random_sym
# for num in range(1,nr_numbers+1):
#     random_num=random.choice(numbers)
#     password+=random_num
# print(password)

# Hard Level
password_list=[]
for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password_list+=random_char
for sym in range(1,nr_symbols+1):
    random_sym=random.choice(symbols)
    password_list+=random_sym
for num in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password_list+=random_num
random.shuffle(password_list)
password=""
for chaar in password_list:
    password+=chaar
print(password)
