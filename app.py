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
    url = 'https://api.giphy.com/v1/gifs/random'
    myobj = {'api_key': 'iMDy2jSTrxPi3WcTa1pwcHbf4BYq9HWH'}
    x = requests.post(url, data = myobj)
    return random.choice(data) + x