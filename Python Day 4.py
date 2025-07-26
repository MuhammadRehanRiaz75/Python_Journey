# Randomisation and Python Lists
# If you want to design a game or want your program to do something different everytime,you need to introduce randomness
import random
import mymodule_Day4
random_integer=random.randint(1,10)
print(random_integer)
random_float=random.random()*5
print(random_float)
print(mymodule_Day4.pi)
love_score=random.randint(1,100)
print(f"Your love score is {love_score}")
# Heads or Tails
import random
random_side=random.randint(0,1)
if random_side==1:
    print("Heads")
else:
    print("Tails")
# Python Lists
# List is a data structure.Its a way of organizing and storing data in python.Lists stores grouped pieces of data
# Lists can have mixed data types like you could store strings together with numbers or a set of booleans
# fruits=[item 1,item 2]
# The first item in the list has zero offset or zero shift.That's why its index is zero.
# The second item has an offset of 1 or shifted by 1.That's why its index is one.
Provinces_of_Pak=["Punjab","Sindh","Balochistan","KPK","Gilgit Baltistan"]
Provinces_of_Pak[3]="Khyber Pakhtunkhwa"
# Append add an item to the end of list
Provinces_of_Pak.append("Kashmir")
Provinces_of_Pak.extend(["Islamabad","Karachi","Multan"])
Provinces_of_Pak.remove("Sindh")
Provinces_of_Pak.insert(1,"Lahore")
print(Provinces_of_Pak[1])
print(Provinces_of_Pak[-1])
print(Provinces_of_Pak)
# Banker Roulette Exercise Who will pay the bill
import random
names_string=input("Give me everybody's names, separated by a comma. ")
names=names_string.split(", ")
# print(names)
num_items=len(names)
random_choice=random.randint(0,num_items-1)
person=names[random_choice]
print(f"{person} is going to buy the meal today!")
# or
import random
names_string=input("Give me everybody's names, separated by a comma. ")
names=names_string.split(", ")
person=random.choice(names)
print(f"{person} is going to buy the meal today!")
# Index errors and working with nested lists
Provinces_of_Pak=["Punjab","Sindh","Balochistan","KPK","Gilgit Baltistan"]
# list index out of range
# print(Provinces_of_Pak[7])
# List within the other list is called nested list
# dirty_dozen=["Apple","Banana","Potatoes","Ginger","Grapes","Mangoes","Turnip","Ladyfinger"]
fruits=["Apple","Banana","Grapes","Mangoes"]
vegetables=["Potatoes","Ginger","Turnip","Ladyfinger"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)
# Tresure map exercise
row1=["😊","😘","😍"]
row2=["😊","😘","😍"]
row3=["😊","😘","😍"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure? ")
horizontal=int(position[0])
vertical=int(position[1])
selected_row=map[vertical-1]
selected_row[horizontal-1]="🏴"
# or
# map[vertical-1][horizontal-1]="🏴"
print(f"{row1}\n{row2}\n{row3}")
# Project Rock Paper Scissors
# Rock beats scissor,Scissor beats paper,Paper beats rock.
import random
rock='''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissor]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if(choice>=3 or choice<0):
    print("You typed an invalid number, you lose!")
else:
    print(f"You choose:\n{game_images[choice]}")

    computer_choose=random.randint(0,2)
    print(f"Computer choose:\n{game_images[computer_choose]}")

    if(choice==0 and computer_choose==2):
        print("You win!")
    elif(computer_choose==0 and choice==2):
        print("You lose!")
    elif(computer_choose>choice):
        print("You lose!")
    elif(choice>computer_choose):
        print("You win!")
    elif(computer_choose==choice):
        print("Draw!")