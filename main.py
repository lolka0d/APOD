import streamlit as st
import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_key = config["DEFAULT"]["KEY"]
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url).json()

title = response["title"]
description = response["explanation"]
image = response["url"]

st.header(title)
st.image(image)
st.write(description)