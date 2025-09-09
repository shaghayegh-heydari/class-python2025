import random

choices = ["rock" , "peper" , "scissors"]

user = ""

while user != "quit":
    user = input("choices rock or peper or scissors")

if user in choices :
    computer = random . choice(choices)
    print (f"cmputer choice is {computer}")
    if user == computer :
        print ("draw")
    elif((user == "rock" and computer == "scissors") or (user == "scissors" and computer == "peper") or
          (user == "peper" and computer == "rock")): 
        print("you win")
else :
    print("you lose!")
print("good luck")