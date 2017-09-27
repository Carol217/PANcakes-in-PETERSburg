from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "go to occupations"

@app.route("/occupations")
def occupy():
    fakearr =[[1, 2, 3], [4, 5, 6]]
    target_doc = csv.reader(open('occupations.csv', rU), delimiter
    return render_template('data.html', foo='title', csv=csv)

if __name__ == "__main__":
    app.debug = True
    app.run()
