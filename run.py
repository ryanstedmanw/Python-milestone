import os
import requests
from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    headers = {"apikey": "aefd1dc0-4edb-11eb-8062-dbb6898f3f94"}
    params = (("url","https://aliexpress.com/item/4001272494924.html"),("amount","1"),);
    response = requests.get('https://app.reviewapi.io/api/v1/reviews', headers=headers, params=params);
    return jsonify(response.text('text'))
    

@app.route("/products")
def products():
    return render_template("products.html")
    

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