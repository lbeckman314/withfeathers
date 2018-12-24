# a poem presenter that draws from the light side of the force.
# created: 2018-04-16
# updated: 2018-04-29
# sources:
#   https://stackoverflow.com/questions/27587127/how-to-convert-datetime-date-today-to-utc-time

from flask import Flask, request, session, g, redirect, \
        url_for, abort, render_template, flash
from datetime import datetime
from pathlib import Path
#import main
import time
import os
#from flask.ext.cache import Cache


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# app = Flask(__name__)
app = Flask(__name__, static_folder='assets')
app.config.from_object(__name__)  # load config from this file , flaskr.py
app.config.from_envvar('WITHFEATHERS', silent=True)
#cache = Cache(app, config={'CACHE_TYPE': 'simple'})


# get random poem
def update():
    poemRandom = main.main()
    poemCurrent = open(os.path.join(__location__, 'poemCurrent.txt'), "w");
    for line in poemRandom:
        poemCurrent.write(line)

    timeCurrent = open(os.path.join(__location__, 'timeInitial.txt'), "w");
    timeCurrent.write(str(int(time.time())))
    print(int(time.time()))
    # return poemCurrent

    poemCurrent.close()
    timeCurrent.close()



app = Flask(__name__)
@app.route("/")
def index():

    # declare initial time (YYYY-MM-DD)
    timeInitialFile = open(os.path.join(__location__, 'timeInitial.txt'), "r");
    timeInitialString = timeInitialFile.readline()
    timeInitial = datetime.utcfromtimestamp(int(timeInitialString)).date()

    timeCurrent = datetime.utcnow().date()

    print("timeInitial:", timeInitial)
    print("timeCurrent:", timeCurrent)

    # if there is a new day...
    if (timeCurrent > timeInitial):

        # update the poem initializer
        update()

        # update the day
        timeInitial = timeCurrent

    poemFile = open(os.path.join(__location__, 'poemCurrent.txt'), "r");
    poemString = poemFile.read()

    poemFile.close()
    timeInitialFile.close()
    timePretty = timeCurrent.strftime("%A, %B %d, %Y")
    return render_template('index.html', content=poemString, date=timePretty)


@app.route('/s')
def simple():
    poemFile = open(os.path.join(__location__, 'poemCurrent.txt'), "r");
    poemString = poemFile.read()
    poemFile.close()
    return render_template('index-minimal.html', content=poemString)


if __name__ == "__main__":
    #app.run()
    context=('ssl/fullchain.pem', 'ssl/privkey.pem')

    app.run(host="0.0.0.0", ssl_context=context, threaded=True)
