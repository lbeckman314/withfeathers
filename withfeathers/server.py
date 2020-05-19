from datetime import datetime
from flask import Flask, request, session, g, redirect, \
        url_for, abort, render_template, render_template_string, flash
import mistune
from pathlib import Path
from withfeathers import getPoem
import os
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = Flask(__name__, static_folder='assets')
app.config.from_object(__name__)  # load config from this file , flaskr.py
app.config.from_envvar('WITHFEATHERS', silent=True)

# get random poem
def update():
    poemRandom = getPoem()
    poemCurrent = open(os.path.join(__location__, 'poemCurrent.txt'), "w");
    for line in poemRandom:
        poemCurrent.write(line)
    poemCurrent.close()


app = Flask(__name__)
@app.route("/")
def index():
    # declare initial time (YYYY-MM-DD)
    timeFile = open(os.path.join(__location__, 'timeInitial.txt'), "r+");
    timeCurrent = datetime.utcnow().date()
    timeInitial = datetime.strptime(timeFile.readline(), "%Y-%m-%d\n").date()

    # if there is a new day...
    if (timeCurrent > timeInitial):
        # update the poem initializer
        update()
        # update the day
        timeFile.seek(0)
        timeFile.write(str(timeCurrent))

    poemFile = open(os.path.join(__location__, 'poemCurrent.txt'), "r");
    poemString = poemFile.read()
    poemFile.close()
    timeFile.close()
    timePretty = timeCurrent.strftime("%A, %B %d, %Y")
    return render_template('index.html', content=poemString, date=timePretty)


@app.route('/s/')
def simple():
    poemFile = open(os.path.join(__location__, 'poemCurrent.txt'), "r");
    poemString = poemFile.read()
    poemFile.close()
    return render_template('index-minimal.html', content=poemString)

if __name__ == "__main__":
    context=('ssl/fullchain.pem', 'ssl/privkey.pem')
    app.run(host="0.0.0.0", ssl_context=context, threaded=True)

