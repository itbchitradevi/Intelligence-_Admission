import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
app=Flask(__name__)
from tensorflow.keras.models import load_model
model=load_model('model.h5')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/y_predict',methods=['Post'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    min1=[290.0,92.0,1.0,1.0,1.0,6.8,0.0]
    max1=[340.0,120.0,5.0,5.0,5.0,9.92,1.0]
    k=[float(x) for x in request.form.value()]
    p=[]
    for i in range(7):
        1=(k[i]-min[i])/(max1[i]-min1[i])
        p.append(1)
        prediction=model.predict([p])
        print(prediction)
        output=prediction[0]
        if(output==False):
            return render_template('noChance.html',prediction_text='you dont have a chance of getting admmission')
        else:
            return render_template('chance.html',prediction_text='you have a chance of getting admission')
        if__name__=="__main__":
            app.run(debug=False)
