import requests
import json
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px


details = ["confirmed","recovered","deaths"]
country = ['Afghanistan', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia',
 'Australia', 'Austria', 'Bahamas', 'Bahrain', 'Bangladesh', 'Belgium', 'Bolivia',
  'Brazil', 'Brunei', 'Bulgaria', 'Canada', 'Chile', 'China', 'Colombia',
   'Croatia', 'Cyprus', 'Denmark',
    'Ecuador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Guatemala',
     'Hungary', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
      'Japan', 'Jordan', 'Kazakhstan', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania', 
      'Luxembourg', 'Malaysia', 'Malta', 'Mexico', 'Mongolia', 'Myanmar', 'Nepal',
       'Netherlands', 'New Zealand', 'Nigeria', 'North Macedonia', 'Norway', 'Oman',
        'Pakistan', 'Peru', 'Philippines', 'Poland', 'Portugal', 
        'Romania', 'Russia', 'San Marino', 'Serbia', 'Singapore', 'Slovakia',
         'Slovenia', 'South Africa', 'Spain', 'Sri Lanka',
          'Sweden', 'Switzerland', 'Syria',  'Thailand', 'Turkey',
            'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uzbekistan',
            'Vietnam', 'Yemen']
states=[]
status_json = dict()

st.sidebar.title("Covid Report")
st.sidebar.subheader("Choose the country.")
option = st.sidebar.selectbox('', country, key=1)
url = "https://covid-api.mmediagroup.fr/v1/cases?country="+option
response = requests.get(url)
status_get = response.content
status_get = status_get.decode('utf-8')
status_json = json.loads(status_get)

st.sidebar.subheader("Choose either All(for country) or any other state present.")
option2 = st.sidebar.selectbox('', list(status_json.keys()), key=2)

st.title("Covid 19 updated chart")

pressed = st.sidebar.button('Press me?',key=1)
if pressed:
    
    value = []
    for j in details:
        value.append(status_json[option2][j])


    fig = px.bar(x=details, y=value, title=option2, color=value, text=value, )
    st.plotly_chart(fig, use_container_width=True)

    if option2!='All':
        d = status_json[option2]['updated'].split()
        st.write("Last updated on date "+d[0]+" at time "+d[1][:5])


    
