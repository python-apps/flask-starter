from flask import (Flask, render_template)
from datetime import datetime
from model import db
app = Flask(__name__)


@app.route("/welcome")
def welcomex():
    return render_template("demo.html",message='This is a message',age=2)

@app.route("/card")
def card():
    card=db[0]
    return render_template("cardx.html",card=card)

@app.route("/")
def welcome():
     return "Hello World"

@app.route("/date")
def date():
   return "This page was served at " + str(datetime.now())

counter = 0
#lesson 2
@app.route("/count_views")
def count_views():
  global counter
  counter = counter+1
  return "This page was served at " + str(counter) + " times"

if __name__ == "__main__":
  app.run()
