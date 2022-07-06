from fileinput import filename
from flask import render_template,request, url_for

from toxic import app

@app.route('/')
def home():
    return render_template('homepage.html')