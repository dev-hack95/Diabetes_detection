import pandas as pd
import numpy as np
import pickle
from fastapi import *
from datat import datat
import uvicorn

with open("./models/Random_Forest.pkl", 'rb') as file:
    model = pickle.load(file)




app = FastAPI()




# Api testing

@app.post("/test_api")
def test_api(data:datat):
    data = data.dict()
    Glucose= data['Glucose']
    BloodPressure= data['BloodPressure']
    SkinThickness= data['SkinThickness']
    Insulin= data['Insulin']
    BMI= data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age= data['Age']
    print(data)

    prediction = model.predict([[Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if prediction[0] == 0:
        prediction='healthy'
    else:
        prediction='diabetic'
    return {
        'prediction': prediction
    }






if __name__ == "__main__":
    uvicorn.run(app, debug=True)
