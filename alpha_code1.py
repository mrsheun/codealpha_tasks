# alpha_code.py (Flask Application)
from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model and label encoder
try:
    model = joblib.load('genre_prediction_model.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
except FileNotFoundError as e:
    print(f"Error loading model or label encoder: {e}")
    raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            valence = float(request.form['valence'])
            danceability = float(request.form['danceability'])
            tempo = float(request.form['tempo'])
            energy = float(request.form['energy'])
            user_id = request.form['user_id']
            song_id = request.form['song_id']
            # ... Get all other input features from the form

            input_data = pd.DataFrame({
                'valence': [valence],
                'danceability': [danceability],
                'tempo': [tempo],
                'energy': [energy],
                'user_id': [user_id],
                'song_id': [song_id],
                # ... Add all other features here in the correct order
            })

            prediction_encoded = model.predict(input_data)
            predicted_genre = label_encoder.inverse_transform(prediction_encoded)[0]

            return render_template('result.html', prediction=predicted_genre)
        except Exception as e:
            print(f"Prediction error: {e}")
            return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)