import random
import time

def generate_guess(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

def get_user_feedback():
    user_response = input("Is the guess correct? (H/L/C): ").upper()
    while user_response not in ["H", "L", "C"]:
        print("Invalid input. Please enter 'H', 'L', or 'C'.")
        user_response = input("Is the guess correct? (H/L/C): ").upper()
    return user_response

def main():
    print("Welcome to Guess the Number - AI Edition!")
    print("Think of a number between", lower_bound, "and", upper_bound)
    time.sleep(2)  # Pause for 2 seconds
    print("I will try to guess the number you are thinking of.")
    time.sleep(1)
    print("You only need to respond with 'H' if the guess is too high, 'L' if it's too low, and 'C' if I guessed correctly.")
    time.sleep(2)
    print("Let's get started!")

    while True:
        guess = generate_guess(lower_bound, upper_bound)
        print("AI's guess:", guess)
        user_response = get_user_feedback()

        if user_response == "H":
            upper_bound = guess - 1
        elif user_response == "L":
            lower_bound = guess + 1
        else:  # user_response == "C"
            print("AI guessed correctly! The number was:", guess)
            break

if _name_ == "_main_":
    main()
