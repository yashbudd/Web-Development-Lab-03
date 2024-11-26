import streamlit as st
import requests
import pandas as pd
import plotly.express as px


# given text input: output 

st.header("Stock Market Information")
input_var = st.text_input("Input a symbol of a current stock, use a comma seperated list if you would like to compare stocks")

graph = st.radio("Choose on the following options", ["Open", "High", "Low", "Close", "Volume"])

if st.button("Submit"):
    if input_var:
        symbols = [symbol.strip() for symbol in input_var.split(",")]
        combined_data = pd.DataFrame()
        api_key = "KDPU4BP0BEHBUVBT"
        for symbol in symbols:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
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
                df[graph] = df[graph].astype(float)
                df["Symbol"] = symbol
                combined_data = pd.concat([combined_data, df[[graph, "Symbol"]]], axis=0)
            else:
                st.warning(f"No data available for {symbol}. Please check again.")
            
        if not combined_data.empty:
            st.write("Data fetched successfully!")
            fig = px.line(
                    combined_data,
                    x=combined_data.index,
                    y=graph,
                    color="Symbol",
                    title=f"{graph} Prices for Selected Stocks",
                    labels={"value": graph, "index": "Date", "Symbol": "Stock Symbol"}
                )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Enter a valid Stock Symbol (e.g., IBM, AAPL).")
    else:
        st.warning("Please enter a stock symbol.")
        