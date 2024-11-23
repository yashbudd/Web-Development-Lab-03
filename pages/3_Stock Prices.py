import streamlit as st
import requests


# given text input: output 

st.header("Stock Market Information")
input = st.text_input("Choose a Symbol of a Current Stock")

graph = st.radio("Choose on the following options", ["Open", "High", "Low", "Close", "Volume"])

try:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={input}&apikey=demo'
    r = requests.get(url)
    data = r.json()
except:
    st.write("Enter a valid Stock Symbol (ex: IMB, APPL)")
