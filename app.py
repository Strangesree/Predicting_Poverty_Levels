from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
import os
import pickle
import warnings

app = Flask(__name__)

# with open('random_forest_classifier_model.pkl', 'rb') as file:
#     loaded_model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    rooms = int(request.form['rooms'])
    males_12_younger = int(request.form['males_12_younger'])
    males_12_older = int(request.form['males_12_older'])
    total_males = int(request.form['total_males'])
    females_12_younger = int(request.form['females_12_younger'])
    females_12_older = int(request.form['females_12_older'])
    total_females = int(request.form['total_females'])
    persons_12_younger = int(request.form['persons_12_younger'])
    persons_12_older = int(request.form['persons_12_older'])
    ceiling = int(request.form['ceiling'])
    num_children = int(request.form['num_children'])
    overcrowding = float(request.form['overcrowding'])
    years_of_schooling = int(request.form['years_of_schooling'])
    walls = int(request.form['walls'])
    roof = int(request.form['roof'])
    floor = int(request.form['floor'])


    feature_list = [rooms,males_12_younger,males_12_older,total_males,females_12_younger,females_12_older,total_females,persons_12_younger,persons_12_older,ceiling,num_children,overcrowding,years_of_schooling,walls,roof,floor]
    single_pred = np.array(feature_list).reshape(1, -1)
    
    prediction = loaded_model.predict(single_pred)
    val = int(prediction[0])
    class_dict = {1: "Non Vulnerable", 2: "Moderate Poverty", 3: "Vulnerable", 4: "Extereme Poverty"}

    if prediction[0] in class_dict:
        clas = class_dict[prediction[0]]
        result = "{} class".format(clas)
    else:
        result = "Sorry, we could not determine the classify with the provided data."

    return render_template('home.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)