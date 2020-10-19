# Load dependencies
import requests
import os
import json

# Load flash
from flask import Flask, request, redirect, jsonify, render_template

app = Flask(__name__)

# Create Routes
@app.route('/')
def run():
    return render_template('index.html')

@app.route('/redact')
def redact():
    return render_template('redact.html')


@app.route("/redact2", methods=["GET", "POST"])
def redact2():

    if request.method == "POST":

        req = request.form
        card_num = req.get("card_num")
        exp_date = req["exp_date"]
        cvv = request.form["cvv"]

        response = requests.post("https://tntx1a9d8wg.SANDBOX.verygoodproxy.com/post",
                          json={'card_num': card_num ,'exp_date':  exp_date, 'cvv': cvv})
        response = response.json()
        print(response)

    return render_template('redact2.html', response=response)

@app.route('/reveal')
def reveal():
    return render_template('reveal.html')

@app.route("/reveal2", methods=["GET", "POST"])
def reveal2():

    if request.method == "POST":

        req = request.form
        card_num = req.get("card_num")
        exp_date = req["exp_date"]
        cvv = request.form["cvv"]

        os.environ['HTTPS_PROXY'] = 'http://USERNAME:PASSWORD@tntsfeqzp4a.sandbox.verygoodproxy.com:8080'
        
        response = requests.post('https://echo.apps.verygood.systems/post',
		json={'card_num': card_num ,'exp_date':  exp_date, 'cvv': cvv},
		verify=('sandbox.pem'))
        response = response.json()
        print(response)

        return render_template('reveal2.html', response=response)

if __name__ == "__main__":

    app.run(debug=True)