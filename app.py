#Carol Pan and Shaina Peters
#SoftDev1 pd7
#HW05 -- Jinja Tuning
#2017-09-27

from flask import Flask, render_template, url_for
import csv
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
	retStr = "<a href='" + url_for('occupy') + "'>go to occupations<a>"
	return retStr

@app.route("/occupations")
def occupy():
	#test array to show arrays can be turned into tables
	#fakearr =[[1, 2, 3], [4, 5, 6]]
	#same code as from reader.py
	target_doc = csv.reader(open('data/occupations.csv', 'rU'), delimiter= ",", quotechar = "\"")
	target_doc2 = csv.reader(open('data/occupations.csv', 'rU'), delimiter= ",", quotechar = "\"") #You need a second one because jinja only lets you cycle through an array once
	r = random.random()*98.8 #Number slightly reduced due to jinja being weird
	return render_template('data.html', title='Census of Occupations', csv=target_doc, rand=r, csv2=target_doc2)
	return retStr



if __name__ == "__main__":
	app.debug = True
	app.run()
