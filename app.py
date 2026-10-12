import streamlit as st
import pandas as pd
from fetch_data import get_cars
st.title("Car Rental Dashboard")
df=get_cars()
st.write=("Total Cars")
st.metric("Total Cars:",len(df))


#Add serach functionality
search=st.text_input("Search by brand")
if search:
   df1=df[df['brand'].str.contains(search,case=False)]
   st.dataframe(df1)

#ADD filter functionality
#filter=st.selectbox("Filter by brnad",df['brand'].unique()]
multiselect=st.multiselect("Select multiple values",df['brand'].unique())
#if filter:
#  df=df[df['brand']==filter]
if multiselect:
    df=df[df['brand'].isin(multiselect)]
st.dataframe(df)

#ADD Chart functionality
st.bar_chart(df.groupby('brand').size())
