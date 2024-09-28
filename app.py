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





