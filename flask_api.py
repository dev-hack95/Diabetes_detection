from flask import *
import numpy as np
import pickle

with open("./models/Random_forest.pkl", "rb") as file:
    model = pickle.load(file)

with open("./models/scalar.pkl", "rb") as file:
    scalar = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    data = np.array(data).reshape(1, -1)
    new_data = scalar.transform(data)
    prediction = model.predict(new_data)
    if prediction[0] == 0:
        prediction='healthy'
    else:
        prediction='diabetic'
    return render_template("home.html", prediction_text="prediction: {}".format(prediction))

if __name__ == '__main__':
    app.run(debug=True)