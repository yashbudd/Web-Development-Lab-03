import google.generativeai as genai
import streamlit as st
import requests

my_api_key = "AIzaSyCmg8WCBRTlouoDMkcgbRMp0ibW50uUZzo"
genai.configure(api_key=my_api_key)
st.header("Stock Market Comparison")
st.subheader("How do the opening prices of 2 stocks compare to each other?")
st.write("The world of stocks are very exciting! If you enter two stock symbols below, we can give you a detailed analysis of how they compare to each other!")
symbol = st.text_input("Choose a Symbol of a Current Stock")
symbol2 = st.text_input("Choose another Symbol of a Current Stock")

if st.button("Submit"):
    stock_key = "KDPU4BP0BEHBUVBT"
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={stock_key}'
    r = requests.get(url)
    data1 = r.json()
    url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol2}&apikey={stock_key}'
    r2 = requests.get(url2)
    data2 = r2.json()
    input = (f'Can you give me an analysis of the the opening prices over time for the stock: {symbol} with data {data1} and {symbol2} with data {data2}?')
    model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
    response = model.generate_content(input) #enter your prompt here!
    st.write(response.text) #dont forget to print your response!

    def processing(input):
        response2 = model.generate_content(input)
        return response2

    count = 0
    with st.sidebar:
        message = st.text_input("Enter your question here:", key=f"user_input_{count}")
        count += 1

    if message:
        actual_message = processing(message)
        st.write(actual_message.text)
        st.session_state.message = ""