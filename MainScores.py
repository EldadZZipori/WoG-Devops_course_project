import Utils
from flask import Flask


# this module runs a server on the hosts computer
# the server returns an html website with the current score
# website is accessible when running the module on - http://0.0.0.0:8777/


# the Flask object constructor
# giving the __name__ lets Flask fetch resources for the program and look up files
# read https://www.geeksforgeeks.org/__name__-special-variable-python/ for more information about __name__
app = Flask(__name__)

import MemoryGame

# inserts our functionality to the app.route function
# the functionality returns an html code for showing the user's score
# the '/' argument provided for app.route tells flask what function to trigger at '/'
@app.route('/')
def score_server():

    try:
        score = open(Utils.SCORES_FILE_NAME, "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.ERROR_MESSAGE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    # starts the server on 0.0.0.0 ip with accessible through port 8777
    # debug lets the server reload when it detects code change and provides a debugger if something goes wrong
    # threaded mode enables handling more than one request at a time
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8080)