import streamlit as st
import requests
import pandas as pd


# given text input: output 

st.header("Stock Market Information")
input_var = st.text_input("Choose a Symbol of a Current Stock")

graph = st.radio("Choose on the following options", ["Open", "High", "Low", "Close", "Volume"])

if st.button("Submit"):
    if input_var:
        api_key = "KDPU4BP0BEHBUVBT"
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={input_var}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        if "Time Series (Daily)" in data:
            time_series = data["Time Series (Daily)"]

            df = pd.DataFrame.from_dict(time_series, orient="index")
            df = df.rename(columns={
                "1. open": "Open",
                "2. high": "High",
                "3. low": "Low",
                "4. close": "Close",
                "5. volume": "Volume"
            })

            df.index = pd.to_datetime(df.index)
            df = df.sort_index()
            

            st.write("Data fetched successfully!")
            if graph == "Volume":
                    st.line_chart(df["Volume"].astype(float), use_container_width=True)
            else:
                st.line_chart(df[graph].astype(float), use_container_width=True)
        else:
            st.error("Enter a valid Stock Symbol (e.g., IBM, AAPL).")
    else:
        st.warning("Please enter a stock symbol.")
