# Conditional Statements,Logical Operators,Code Blocks and Scope
# if/else statement
# if condition:
# do this(block of code)
# else:
# do this(block of code)
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
if height>=120:
 print("You can ride the rollercoaster!")
else:
 print("Sorry, you have to grow taller before you ride.")
# Comparison Operators
# Greate than >
# Less than <
# Greater than or equal to >=
# Less than or equal to <=
# Equal to ==
# Not equal to !=
# Odd or even exercise
number=int(input("Which number do you want to check? "))
if number%2==0:
 print("This is an even number.")
else:
 print("This is an odd number.")
# Nested if statements and elif statements
# Nested if statements
 print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
if height>=120:
 print("You can ride the rollercoaster!")
 age=int(input("Please enter your age: "))
 if age<=18:
  print("You will $7")
 else:
  print("You will pay $12")
else:
 print("Sorry, you have to grow taller before you ride.")
# Nested elif statements
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
if height>=120:
 print("You can ride the rollercoaster!")
 age=int(input("Please enter your age: "))
 if age<12:
  print("You will $5.")
 elif age<=18:
  print("You will pay $7.")
 else:
  print("You will pay $12.")
else:
 print("Sorry, you have to grow taller before you ride.")
# Coding exercise BMI Calculator
print("Wlecome to BMI Calculator")
height=float(input("Please enter your height in meters: "))
weight=float(input("Please enter your weight in kilograms: "))
bmi=round(weight/(height**2))
# final_bmi="{:.2f}".format(bmi)
if bmi<18.5:
 print(f"Your BMI is {bmi}, you are underweight")
elif bmi<25:
 print(f"Your BMI is {bmi}, you have normal weight")
elif bmi<30:
 print(f"Your BMI is {bmi}, you are overweight")
elif bmi<35:
 print(f"Your BMI is {bmi}, you are obese")
else:
 print(f"Your BMI is {bmi}, you are clinically obese")
# Coding exercise Leap Year
year=int(input("Enter the year you want to check: "))
if year%4==0:
 if year%100==0:
  if year%400==0:
   print("Leap Year!")
  else:
   print("Not Leap Year")
 else:
   print("Leap Year!")
else:
 print("Not Leap Year")
# Multiple If Statements in Succession
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0
if height>=120:
 print("You can ride the rollercoaster!")
 age=int(input("Please enter your age: "))
 if age<12:
  bill=5
  print("Child tickets are $5.")
 elif age<=18:
  bill=7
  print("Youth tickets are $7.")
 else:
  bill=12
  print("Adult tickets are $12.")

 want_photos=input("You want a photo taken.Y or N ")
 if want_photos=="Y":
   bill+=3

 print(f"Your bill is ${bill}")

else:
 print("Sorry, you have to grow taller before you ride.")

 # Coding Exercise for Piza Order
print("Welcome to the Python Pizza Deliveries")
size=input("What size pizza do you want: S,M or L ")
add_pepperoni=input("Do you want pepperoni: Y or N ")
extra_cheese=input("Do you want extra cheese: Y or N ")
bill=0
if size=="S":
 bill+=15
elif size=="M":
 bill+=20
else:
 bill+=25

if add_pepperoni=="Y":
 if size=="S":
  bill+=2
 else:
  bill+=3

if extra_cheese=="Y":
 bill+=1

print(f"Your final bill is ${bill}")

# Logical Operators
# And,Or,Not
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0
if height>=120:
 print("You can ride the rollercoaster!")
 age=int(input("Please enter your age: "))
 if age<12:
  bill=5
  print("Child tickets are $5.")
 elif age<=18:
  bill=7
  print("Youth tickets are $7.")
 elif age>=45 & age<=55:
  bill=0
  print("Have a free ride on us")
 else:
  bill=12
  print("Adult tickets are $12.")

 want_photos=input("You want a photo taken.Y or N ")
 if want_photos=="Y":
   bill+=3

 print(f"Your bill is ${bill}")

else:
 print("Sorry, you have to grow taller before you ride.")

# Love Calculator
print("Welcome To Love Calculator!")
name1=input("What is you name?\n")
name2=input("What is their name?\n")
combined_string=name1+name2
print(combined_string)
lower_case_string=combined_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true=t+r+u+e
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
 print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
 print(f"Your love score is {love_score}, you are alright together")
else:
 print(f"Your love score is {love_score}")

# Project Tresure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYou mission is to find the treasure.")
dir=input('You\'re at a cross road.Where do you want to go? Type "left" or "right"\n')
dir2=dir.lower()
if dir2=="left":
 wait_or_swim=input('You come to a lake.There is an island in the middle of the lake.Type "wait" to wait for a boat or "swim" to swim across.\n')
 wait_or_swim2=wait_or_swim.lower()
 if wait_or_swim=="wait":
  door=input("You arrive at the island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which colour do you choose?\n")
  door2=door.lower()
  if door=="red":
   print("Its a room full of fire.Game Over!")
  elif door=="yellow":
   print("You found the treasure.You Win!")
  elif door=="blue":
   print("You enter a room of beasts.Game Over!")
  else:
   print("You entered the room that does not exist.Game Over!")
 else:
  print("You got attacked by an angry trout.Game Over!")
else:
 print("You fell into a hole.Game Over!")


 


