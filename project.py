import random
import pyfiglet
from datetime import datetime

class GuessGame:
    def __init__(self):   # <-- also fixed to init
        self._number = random.randint(1, 20)
        self._attempts = 0
        self._start_time = datetime.now()  # game start time

def main():
    # Big decorative ASCII title
    ascii_title = pyfiglet.figlet_format("GUESS IT!", font="slant")
    print(ascii_title)
    print("Welcome! Guess a number between 1-20.\n")
    game = GuessGame()
    play(game)

def get_guess(test_input=None):
    """
    If test_input is provided, uses it instead of input().
    This allows testing without interactive input.
    """
    while True:
        try:
            guess = test_input if test_input is not None else input("Your guess: ")
            guess = int(guess)
            if 1 <= guess <= 20:
                return guess
            print("Enter a number between 1 and 20 ❗")
        except ValueError:
            print("Invalid ❌ Enter a number.")
        # Break loop for test_input to avoid infinite loop
        if test_input is not None:
            return None

def check_guess(guess, game):
    game._attempts += 1
    if guess < game._number:
        print("Guess a higher Number...⬆️")
        return False
    elif guess > game._number:
        print("Guess a lower Number... ⬇️")
        return False
    else:
        print(f"Correct! {guess} is the number! ✅")
        print(f"You guessed it in {game._attempts} tries {'👍'*game._attempts}")

        # Calculate total time taken
        time_taken = datetime.now() - game._start_time
        print(f"⏳ Time taken: {time_taken.seconds} seconds")

        # Determine result and stars
        if game._attempts <= 2:
            result = "Excellent"
            stars = "⭐" * 5
        elif 3 <= game._attempts <= 5:
            result = "Very Good"
            stars = "⭐" * 4
        elif 6 <= game._attempts <= 8:
            result = "Good"
            stars = "⭐" * 3
        else:
            result = "Satisfactory"
            stars = "⭐"

        # Print result in an ASCII table
        print("+----------------------+")
        print(f"| Result: {result:<11} {stars:<6} |")
        print("+----------------------+")
        return True

def play(game):
    while not check_guess(get_guess(), game):
        pass

# Fixed entry point
if __name__ == "__main__":   # <-- fixed here too
    main()
