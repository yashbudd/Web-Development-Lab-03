import google.generativeai as genai
import os
import streamlit as st

my_api_key = "AIzaSyCmg8WCBRTlouoDMkcgbRMp0ibW50uUZzo"
genai.configure(api_key=my_api_key)

st.header("Stock Market Prediction")

symbol = st.text_input("Choose a Symbol of a Current Stock")

date = st.text_input("Enter a date in the future")

input = st.text_input("Enter a prompt for the chatbot")

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
response = model.generate_content(input) #enter your prompt here!
st.write(response.text) #dont forget to print your response!