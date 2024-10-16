# make an infinite loop

while True:
    question = input("Select an operator (+,-,*,/): ")
    try:
        if question == "+":
                user1 = int(input("Enter a number to add: "))
                user2 = int(input("Enter the second number to add: "))
                print(user1 + user2)
        elif question == "-":
                user1 = int(input("Enter a number to substract: "))
                user2 = int(input("Enter the second number to substract: "))
                print(user1 - user2)
        elif question == "*":
                user1 = int(input("Enter a number to multiplicate: "))
                user2 = int(input("Enter the second number to multiplicate: "))
                print(user1*user2)
        elif question == "/":
                user1 = int(input("Enter a number to divide: "))
                user2 = int(input("Enter the second number to divide: "))
                print(user1/user2)

# Add an else statement to complete the user input! and just pass it.
        
        else:
            print("Unknown Operator, you can only choose on of the following (+,-,*,/)!")
            pass


    except(ZeroDivisionError, ValueError) as e:
        print(e)
        print("you can't divide by zero or by a string! ")
    except Exception as e:
        print(e)
        print("There is an error!")

# finally always executes!!!

    finally:
        print("Thank you for participating in this calculation task!")

# Create a new variable to set the user if he wants to play again!!

# At the end of the input, add a lower method to set the upper case letter in terminal if that is needed!

    try_again = input("Do you want to try again? (yes or no) : ").lower()
    if try_again != "yes":
        break
          
print("#--------------")
print("Next Time, By")
        