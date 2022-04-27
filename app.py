from flask import Flask, request,render_template, url_for ,flash , redirect
from flask import send_from_directory
import joblib
import numpy as np
#from requests import request
import tensorflow
import os
import tensorflow as tf
import keras as K 
import sklearn 
app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

'''@app.route('/')
def hello_world():
    return 'Hello, World!' '''

@app.route("/")



@app.route("/index")
def index():
    return render_template("index.html")

#navbar elements

@app.route("/about")
def home():
    return render_template("about.html")

@app.route("/blogs")
def blog():
    return render_template("blog.html")

@app.route("/Achievements")
def Achievements():
    return render_template("Achievements.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact.html")


#start button - index.html-> Activities

@app.route("/ActivitiesForYou")
def secondpage():
    return render_template("Secondpage.html")


# Medical checkup
@app.route("/DiseaseDescription")
def DiseaseDescription():
    return render_template("DiseaseDescription.html")


@app.route("/CancerForm")
def cancerForm():
    return render_template("cancerForm.html")

@app.route("/DiabetesForm")
def DiabetesForm():
    return render_template("diabetesForm.html")


@app.route("/HeartForm")
def heartForm():
    return render_template("heartForm.html")

@app.route("/LiverForm")
def LiverForm():
    return render_template("liverForm.html")


@app.route("/KidneyForm")
def KidneyForm():
    return render_template("kidneyForm.html")

@app.route("/MalariaForm")
def malariaForm():
    return render_template("malariaForm.html")

@app.route("/PneumoniaForm")
def pneumoniaForm():
    return render_template("pneumoniaForm.html")


#**************** Model Integration*********************#

from keras.models import load_model

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = joblib.load("models/diabetes_model")
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = joblib.load("models/cancer_model")
        result = loaded_model.predict(to_predict)
    elif(size==12):#Kidney
        loaded_model = joblib.load("models/Kidney_model")
        result = loaded_model.predict(to_predict)
    elif(size==11):#Heart
        loaded_model = joblib.load("models/heart_model")
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
        elif(len(to_predict_list)==12):
            result = ValuePredictor(to_predict_list,12)
        elif(len(to_predict_list)==11):
            result = ValuePredictor(to_predict_list,11)
           
    if(int(result)==1):
        prediction='Sorry ! Suffering'
    else:
        prediction='Congrats ! you are Healthy' 
    return(render_template("result.html", prediction=prediction))




if __name__ == "__main__":
    app.run(debug='True')
    
