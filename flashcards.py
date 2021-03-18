from flask import (Flask, render_template)
from datetime import datetime
app = Flask(__name__)


@app.route("/welcome")
def welcomex():
    return render_template("demo.html",message='This is a message')



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
