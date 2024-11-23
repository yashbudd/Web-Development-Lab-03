import streamlit as st
import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

# given text input: output 

st.header("Stock Market Information")
input = st.text_input("Choose a Symbol of a Current Stock")

graph = st.radio("Choose on the following options", ["Open", "High", "Low", "Close", "Volume"])