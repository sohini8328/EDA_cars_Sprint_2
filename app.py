import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



st.header('Market data for used cars')
st.write('Filter cars with under 200,000 miles on it')

df = pd.read_csv('vehicles_us.csv')


car_model = df['model'].unique()

selected_model = st.selectbox('Select a car model', car_model)


min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider("Choose years", value=(min_year, max_year), min_value= min_year, max_value= max_year)
                                                
actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df[(df.model == selected_model) & df.model_year.isin(list(actual_range))]
df_filtered



st.header('Price analysis')
st.write('See the how the prices changes based on car transmission, type, odometer and condition')

list_for_hist = ['condition', 'type', 'transmission', 'odometer']
selected_type = st.selectbox('Split for price distribution',list_for_hist)

fig1 = px.histogram(df, x='price', color = selected_type)
fig1.update_layout(title='<b> Split for price distribution by {}<b>'.format(selected_type))
st.plotly_chart(fig1)

list_for_scatter=['odometer', 'paint_color', 'days_listed']

choice_for_scatter = st.selectbox('Price dependency on', list_for_scatter)

fig2 = px.scatter(df, x='price', y=choice_for_scatter, color= 'days_listed', hover_data= ['model_year'])

st.plotly_chart(fig2)


st.header('Car models conditions')
st.write('See the how the conditions of cars based on models')

list_for_hist = ['model', 'condition']
selected_condition = st.selectbox('Split for model conditions',list_for_hist)

fig3 = px.histogram(df, x='model', color = selected_type)
fig3.update_layout(title='<b> Split for condition of model by {}<b>'.format(selected_type))
st.plotly_chart(fig3)


agree = st.checkbox("I agree to all the terms and conditions of the website")

if agree:
      st.write("Great!")

 click = st.button('click me if ready to buy')

if click:
      st.write("Please provide contact information")