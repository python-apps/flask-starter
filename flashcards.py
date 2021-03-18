from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(
        "welcome.html"
        
    )

@app.route("/date")
def date():
   return "This page was served at " + str(datetime.now())

if __name__ == "__main__":
  app.run()
