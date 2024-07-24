#Importing Libraries
import streamlit as st
import pandas as pd
import pickle

#Loading the file
df=pd.read_csv(r"weather_classification_data.csv")

#Logo and Title
st.image(r"inno logo png.png")
st.title("Weather ForeCast")

#Loading Pickle file
model = pickle.load(open(r"weather.pkl","rb"))


#Columns
temperature = st.number_input("Temperature",min_value=df['Temperature'].min(),max_value=df['Temperature'].max(),step=3.0)
humidity = st.number_input("Humidity",min_value=df['Humidity'].min(),max_value=df['Humidity'].max(),step=10)
wind_speed = st.number_input("Wind Speed",min_value=df['Wind Speed'].min(),max_value=df['Wind Speed'].max(),step=1.0)
precipitation = st.number_input("Precipitation (%)",min_value=df['Precipitation (%)'].min(),max_value=df['Precipitation (%)'].max(),step=5.0)
atmospheric_Pressure=st.number_input("Atmospheric Pressure",min_value=df['Atmospheric Pressure'].min(),max_value=df['Atmospheric Pressure'].max(),step=50.0)
uv_index=st.number_input("UV Index",min_value=df['UV Index'].min(),max_value=df['UV Index'].max(),step=1)
visibility=st.number_input("Visibility (km)",min_value=df['Visibility (km)'].min(),max_value=df['Visibility (km)'].max(),step=3.0)
cloud_cover=st.selectbox("Cloud Cover",['partly cloudy', 'clear', 'overcast', 'cloudy'])
season=st.selectbox("Season",['Winter', 'Spring', 'Summer', 'Autumn'])
location=st.selectbox("Locaton:",['inland', 'mountain', 'coastal'])



#Inputs
if st.button("Predict the Weather Type"):
    input_data = pd.DataFrame({
        'Temperature': [temperature],
        'Humidity': [humidity],
        'Wind Speed': [wind_speed],
        'Precipitation (%)': [precipitation],
        'Atmospheric Pressure': [atmospheric_Pressure],
        'UV Index': [uv_index],
        'Visibility (km)': [visibility],
        'Cloud Cover': [cloud_cover],
        'Season': [season],
        'Location': [location]
    })
    #Results
    predicted=model.predict(input_data)
    if predicted=="Rainy":
        st.write("Hey it's Rainy")
        st.write("Better to carry an Umbrella")
        st.image(r"Rainy.png")
    elif predicted=="Cloudy":
        st.write("oh it's Cloudy")
        st.write("Better to stay at HOME")
        st.image(r"cloudy png.webp")
    elif predicted=="Sunny":
        st.write("Hey Hey it's Sunny")
        st.write("Lets Play")
        st.image(r"sunny_image.png")
    elif predicted=="Snowy":
        st.write("Hey it's Snowy")
        st.write("lets make Snowman")
        st.image(r"snowman.webp")
