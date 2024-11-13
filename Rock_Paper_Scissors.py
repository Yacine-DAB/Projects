# Import random module: 

import random

#Create an infinite loop:

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or Scissors? ").lower()

# Check randomly (rock, paper or scissors)!

        if player == computer:
            print("computer: ",computer)
            print("player: ",player)
            print("A Tie, Really?")
        elif player == "rock":
            if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose")
            if computer == "scissors":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win")
        elif player == "paper":
            if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win")
            if computer == "scissors":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose")
        elif player == "scissors":
            if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose")
            if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win")

# Create another variable to set the user if he wants to try once again:

    again = input("Do you want to play again?: ").lower()
    if again =="no":
        break

print("Thank you for playing!")