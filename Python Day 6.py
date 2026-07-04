# Code Blocks,Functions,While Loop
# Functions
# Print and len are built in functions
print("Hello World")
num_char=len("Hello")
print(num_char)
# User defined function
def my_function():
    print("Hello")
    print("Bye")
my_function()
# ***Reborg's World***
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

# ***Reborg's World Hurdle***
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# for step in range(0,6):
#     jump()

# Indentation
# def my_function():
#  ....if(sky=="clear"):
#  ........print("Blue")
#  ....elif(sky=="cloudy"):
#  ........print("Black")
#  ....print("Hello")
# print("World")
# In the above code, if,elif and print is indented by 4 spaces.print inside if and elif is indented by 8 spaces
# Space is preferred for indentation

# While Loop
# The loop that will continue going while a particular condition is true.
# Reborg's World Hurdle with while loop
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# n = 6
# while n > 0:
#     jump()
#     n=n-1

# Reborg's World Hurdle Random Goal
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()    
# while not at_goal():
#     jump()

# Infinite loop
# while 5>3:
#     print(5>3)
# This condition is always true and the loop becomes infinite

# for loops are really great when you want to iterate over something and you need to do something with each thing that you are iterating over
# Using while loops,you just simply want to carry out some sort of functionality many,many times until some sort of condition that you set.

# Reborg's World Random Hurdle
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()   
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# Reborg's World Jumping Over Hurdles with Variable Height
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# Final Project Escaping the Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while front_is_clear():
#     move()
# turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
