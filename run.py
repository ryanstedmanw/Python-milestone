import os
import json
import requests
import docx
import pandas as pd
import numpy as np
from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/products")
def products():
    headers = {"apikey": "aefd1dc0-4edb-11eb-8062-dbb6898f3f94"}
    params = (("url","https://www.capterra.com/p/140650/Recruitee/reviews"),("amount","1"))
    response = requests.get('https://app.reviewapi.io/api/v1/reviews', headers=headers, params=params)
    data = response.json()
    test = (data)
    return render_template("products.html", test=test)
    
@app.route("/test")
def test():
    doc = docx.Document("static/YuBambu.docx")
    df = pd.DataFrame()
    tables = doc.tables[0]
##Getting the original data from the document to a list
    ls =[]
    for row in tables.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                ls.append(paragraph.text)
    product_dict =	{
        "Product Name": "",
        "Product Price": "",
        "Manufacturer Price": "",
        "Shipping Price": "",
        "Shipping Times": "",
        "Category ": "",
    }
    
    return render_template("test.html", text=product_dict('Product Name'))

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
