from flask import Flask
import pandas as pd
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world, from Flask!"

@app.route('/view')
def userData():
    columns = ["id","email","firstname","lastname","age","countrycode" ]
    df = pd.read_csv('data.csv', names=columns, header=None) 
    data = str(df)
    return data


if __name__ == "__main__": 
    app.run(host="localhost", port=int("5000"))