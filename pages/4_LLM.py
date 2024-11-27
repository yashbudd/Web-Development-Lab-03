import google.generativeai as genai
import streamlit as st
import requests

my_api_key = "AIzaSyCmg8WCBRTlouoDMkcgbRMp0ibW50uUZzo"
genai.configure(api_key=my_api_key)


if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'stock_analysis' not in st.session_state:
    st.session_state.stock_analysis = ""

st.header("Stock Market Comparison")
st.subheader("How do the opening prices of 2 stocks compare to each other?")
st.write("The world of stocks is very exciting! If you enter two stock symbols below, we can give you a detailed analysis of how they compare to each other!")

symbol = st.text_input("Choose a Symbol of a Current Stock")
symbol2 = st.text_input("Choose another Symbol of a Current Stock")


def get_analysis(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")  
    response = model.generate_content(input_text)
    return response.text


def display_conversation():
    if st.session_state.messages:
        for msg in st.session_state.messages:
            st.write(f"**You:** {msg['user']}")
            st.write(f"**Bot:** {msg['bot']}")


if st.button("Submit"):
    stock_key = "KDPU4BP0BEHBUVBT"
    
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={stock_key}'
    r = requests.get(url)
    data1 = r.json()
    
    url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol2}&apikey={stock_key}'
    r2 = requests.get(url2)
    data2 = r2.json()
    
    input_text = f'Can you give me an analysis of the opening prices over time for the stock: {symbol} with data {data1} and {symbol2} with data {data2}?'
    
    response = get_analysis(input_text)
    
    st.session_state.stock_analysis = response
    
    st.write(response)  

message = st.text_input("Ask me anything about the stocks!", key="user_message")

if message:
    response = get_analysis(message)
    
    st.session_state.messages.append({"user": message, "bot": response})

display_conversation()

st.markdown("""
    <style>
    .css-1uv9ubt {
        position: fixed;
        bottom: 10px;
        left: 0;
        right: 0;
    }
    </style>
""", unsafe_allow_html=True)
