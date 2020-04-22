from flask import Flask, render_template, request, redirect
from modules.naivebayes import NaiveBayes
from modules.data import Dataset, Labels
import math
import os, sys
import numpy as np
import webbrowser


cache = dict()
nb = NaiveBayes()
ds = Dataset('train').fetch()
nb.train(ds)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")
  

@app.route("/result", methods=['POST'])
def processResults():
    searchValue = request.form["searchValue"]

    if searchValue not in cache:
        y = nb.predict(searchValue)
        cache[searchValue] = render_template("results.html", searchValue=searchValue, result=y)
    return cache[searchValue]
   

if __name__ == "__main__":
    app.run(debug=True)





