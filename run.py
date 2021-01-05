import os
import json
import requests
from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/products")
def products():
    headers = {"apikey": "aefd1dc0-4edb-11eb-8062-dbb6898f3f94"}
    params = (("url","https://www.capterra.com/p/140650/Recruitee/reviews"),("amount","1"),)
    response = requests.get('https://app.reviewapi.io/api/v1/reviews', headers=headers, params=params)
    return render_template("products.html", test=response.text)
    

@app.route("/about")
def about():
    return render_template("about.html")
    


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
