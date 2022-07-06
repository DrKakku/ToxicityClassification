from crypt import methods
from fileinput import filename
from flask import render_template,request, url_for

from toxic import app
from toxic.predict import predict
import os
from toxic.predict import getGloveCorpus
from tensorflow.keras.models import load_model


VEC = getGloveCorpus()
model = load_model("./model/lstmModel.hdf5")


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html',route = os.getcwd())


@app.route('/predict',methods=["GET","POST"])
def getData():
    if request.method == "POST":
        form = request.form
        data = form["data"]
        prediction =  predict(data,VEC,model)
        return render_template("Prediction.html",pred = prediction,data = data)
