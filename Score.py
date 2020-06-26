import Utils
from os import path
# this module manages the score records


# adds points to the current score in the file and prints the current score AFTER the addition
# In case the file does not exists the function will create one
def add_score(points: int):

    previous_score = 0

    if path.exists(Utils.SCORES_FILE_NAME):

        file = open(Utils.SCORES_FILE_NAME,"r")
        try:
            previous_score = int(file.read())
        except ValueError:
            print(Utils.ERROR_MESSAGE, "Maybe try to delete Scores.txt")
            return

        file.close()

    file = open(Utils.SCORES_FILE_NAME,"w")
    current_score = previous_score + points
    file.write(str(current_score))
    file.close()

    print("\nYour current score is", current_score)

