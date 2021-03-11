import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App         

shown are the stock closing price and volumn of goggle !
         """)

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
