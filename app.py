from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from generateJson import create_json
import os

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    return create_json()

if __name__ == "__main__":
    app.run(debug=True)