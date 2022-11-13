from flask import Flask, render_template, redirect, url_for, request, session, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from generateJson import create_json
import os
import json

app = Flask(__name__)

@app.route('/', methods = ["GET", 'POST'])
def home():
    return render_template('index.html', category = create_json())

@app.route('/game', methods=["GET","POST"])
def game():
    return render_template('game.html')

@app.route('/test')
def d():
    return render_template('ddd.html')

@app.route('/aidemo', methods = ["GET", "POST"])
def reload():
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)