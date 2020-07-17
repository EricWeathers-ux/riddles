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
@app.route('/index', methods=["GET", "POST"])
def index():
    print("index loaded")
    return render_template("index.html")

@app.route('/index2', methods=["GET", "POST"])
def index2():
    riddles=[{"riddle": ["What starts with I and ends with phone?", "Iphone"]},
    {"riddle": ["What starts with t ends with t and has t in it?", "teapot"]},
    {"riddle": ["What color is the sky?", "blue"]}
    ]
    if request.form['riddle_answer'] == riddles[random_number]["riddle"][1]:
        return render_template("index.html")
    else:
        return render_template("solve_riddle.html", Aaron=riddles[random_number])
from random import randint
@app.route('/riddle')
def riddle():
    global riddle2
    global random_number
    global riddles
    global codes
    global Riddle
    riddles=[{"riddle": ["What starts with I and ends with phone?", "Iphone"]},
    {"riddle": ["What starts with t ends with t and has t in it?", "teapot"]},
    {"riddle": ["What color is the sky?", "blue"]}
    ]
    random_number=randint(-1,2)
    Riddle=riddles[random_number]
    riddle2=Riddle
    print("RIDDLE2:")
    print(riddle2)
    codes=[]
    if randint(-1,1) == 1:
        codes.append(no_vowels(Riddle))
    else:
        codes.append(reverse_riddle(Riddle))
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
def reverse_riddle(string):
    string["riddle"][0]=string["riddle"][0][::-1]
    return string
riddle2=""
random_number=randint(-1,2)
riddles=[{"riddle": ["What starts with I and ends with phone?", "Iphone"]},
    {"riddle": ["What starts with t ends with t and has t in it?", "teapot"]},
    {"riddle": ["What color is the sky?", "blue"]}
]
Riddle=riddles[random_number]
codes=[]
@app.route('/code')
def code():
    return render_template("code.html")

@app.route('/solve_riddle', methods=['GET', 'POST'])
def solve_riddle():
    riddles=[{"riddle": ["What starts with I and ends with phone?", "Iphone"]},
    {"riddle": ["What starts with t ends with t and has t in it?", "teapot"]},
    {"riddle": ["What color is the sky?", "blue"]}
    ]
    print(Riddle["riddle"][0])
    if request.form['riddle_input'] == riddles[random_number]["riddle"][0]:
        riddles=[{"riddle": ["What starts with I and ends with phone?", "Iphone"]},
        {"riddle": ["What starts with t ends with t and has t in it?", "teapot"]},
        {"riddle": ["What color is the sky?", "blue"]}
        ]
        print("riddles[random_number]:")
        print(riddles[random_number])
        return render_template("solve_riddle.html", Aaron=riddles[random_number])
    else:
        return render_template("riddle.html", codes=codes[0])