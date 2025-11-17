import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go



data =  pd.read_csv(r"Dataset/bitcoin_price_Training - Training.csv")

# @nd step 
data['Date'] = pd.to_datetime(data['Date'])
data  = data.sort_index(ascending=False).reset_index()
data.drop('index',axis=1,inplace=True)
data.set_index(data['Date'],inplace=True)
# for 2nd plot 
data['Close_price_pct_change'] = data['Close'].pct_change()*100














# Title of App
st.title("Bitcoin Data Analysis")
st.set_page_config(page_title="Bitcoin Dashboard",layout="wide")
st.title('Comprehensive Bitcoin Price Analysis Dashboards')



# !st plot of Candlesticks
st.subheader("Bitcoin Candlestick Chart ( First 10days)")
bitcoin_sample  = data[0:100]
trace = go.Candlestick(x=bitcoin_sample['Date'],
               high=bitcoin_sample['High'],
               open=bitcoin_sample['Open'],
               close=bitcoin_sample['Close'],
               low=bitcoin_sample['Low'])
candle_data  = [trace]

layout={
    'title':'Bitcoin Historical Price',
    'xaxis':{'title':'Date'}
}

fig = go.Figure(data=candle_data,layout=layout)

fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig,use_container_width=True)


# 2nd plot 
st.subheader("Close price % change over a period ")

fig_pct  = go.Figure([
    go.Scatter(x  = data.index , 
               y = data['Close_price_pct_change'],
               mode = "lines")

])

fig_pct.update_layout(
    xaxis_title ="Data",
    yaxis_title = "precentage_change",
    template = "plotly_white"
)
#px.line(data, y='Close_price_pct_change', title='Close Price % Change')
st.plotly_chart(fig_pct ,use_container_width=True)

#rd plot
st.subheader("Bitcoin Price Trends Time")
price_type  = st.selectbox("Select Price type",options={'Open','High','Low','Close'},index=3)

fig_trend  = go.Figure([
    go.Scatter(x  = data.index , 
               y = data[price_type],
               mode = "lines")

])

fig_trend.update_layout(
    title = price_type + "Price Over Time",
    xaxis_title ="Data",
    yaxis_title = "Price USD",
    template = "plotly_white")

st.plotly_chart(fig_trend ,use_container_width=True)



# 4th plot

col1 , col2 , col3  = st.columns(3)
with col1 :
    st.subheader("yearly bases average CLose Price")
    yearly_avg = data['Close'].resample('YE').mean()
    fig_year = px.bar(
        x =  yearly_avg.index.strftime("%Y") , 
        y  = yearly_avg.values ,
        labels= { 'x': "year","y":"Avegae values"},
        title="yearly_avg_trend"

    )

    st.plotly_chart(fig_year , use_container_width=True)    


with col2 :
    st.subheader("Quarterly bases average CLose Price")
    Quarterly_avg = data['Close'].resample('QE').mean()
    fig_quarter = px.bar(
        x =  Quarterly_avg.index.strftime("%Y") , 
        y  = Quarterly_avg.values ,
        labels= { 'x': "Quarter","y":"Avegae values"},
        title="Quarterly_avg_trend"

    )

    st.plotly_chart(fig_quarter , use_container_width=True)



with col3 :
    st.subheader("Quarterly bases average CLose Price")
    Monthly_avg = data['Close'].resample('ME').mean()
    fig_monthly = px.bar(
        x =  Monthly_avg.index.strftime("%Y") , 
        y  = Monthly_avg.values ,
        labels= { 'x': "Month","y":"Avegae values"},
        title="Monthly_avg_trend"

    )

    st.plotly_chart(fig_monthly , use_container_width=True)    
