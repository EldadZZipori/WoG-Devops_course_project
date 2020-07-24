import os

# This library contains the constant variables and reusable functions for the whole project
# NOTICE! multi line text will stat with a new line, and end without one

GUESS_LOW_END = 1
GUESS_HIGH_END = 101
SCORES_FILE_NAME = "Scores.txt"
CONN_HOST = "127.0.0.1"
CONN_PORT = 3306
CONN_USER = "root"
CONN_PASSWORD = "pswd"
CONN_DB = "games"
ERROR_MESSAGE = "Something went wrong.."
WELCOME_STATEMENT = '''
Hello <name> and welcome to the World of Games (WoG).
Here you can find many cool games to play.'''

GAMES_AVAILABLE = '''
Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer'''

USER_INPUT_SELECTION = '''
Please enter a <selection> from <low_end> to <high_end>: '''


# GUESS_LOW_END contains the smallest number used in the Guess Game
# GUESS_HIGH_END contains the largest number used in the Guess Game
# SCORES_FILE_NAME contains the default path and file for the scores records
# ERROR_MESSAGE contains the default message for an error in the project
# WELCOME_STATEMENT contains the first text the user get when he loads the game
# GAMES_AVAILABLE contains in the text of the list of games available for the user
# USER_INPUT_SELECTION contains the test for getting user input


# clears the screen for both unix and windows based computers
def screen_cleaner():
    os.system("cls" if os.name == "nt" else "clear")


# validates user number input , returns the input
# this function allows wrong number input, but will return an error otherwise
def validate_user_input(low_end:int , high_end: int, selection: str) -> int:

    user_input = ""

    try:
        user_input = int(input((((
                        USER_INPUT_SELECTION
                        .replace("<selection>", selection))
                        .replace("<low_end>", str(low_end)))
                        .replace("<high_end>", str(high_end)))))

        while user_input < low_end or user_input > high_end:
            user_input = int(input("Please enter a valid selection: "))

    except ValueError as e:
        print(ERROR_MESSAGE)
        exit()

    return user_input
