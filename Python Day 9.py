# Dictionaries and Nesting
# Dictionaries in Python
# Syntax {key:value}
programming_dictionary={
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again.",
}
print(programming_dictionary["Bug"])
# Adding new items to Dictionary
programming_dictionary["While"]="Runs until a certain condition is true"
print(programming_dictionary["While"])
# Create an empty dictionary
empty_dictionary={}
# Wipe or remove an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"]="A moth in your Computer."
print(programming_dictionary["Bug"])
# Loop through a Dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
# Grading Program Exercise
student_scores={
    "Harry":81,
    "Ron":79,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
student_grades={}
for scores in student_scores:
    scored=student_scores[scores]
    if scored>90:
        student_grades[scores]="Outstanding"
    elif scored>80:
        student_grades[scores]="Exceeds Expectations"
    elif scored>70:
        student_grades[scores]="Acceptable"
    else:
        student_grades[scores]="Fail"
print(student_grades)
# Nesting Lists and Dictionaries
# Nesting Lists and Dictionaries means putting one inside the other
# {key1:[list],
#  key2:{dict},
# }
capitals={
    "Pakistan":"Islamabad",
    "Australia":"Canberra",
}
# Nesting a list in a dictionary
travel_log={
    "Pakistan":["Rawalpindi","Karachi","Swat"],
}
# Nesting a dictionary in a dictionary
travel_log={
    "Pakistan":{"cities_visited":["Rawalpindi","Karachi","Swat"],
                "total_visits":12},
    "Australia":{"cities_visited":["Sydney","Melbourne","Adelaide"],
                 "total_visits":10},
}
# Nesting a dictionary in a list
travel_log=[{
    "country":"Pakistan",
    "cities_visited":["Rawalpindi","Karachi","Swat"],
    "total_visits":12
    },
    {
    "country":"Australia",
    "cities_visited":["Sydney","Melbourne","Adelaide"],
    "total_visits":10,
    },
]
# Coding Exercise
travel_log=[{
    "country":"Pakistan",
    "cities_visited":["Rawalpindi","Karachi","Swat"],
    "total_visits":12
    },
    {
    "country":"Australia",
    "cities_visited":["Sydney","Melbourne","Adelaide"],
    "total_visits":10,
    },
]
def add_country(country_visisted,total_visits,cities_visited):
    new_country={}
    new_country["country"]=country_visisted
    new_country["total_visits"]=total_visits
    new_country["cities_visited"]=cities_visited
    travel_log.append(new_country)
add_country("Russia",5,["Moscow","Saint Petersburg"])
print(travel_log)
# The Secret Auction Program
from replit import clear
from blind_auction_art_day9 import logo
print(logo)
bids={}
def highest_bid(bidding_record):
    highest=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest:
            highest=bid_amount
            winner=bidder
    print(f"The winner is {winner} with the highest bid of ${highest}")
should_continue=True
while should_continue:
    name=input("What is your name?\n")
    bid=int(input("Enter your bid: $"))
    bids[name]=bid
    choice=input("Is there any other bid,yes or no ").lower()
    if choice=="yes":
        clear()
    else:
        should_continue=False
        highest_bid(bids)








