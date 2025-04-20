import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load('california_housing_price_model.pkl')

st.title('California Housing Price Predictor')

# Create input fields
st.subheader('Enter District Information')
longitude = st.slider('Longitude', -124.0, -114.0, -122.0)
latitude = st.slider('Latitude', 32.0, 42.0, 37.0)
housing_age = st.slider('Housing Median Age', 1, 52, 25)
total_rooms = st.number_input('Total Rooms', 1, 20000, 2000)
total_bedrooms = st.number_input('Total Bedrooms', 1, 5000, 500)
population = st.number_input('Population', 1, 10000, 1500)
households = st.number_input('Number of Households', 1, 5000, 500)
median_income = st.slider('Median Income (in tens of thousands)', 0.0, 15.0, 5.0)
ocean_proximity = st.selectbox('Ocean Proximity', 
                              ['<1H OCEAN', 'INLAND', 'NEAR BAY', 'NEAR OCEAN', 'ISLAND'])

# Calculate engineered features
rooms_per_household = total_rooms / households if households > 0 else 0
bedrooms_ratio = total_bedrooms / total_rooms if total_rooms > 0 else 0
population_per_household = population / households if households > 0 else 0

# Create prediction button
if st.button('Predict House Value'):
    # Create a dataframe with the input values
    input_data = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity],
        'rooms_per_household': [rooms_per_household],
        'bedrooms_ratio': [bedrooms_ratio],
        'population_per_household': [population_per_household]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display result
    st.success(f'Predicted Median House Value: ${prediction[0]:,.2f}')
    
    # Show feature importance if available
    st.subheader('Understanding this prediction:')
    st.write('Key factors influencing California housing prices:')
    st.write('- Location (latitude, longitude, and ocean proximity)')
    st.write('- Median income of residents')
    st.write('- Housing density features (rooms per household)')
    st.write('- Neighborhood age and characteristics')