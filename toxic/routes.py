from flask import jsonify, render_template,request

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

@app.route('/classify',methods=["POST"])
def classifyApi():
    if request.method == "POST":
        data = request.args['data']
        prediction =  predict(data,VEC,model)
        headers = ["toxic",	"severe_toxic",	"obscene",	"threat",	"insult",	"identity_hate"]
        prediction = dict(zip(headers,prediction))
        return jsonify({"pred" : prediction,"data" : data})

