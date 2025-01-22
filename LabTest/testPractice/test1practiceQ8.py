import random

def userInput():

    while True:
        user_input = input("\nGuess a 3 digit number: ")

        if user_input.isdigit() and len(user_input) == 3:
            return user_input
        else:
            print("Invalid input. Make sure to enter exactly three digits.")

def tips(target_code, user_input):
    
    for i in range(3):
        """Provide feedback on the user's guess compared to the target code."""

        if user_input[i] == target_code[i]:
            print("Bullseye!", end=' ')
        elif user_input[i] in target_code:
            print("Off-target!", end=' ')
        else:
            print("Null", end=' ')

def play_game():
    """Main game loop for 'Conundrum Code'."""

    print("Welcome to 'Conundrum Code'. Try to guess the three digit number.")
    print()
    print("Here are some clues: ")
    print("When I say 'Off-target' that means one of your digits is correct but in the wrong position.")
    print("When I say 'Bullseye' that means one of your digits is correct but in the right position.")
    print("When I say 'Null' that means one of your digits is incorrect.")
    print()

    random_number = random.randint(0, 999)
    target_code = "{:03}".format(random_number)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        user_guess = userInput()
        attempts += 1
        tips(target_code, user_guess)


        if user_guess == target_code:
            print("\nYou got it!")
            break
    else:
        print("\nSorry, you've used all your attempts. The secret code was: ", target_code)



while True:
    play_game()

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again == 'n':
        print("Thank you for playing!")
        break




