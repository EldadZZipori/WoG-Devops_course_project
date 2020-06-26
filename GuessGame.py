import Utils
from random import randint


# this module contains the function needed to run the Guess Game


# generates a number between 1 and the games difficulty
def generate_number(difficulty: int) -> int:
    return randint(1,difficulty)


# asks the user for a guess between 1 to difficulty, returns the users guess
def guess_from_user(difficulty: int) -> int:
    return Utils.validate_user_input(1, difficulty, "guess")


# checks weather the generated number is the same as the users guess
# calls guess_from_user to get the users input
def compare_results(difficulty: int, secret_number: int) -> bool:
    return guess_from_user(difficulty) == secret_number


# starts the game by using the above functions
# returns:
#   True - if user won
#   False - if user lost
def play(difficulty: int) -> bool:

    secret_number = generate_number(difficulty)
    return compare_results(difficulty, secret_number)
