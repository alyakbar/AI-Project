import random
import time

class DifficultyLevel:
    def __init__(self, name, lower_bound, upper_bound):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

# Define difficulty levels with their respective ranges
EASY = DifficultyLevel("Easy", 1, 50)
MEDIUM = DifficultyLevel("Medium", 1, 100)
HARD = DifficultyLevel("Hard", 1, 200)

def generate_guess(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

def get_user_feedback():
    user_response = input("Is the guess correct? (H/L/C): ").upper()
    while user_response not in ["H", "L", "C"]:
        print("Invalid input. Please enter 'H', 'L', or 'C'.")
        user_response = input("Is the guess correct? (H/L/C): ").upper()
    return user_response

def get_range_from_user():
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("Invalid range. The lower bound must be less than the upper bound.")
            else:
                return lower_bound, upper_bound
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def get_max_guesses_from_user():
    while True:
        try:
            max_guesses = int(input("Enter the maximum number of guesses allowed: "))
            if max_guesses <= 0:
                print("Invalid number of guesses. Please enter a positive integer.")
            else:
                return max_guesses
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def select_difficulty_level():
    print("\nSelect the difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        try:
            user_choice = int(input("Enter the corresponding number (1/2/3): "))
            if user_choice == 1:
                return EASY
            elif user_choice == 2:
                return MEDIUM
            elif user_choice == 3:
                return HARD
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to Guess the Number - AI Edition!")
    difficulty = select_difficulty_level()

    lower_bound = difficulty.lower_bound
    upper_bound = difficulty.upper_bound

    print("Think of a number between", lower_bound, "and", upper_bound)
    time.sleep(2)
    print("I will try to guess the number you are thinking of.")
    time.sleep(1)
    print("You only need to respond with 'H' if the guess is too high, 'L' if it's too low, and 'C' if I guessed correctly.")
    time.sleep(2)
    print("Let's get started!")

    max_guesses = get_max_guesses_from_user()
    num_guesses = 0

    while num_guesses < max_guesses:
        guess = generate_guess(lower_bound, upper_bound)
        #new guess count variable
        guess_count += 1
        print("AI's guess:", guess)
        user_response = get_user_feedback()
        num_guesses += 1

        if user_response == "H":
            upper_bound = guess - 1
        elif user_response == "L":
            lower_bound = guess + 1
        else:  # user_response == "C"
            print("AI guessed correctly! The number was:", guess)
            #he number of guesses the AI has made.
            print("AI took", guess_count, "guesses to get the correct answer.")
            break
    else:
        print("Sorry, the AI could not guess the correct number within the given number of guesses.")

if __name__ == "__main__":
    main()
