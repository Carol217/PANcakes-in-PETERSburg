#Carol Pan and Shaina Peters
#SoftDev1 pd7
#HW05 -- Jinja Tuning
#2017-09-27

from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route("/")
def hello_world():
    retStr = "go to occupations"
    return retStr

@app.route("/occupations")
def occupy():
    #test array to show arrays can be turned into tables
    #fakearr =[[1, 2, 3], [4, 5, 6]]
    #same code as from reader.py
    target_doc = csv.reader(open('occupations/occupations.csv', 'rU'), delimiter= ",", quotechar = "\"")
    return render_template('data.html', foo='Census of Occupations', csv=target_doc)
    return retStr

                            

if __name__ == "__main__":
    app.debug = True
    app.run()
