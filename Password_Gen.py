# Import required modules

import random
import string

# Create a function called generated_password! And set both numbers and other_characters "True".

def generated_password(length,
                       numbers=True,
                       other_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

# New variable

    characters = letters

# Check with an if statemen:

    if numbers:
        characters += digits
    if other_characters:
        characters += punctuation

# Create new variables called: 

    password = ""
    critiria = False
    check_number = False
    check_punctuation = False

# Add a while loop and set the random choice to variable named code
# To check length of the password, and return variable to "True".

    while not critiria or len(password) < length:
        code = random.choice(characters)
        password += code

        if code in digits:
            check_number = True
        elif code in punctuation:
            check_punctuation = True

        critiria = True
        if numbers:
            critiria = check_number
        elif other_characters:
            critiria += check_punctuation

# Return password

    return password

# Add user input for the negth of the password and if it implies number and other characters!!

length = int(input("Enter a length to your password: "))
check_number = input("Do you want to include digits in your password? (Yes or No): ").lower() == "yes"
check_punctuation = input("Do you want to include punctuation in your password?(Yes or No): ").lower() == "yes"

password = generated_password(length,
                    check_number,
                    check_punctuation)
print(password)