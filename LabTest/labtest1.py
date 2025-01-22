import random
import string


def is_valid(password) -> bool:
    """ Function that checks if the user's password is valid against set criteria """

    # check if password has a length of less than 10
    if len(password) < 10:
        return False
    
    
     # Check if there is at least one digit
    has_digit = False
    for char in password:
        if char in string.digits:
            has_digit = True
            break  # We found a digit, no need to continue

    # Check if there is at least one uppercase letter
    has_uppercase = False
    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase = True
            break  # We found an uppercase letter, no need to continue

    # Check if there is at least one special character (punctuation)
    has_special = False
    for char in password:
        if char in string.punctuation:
            has_special = True
            break  # We found a special character, no need to continue

    return has_digit and has_uppercase and has_special
        

def strengthen_password(password) -> str:
    """ Function that strengthens the user's password if it is not a valid password """

    # while password length is less than 10, keep adding random characters to the password until the length is 10
    while len(password) < 10:
        random_char = random.choice(string.ascii_letters + string.digits)
        password += random_char
    

    # for each character in password, if an integer isn't in the password, add a random digit
    has_digit = False
    for char in password:
        if char in string.digits:
            has_digit = True
            break
    if not has_digit:
        random_digit = random.choice(string.digits)  # Generate a random digit
        password += random_digit  # Add the digit to the password


    # for each character in password, if the character in upper case is not in the password, add a single upper case letter
    has_uppercase = False
    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase = True
            break
    if not has_uppercase:
        upper_case = random.choice(string.ascii_uppercase)
        password += upper_case


    # for each character in password, if the character doesn't contain any special characters, add one
    has_special = False
    for char in password:
        if char in string.punctuation:
            has_special = True
            break
    if not has_special:
        special_character = random.choice(string.punctuation)
        password += special_character

    
    return password
    
    
# Keep asking the user for input until they choose to exit
while True:
    user_password = input("Enter a password for evaluation (or type 'exit to quit): ")

    if user_password == 'exit':
        break
    else:
        if is_valid(user_password): # if password is valid tell the user it is valid
            print("Password is valid")
        else:
            print("Password is not valid") # if it's not valid tell the user it's not valid and also strengthen their password
            suggested_password = strengthen_password(user_password)
            print("New suggested password:", suggested_password)

