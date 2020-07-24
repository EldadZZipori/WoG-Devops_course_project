import Utils
from os import path
import pymysql
# this module manages the score records


# adds points to the current score in the file and prints the current score AFTER the addition
# In case the file does not exists the function will create one
def add_score(points: int):

    previous_score = 0
    current_score = 0

    # Connectting to the dockers mysql server
    conn = pymysql.connect(host=Utils.CONN_HOST, port=Utils.CONN_PORT, user=Utils.CONN_USER,
        passwd=Utils.CONN_PASSWORD, db=Utils.CONN_DB)

    try:
        # opening a cursor to fetch the current score
        with conn.cursor() as cursor:
            sql = "SELECT score FROM users_scores WHERE id=1"
            cursor.execute(sql)
            previous_score = cursor.fetchone()

        current_score = previous_score[0] + points

        # opening a cursor to update the new score
        with conn.cursor() as cursor:
            sql = "UPDATE users_scores SET score={0} WHERE id=1".format(current_score)
            cursor.execute(sql)

        conn.commit()

    # !!! Catch is needed
    finally: 
        conn.close()

    # Conversion to MySQL Usage
    #previous_score = 0
    # if path.exists(Utils.SCORES_FILE_NAME):

    #     file = open(Utils.SCORES_FILE_NAME,"r")
    #     try:
    #         previous_score = int(file.read())
    #     except ValueError:
    #         print(Utils.ERROR_MESSAGE, "Maybe try to delete Scores.txt")
    #         return

    #     file.close()

    # file = open(Utils.SCORES_FILE_NAME,"w")
    # current_score = previous_score + points
    # file.write(str(current_score))
    # file.close()

    print("\nYour current score is", current_score)

