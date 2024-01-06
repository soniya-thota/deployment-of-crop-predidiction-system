import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))  # Replace with your actual model file
st.title('Crop Prediction')

N = st.text_input('Enter Nitrogen amount: ')
P = st.text_input('Enter Phosphorous amount: ')
K = st.text_input('Enter Potassium amount: ')
T = st.text_input('Enter Temperature: ')
H = st.text_input('Enter Humidity level: ')
PH = st.text_input('Enter pH level: ')
R = st.text_input('Enter Rainfall level: ')

if st.button('Predict'):
    # Convert user input to the appropriate data type
    data = [float(N), float(P), float(K), float(T), float(H), float(PH), float(R)]

    # Make predictions
    result = model.predict([data])

    # Display the result
    st.success(f"The predicted crop is: {result[0]}")

