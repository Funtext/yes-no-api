import os
import random
import requests
from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

data = ["yes", "no"]

@app.route('/')
@cross_origin()
def one_post():
    r = requests.get(url="https://api.giphy.com/v1/gifs/random?api_key=iMDy2jSTrxPi3WcTa1pwcHbf4BYq9HWH")
    data = r.json()
    gifLink = data['data']['image_url']
    return "{ \"response\":\"" + random.choice(data) + "\", \"gifLink\":\"" + gifLink + "\"}"