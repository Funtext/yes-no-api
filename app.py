import os
import random
from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

data = ["yes", "no"]

@app.route('/')
@cross_origin()
def one_post():
    return random.choice(data)