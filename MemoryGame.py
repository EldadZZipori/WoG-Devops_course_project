import random, time, Utils
from __main__ import app

# this module sets the functionality and the game-play of the memory game
# this game show a sequence of numbers to the user
# the user needs to type in the sequence after it disappears


# generates the numbers from 1 to 101 (both included) to be used for the game
# difficulty decides how many numbers there are
# shows the list for 0.7 secs
# returns a list of ints
def generate_sequence(difficulty: int) -> list:

    # generates the sequence of numbers
    sequence = []
    for item in range(0, difficulty):
        sequence.append(random.randint(Utils.GUESS_LOW_END, Utils.GUESS_HIGH_END))

    # shows the sequence of numbers for 0.7 sec
    print(sequence)
    time.sleep(0.7)
    Utils.screen_cleaner()

    return sequence


# gets the users input for his guess on the list of numbers he sees in generate_sequence
# the lists length is equals to difficulty
# returns a list of ints
def get_list_from_user(difficulty: int) -> list:

    # gets the users guess for the list he saw
    user_sequence = []
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    for item in range(0, difficulty):
        user_sequence.append(Utils.validate_user_input(Utils.GUESS_LOW_END, Utils.GUESS_HIGH_END, "number"))

    return user_sequence


# checks if two list are identical
# they must have the same values in the same order
# returns True or False
def is_list_equal(list_a: list, list_b: list) -> bool:
    return list_a == list_b


# starts the game with the above functions
# returns:
#   True - if user won
#   False - if user lost
@app.route('/test')
def play(difficulty: int) -> bool:

    computer_generated_sequence = generate_sequence(difficulty)
    users_sequence = get_list_from_user(difficulty)
    #return is_list_equal(computer_generated_sequence, users_sequence)
    return 1
