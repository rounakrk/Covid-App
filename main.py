import requests
import json
import numpy as np
import pandas as pd
import datetime
from datetime import date, time, datetime

'''
{'Afghanistan': 1, 'Algeria': 1, 'Andorra': 1, 'Angola': 1, 'Argentina': 1, 'Armenia': 1, 'Australia': 9, 
'Austria': 1, 'Bahamas': 1, 'Bahrain': 1, 'Bangladesh': 1, 'Belgium': 13, 'Bolivia': 1,
 'Bosnia Herzegovina': 192, 'Brazil': 28, 'Brunei': 1, 'Bulgaria': 1, 'Canada': 17,
  'Chile': 18, 'China': 34, 'Colombia': 35, 'Croatia': 1, 'Cyprus': 1, 'Czech Republic': 192,
   'Democratic Republic of the Congo': 192, 'Denmark': 3, 'Ecuador': 1, 'Ethiopia': 1,
    'Finland': 1, 'France': 12, 'Germany': 18, 'Ghana': 1, 'Guatemala': 1, 'Hong Kong SAR': 192,
     'Hungary': 1, 'India': 38, 'Indonesia': 1, 'Iran': 1, 'Iraq': 1, 'Ireland': 1, 'Israel': 1,
      'Italy': 22, 'Ivory Coast': 192, 'Japan': 50, 'Jordan': 1, 'Kazakhstan': 1, 'Kosovo': 1,
       'Kuwait': 1, 'Kyrgyzstan': 1, 'Latvia': 1, 'Lithuania': 1, 'Luxembourg': 1, 'Macao SAR': 192,
        'Malaysia': 1, 'Malta': 1, 'Mexico': 34, 'Mongolia': 1, 'Myanmar': 192, 'Nepal': 1,
         'Netherlands': 18, 'New Caledonia': 192, 'New Zealand': 1, 'Nigeria': 1, 'North Macedonia': 1,
          'Norway': 1, 'Oman': 1, 'Pakistan': 8, 'Palestinian Territory': 
192, 'Peru': 27, 'Philippines': 1, 'Poland': 1, 'Portugal': 1, 'Puerto Rico': 192, 'Romania': 1,
 'Russia': 84, 'San Marino': 1, 'Serbia': 1, 'Singapore': 1, 'Slovakia': 1, 'Slovenia': 1,
  'South Africa': 1, 'South Korea': 192, 'Spain': 21, 'Sri Lanka': 1, 
  'Svalbard and Jan Mayen': 192, 'Sweden': 22, 'Switzerland': 1, 'Syria': 1, 
  'Taiwan': 192, 'Thailand': 1, 'Turkey': 1, 'U.S. Virgin Islands': 192, 'USA': 192,
   'Uganda': 1, 'Ukraine': 28, 'United Arab Emirates': 1, 'United Kingdom': 16, 
   'Uzbekistan': 1, 'Vietnam': 1, 'Yemen': 1}
'''

country = ['Afghanistan', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia',
 'Australia', 'Austria', 'Bahamas', 'Bahrain', 'Bangladesh', 'Belgium', 'Bolivia',
  'Bosnia Herzegovina', 'Brazil', 'Brunei', 'Bulgaria', 'Canada', 'Chile', 'China', 'Colombia',
   'Croatia', 'Cyprus', 'Czech Republic', 'Democratic Republic of the Congo', 'Denmark',
    'Ecuador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Guatemala', 'Hong Kong SAR',
     'Hungary', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast',
      'Japan', 'Jordan', 'Kazakhstan', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania', 
      'Luxembourg', 'Macao SAR', 'Malaysia', 'Malta', 'Mexico', 'Mongolia', 'Myanmar', 'Nepal',
       'Netherlands', 'New Caledonia', 'New Zealand', 'Nigeria', 'North Macedonia', 'Norway', 'Oman',
        'Pakistan', 'Palestinian Territory', 'Peru', 'Philippines', 'Poland', 'Portugal', 
        'Puerto Rico', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Singapore', 'Slovakia',
         'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Svalbard and Jan Mayen',
          'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Thailand', 'Turkey', 'U.S. Virgin Islands',
           'USA', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uzbekistan',
            'Vietnam', 'Yemen']


details = ["confirmed","recovered","deaths"]
country_data = dict()
country=['India']
for i in country:
    url = "https://covid-api.mmediagroup.fr/v1/cases?country="+i

    response = requests.get(url)
    status_get = response.content
    status_get = status_get.decode('utf-8')
    status_json = json.loads(status_get)
    # country_data[i] = len(status_json)
    value = []
    for j in details:
        value.append(status_json['All'][j])

    # print(i)
    # print(details)
    # print(value)
    # print(list(status_json.keys()))
    d = status_json['Karnataka']['updated']
    e = d.split(' ')
    print(e[1][:5])
    # print(datetime.strptime(d,'%y/%m/%d %H:%M:%S'))

# print(country_data)