# Namespaces
# Local Scope VS Global Scope
# Scope: An apple tree in your garden can only be accessed by your family but apple tree on the side walk can be accessed by anyone.
enemies=1
def increase_enemies():
    enemies=2
    print(f"Enemies inside the function: {enemies}")
increase_enemies()
print(f"Enemies outside the function: {enemies}")
# Local Scope: When you create a new variable or function inside another function,its only accessible when you are inside that function
def drink_potion():
    potion_strength=2
    print(potion_strength)
drink_potion()
# Error: print(potion_strength)
# Global Scope: Global variables are available inside the function as well as outside the function anywhere in the file.
player_health=10
def drink_potion():
    potion_strength=2
    print(player_health)
drink_potion()
print(player_health)
# Anything you define or to which you have given a name has a namespace.This namespace is valid in a certain scope.
player_health=10
def game():
    def drink_water():
        potion_strength=2
        print(player_health)
    drink_water()
game()
print(player_health)
# Python has no block scope.
# If you create a variable within a function, then it's only available within that function.
game_level=3
def create_enemy():
    enemie=["Skeleton","Zombie","Alien"]
    if game_level<5:
        new_enemy=enemie[0]
    print(new_enemy)
create_enemy()
# print(new_enemy) Error
# But if you create a variable within an if block or a while loop or a for loop or anything that has the indentation and the colon,then that does not count as creating a separate local scope.
game_level=3
enemie=["Skeleton","Zombie","Alien"]
if game_level<5:
    new_enemy=enemie[0]
print(new_enemy)
# Modifying Global Scope
enemii=1
def increase_enemiis():
    global enemii
    enemii+=1
    print(f"Enemies inside the function: {enemii}")
increase_enemiis()
print(f"Enemies outside the function: {enemii}")
# Without modifying global scope
enem=1
def increase_enemees():
    return enem+1
enemiis=increase_enemees()
print(f"Enemies inside the function: {enemiis}")
print(f"Enemies outside the function: {enem}")
# Python Constants and Global Scope
# Global scope can be incredibly useful especially when you're defining constants.
# Global constants are variables which you define and you're never planning on changing it ever again.
# The naming convention in Python is to turn it into all uppercase to change from variables.
PI=3.14159
TWITTER_HANDLE="@rehanriaz"
# Number Guessing Game
# import random
# from guessnumberart_day12 import logo
# print(logo)
# print("Welcome To The Number Guessing Game!\nI am thinking of a number between 1 and 100.")
# difficulty=input("Choose difficulty level.Type 'easy' or 'hard': ")
# computer_num=random.randint(1,100)
# print(computer_num)
# def answer(level):
#     if level=="easy":
#         guess_number=10
#     if level=="hard":
#         guess_number=5
#     return guess_number
# attempts=answer(difficulty)
# print(f"You have {attempts} attempts to guess the number.")
# while attempts>0:
#     num=int(input("Enter your number: "))
#     if num==computer_num:
#         print(f"You won.The answer is {num}")
#         break
#     elif num>computer_num:
#         print(f"Too High")
#     else:
#         print("Too Low")
#     attempts-=1
#     if attempts>0:
#         print(f"You have {attempts} attempts remaining to guess the number.")
#     else:
#         print(f"You have used all your attempts.You Lose.The correct number was {computer_num}")
import random
from guessnumberart_day12 import logo
Easy_turns=10
Hard_turns=5
def set_difficulty():
    level=input("Choose difficulty level.Type 'easy' or 'hard': ")
    if level=="easy":
        return Easy_turns
    if level=="hard":
        return Hard_turns
def check_answer(gues,answer,turns):
    """Checks answer against guess.Returns the number of attempts remaining."""
    if gues==answer:
        print(f"You got it!.You won.The answer is {answer}")
    elif gues>answer:
        print("Too high")
        return turns-1
    else:
        print("Too low")
        return turns-1
def game():
    print(logo)
    print("Welcome To The Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    computer_num=random.randint(1,100)
    print(computer_num)
    attempts=set_difficulty()
    guess=0
    while guess!=computer_num:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess=int(input("Guess a number: "))
        attempts=check_answer(guess,computer_num,attempts)
        if attempts==0:
            print(f"You have run out of attempts.You lose.The answer was {computer_num}")
            return
        elif guess!=computer_num:
            print("Guess again")
game()







