import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def load_data():
    data_path = 'Data/data.csv'
    return pd.read_csv(data_path)

def run():
    data = load_data()
    
    st.title("Food Waste Analysis")
    st.write("Explore food waste per capita across various countries and sectors.")
    
    if st.checkbox('Show data overview'):
        st.write(data.describe())

    selected_region = st.multiselect('Select Region', options=data['Region'].unique())
    selected_confidence = st.multiselect('Select Confidence Level', options=data['Confidence in estimate'].unique())

    filtered_data = data
    if selected_region:
        filtered_data = filtered_data[filtered_data['Region'].isin(selected_region)]
    if selected_confidence:
        filtered_data = filtered_data[filtered_data['Confidence in estimate'].isin(selected_confidence)]
    
    st.subheader('Food Waste per Capita by Country')
    fig = px.bar(filtered_data, x='Country', y='combined figures (kg/capita/year)', title='Food Waste per Capita by Country')
    st.plotly_chart(fig)
