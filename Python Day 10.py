# Functions with Outputs
def my_function():
    result=2*3
    return result
output=my_function()
print(output)
# Format Name
F_name=input("Enter your first name: ")
L_name=input("Enter your last name: ")
def format_name(f_name,l_name):
    # Docstrings
    """Take a first and last name and format it to 
    return the title case version of the name"""
    first_name=f_name.title()
    last_name=l_name.title()
    # name=first_name+" "+last_name
    # return name
    return f"{first_name} {last_name}"
name=format_name(f_name=F_name,l_name=L_name)
print(name)
# Multiple return values
F_name=input("Enter your first name: ")
L_name=input("Enter your last name: ")
def format_name(f_name,l_name):
    # Docstrings
    """Take a first and last name and format it to 
    return the title case version of the name"""
    if f_name=="" and l_name=="":
        return f"You did not provide valid inputs"
    first_name=f_name.title()
    last_name=l_name.title()
    # name=first_name+" "+last_name
    # return name
    return f"{first_name} {last_name}"
name=format_name(f_name=F_name,l_name=L_name)
print(name)
# Days in Month
yearr=int(input("Enter the year: "))
monthh=int(input("Enter the month: "))
def leap_year(year):
    # Docstrings
    """Takes a year and return whether its leap or not"""
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year,month):
    # Docstrings
    """Takes a year and a month and return the 
    number of days in month of that year"""
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    return days[month-1]
days=days_in_month(yearr,monthh)
print(days)
# Calculator
# Recursion is calling a function within its own definition
from Calculator_art_day10 import logo
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
operations={
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
}
def calculator():
    print(logo)
    num1=float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue=True
    while should_continue:
        opr=input("Pick an operation: ")
        num2=float(input("Enter the next number: "))
        calculate_function=operations[opr]
        answer=calculate_function(num1,num2)
        print(f"{num1}{opr}{num2}={answer}")
        choice=input(f"Type y to continue calculating with {answer},or type n to start new calculation: ")
        if choice=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()

