import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



st.header('Market data for used cars')
st.write('Filter cars with under 80,000 miles on it')

df = pd.read_csv('vehicles_us.csv')

df['model_year'] = df['model_year'].fillna(0)
df['cylinders'] = df['cylinders'].fillna(0)
df['paint_color']=df['paint_color'].fillna('unknown')
df['is_4wd'] = df['is_4wd'].fillna(0)


car_model = df['model'].unique()

selected_model = st.selectbox('Select a car model', car_model)

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider("Choose years", value=(min_year, max_year), min_value= min_year, max_value= max_year)
                                                
actual_range = list(range(year_range[0], year_range[1]+1))






