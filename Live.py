import Utils, MemoryGame, GuessGame, Score


# this module contains the functions for the process of the program


# gets a name and returns the welcoming statement
def welcome(name: str) -> str:
    return Utils.WELCOME_STATEMENT.replace("<name>", name)


# gets the desired game and difficulty from the user
# runs the desired game and calls the Score.py file to record the score
def load_game():
    print(Utils.GAMES_AVAILABLE)

    # game and difficulty choosing process
    game_chosen = Utils.validate_user_input(1, 2, "game")

    difficulty = Utils.validate_user_input(1, 5, "difficulty")

    game_result = None

    # running games by user's choice
    if game_chosen == 1:
        game_result = MemoryGame.play(difficulty)

    elif game_chosen == 2:
        game_result = GuessGame.play(difficulty)

    # checking weather the user won or lost - Refer to the play method in either GuessGame or MemoryGame
    if game_result:
        print("Congratulation! YOU WON")
        Score.add_score(difficulty)
    else:
        print("Close but not quit right")
        Score.add_score(0)
        load_game()

