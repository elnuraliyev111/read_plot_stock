import streamlit as st
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import yfinance as yf
import streamlit as st
import pandas as pd 
import plotly.figure_factory as ff
import plotly.express as px
import cufflinks as cf
import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def app():

    # App title
    st.markdown('''
    # Spread of Two Stocks App
    Shown are the stock price data for query companies!
    **Credits**
    - App built by Elnur Aliyev
    - Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
    ''')
    st.write('---')

    # Sidebar
    st.sidebar.subheader('Query parameters')
    start_date = st.sidebar.date_input("Start date", datetime.date(2010, 1, 1))
    end_date = st.sidebar.date_input("End date", datetime.date(2022, 5, 31))

    # Retrieving tickers data
    ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt', header = None)
    firsttickerSymbol = st.sidebar.selectbox('First Stock', ticker_list, index = 197) # Select ticker symbol
    firsttickerData = yf.Ticker(firsttickerSymbol) # Get ticker data
    firsttickerDf = firsttickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker
    secondtickerSymbol = st.sidebar.selectbox('Second Stock', ticker_list, index = 198) # Select ticker symbol
    secondtickerData = yf.Ticker(secondtickerSymbol) # Get ticker data
    secondtickerDf = secondtickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker


#    fig = make_subplots(rows=1, cols=2)
#    fig.add_trace(
#        go.Scatter(x = firsttickerDf.index, y=firsttickerDf['Close'], name = firsttickerSymbol),
#        row=1, col=1
#    )

#    fig.add_trace(
#        go.Scatter(x = secondtickerDf.index, y=secondtickerDf['Close'], name = secondtickerSymbol),
#        row=1, col=2
#    )

#    fig.update_layout(height=600, width=800, title_text="Close Price for " + firsttickerSymbol + " and " + secondtickerSymbol)

#    st.plotly_chart(fig)
    #st.write(secondtickerDf)
    
    trace2 = go.Figure()
    trace2.add_trace(go.Scatter(x = firsttickerDf.index, y=firsttickerDf['Close'], name = firsttickerSymbol))
    trace2.add_trace(go.Scatter(x = secondtickerDf.index, y=secondtickerDf['Close'], name = secondtickerSymbol))

    st.plotly_chart(trace2)
    #print(ticker_list)