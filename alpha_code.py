# alpha_code.py (Streamlit Application)
import streamlit as st
import joblib
import pandas as pd

# Load the trained model and label encoder
try:
    model = joblib.load('genre_prediction_model.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
except FileNotFoundError as e:
    st.error(f"Error loading model or label encoder: {e}")
    st.stop()

st.title("Music Genre Prediction")

st.sidebar.header("Enter Song Features:")
valence = st.sidebar.slider("Valence", 0.0, 1.0, 0.5)
danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.5)
tempo = st.sidebar.slider("Tempo", 50.0, 200.0, 120.0)
energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.5)
user_id = st.sidebar.text_input("User ID", "user_001")
song_id = st.sidebar.text_input("Song ID", "song_001")
# ... Add input widgets for ALL other features your model expects

if st.button("Predict Genre"):
    try:
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

        st.subheader(f"Predicted Genre: {predicted_genre}")
    except Exception as e:
        st.error(f"Prediction error: {e}")