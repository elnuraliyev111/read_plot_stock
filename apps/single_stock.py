import streamlit as st
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
    st.title('Single Stock')

    st.write('This is the `Model` page of the multi-page app.')

    st.write('The model performance of the Iris dataset is presented below.')

    # App title
    st.markdown('''
    # Stock Price App
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
    ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
    tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
    tickerData = yf.Ticker(tickerSymbol) # Get ticker data
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker


    #tickerSymbol = 'GOOGL'

    #tickerData = yf.Ticker(tickerSymbol)

    #tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end ='2020-5-31')



    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(
        go.Scatter(y=tickerDf['Close']),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(y=tickerDf['Volume']),
        row=1, col=2
    )

    fig.update_layout(height=600, width=800, title_text="Close Price and Volume")

    st.plotly_chart(fig)