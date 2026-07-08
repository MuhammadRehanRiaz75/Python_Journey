# Function Parameters and Caesar Cipher
# Functions with inputs,Arguments and Parameters
# Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet()
# Function that allows for input
def greet_with_me(name):
    print(f"Hello {name}")
    print(f"What do you do {name}?")
    print(f"Isn't the weather nice today?")
greet_with_me("Rehan")
# ☝️ name is parameter and Rehan is argument
# Parameter is the name of the data thats been passed in
# Argument is the actual value of the data

# Positional VS Keyword Arguments
# Functions with more than one input
def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
greet_with("Rehan","Pakistan")
# Positional Arguments
# When we call the function,we haven't specified anywhere which particular parameter we want to associate
# these pieces of data with. So it's just gone and looked at the position.
def number(a,b,c):
    print(f"a={a}\nb={b}\nc={c}")
number(1,2,3)
number(3,2,1)
# ☝️ not same values
# Keyword Arguments
def numbers(a,b,c):
    print(f"a={a}\nb={b}\nc={c}")
numbers(a=1,b=2,c=3)
numbers(c=3,b=2,a=1)
# ☝️ same values
def greet_to(name,location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?") 
greet_to(location="Pakistan",name="Rehan")  
# Paint Area Calculator
import math
test_h=int(input("Enter the height of the wall\n"))
test_w=int(input("Enter the width of the wall\n"))
coverage=5
def calculate_paint(height,width,cover):
    area=height*width
    num_of_cans=math.ceil(area/cover)
    # num_of_cans=round(area/cover)
    print(f"You will need {num_of_cans} cans of paint")
calculate_paint(height=test_h,width=test_w,cover=coverage)
# Prime Number Checker
# n=int(input("Check this number: "))
# def prime_number(number):
#     is_prime=True
#     for i in range(2,number):
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
# prime_number(number=n)
# or
n=int(input("Check this number: "))
def prime_number(number):
    if number==1:
        print("Neither prime nor composite")
    else:
        count=0
        for i in range(1,number+1):
            if number%i==0:
                count+=1
        if(count==2):
            print("Its a prime number")
        else:
            print("Its not a prime number")
prime_number(number=n)
# Cipher Caesar Project
from caesar_cipher_artday8 import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(message,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in message:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {cipher_direction}d text is {end_text}")
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(message=text,shift_amount=shift,cipher_direction=direction)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if choice=="no":
        should_continue=False
        print("Goodbye")
# def encrypt(message,shift_amount):
#     cipher_text=""
#     for letter in message:
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")
# def decrypt(cipher_text,shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         new_letter=alphabet[new_position]
#         plain_text+=new_letter
#     print(f"The decoded text is {plain_text}")
# if direction=="encode":
#     encrypt(message=text,shift_amount=shift)
# elif direction=="decode":
#     decrypt(cipher_text=text,shift_amount=shift)
# else:
#     print("Invalid Direction")
