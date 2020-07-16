# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)
riddle2=""

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

from random import randint
@app.route('/riddle')
def riddle():
    global riddle2
    riddles=[{"riddle": ["What starts with I and ends with phone?", "Iphone"]},
    {"riddle": ["What starts with t ends with t and has t in it?", "teapot"]}
    ]
    Riddle=riddles[randint(-1,1)]
    riddle2=Riddle
    codes=[no_vowels(Riddle)]
    return render_template("riddle.html", codes=codes[0])
def no_vowels(string):
    string2=string
    vowels=["a","e","i","o","u","y","A","E","I","O","U","Y"]
    for vowel in vowels:
        print(string2)
        string2["riddle"][0]=string2["riddle"][0].replace(vowel,"_")
    #     print(string2["riddle"][0].replace(vowel,"_"))
    # print(string2)
    return string2
riddle2=""
@app.route('/code')
def code():
    return render_template("code.html")

@app.route('/solve_riddle', methods=['GET', 'POST'])
def solve_riddle():
    print("RIDDLE2:")
    print(riddle2)
    return render_template("solve_riddle.html", riddle2=riddle2)