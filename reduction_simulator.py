import streamlit as st
import plotly.graph_objects as go

def get_radar_chart(reduction_dict):
    categories = ['Household', 'Retail', 'Food Service']
    original_values = [100, 100, 100]
    adjusted_values = [
        100 - reduction_dict['household'],
        100 - reduction_dict['retail'],
        100 - reduction_dict['food_service']
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=original_values,
        theta=categories,
        fill='toself',
        name='Original',
        line=dict(color='red')
    ))
    fig.add_trace(go.Scatterpolar(
        r=adjusted_values,
        theta=categories,
        fill='toself',
        name='After Reduction',
        line=dict(color='blue')
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True
    )
    return fig

def run():
    st.title("Reduction Simulator")
    st.write("Simulate the impact of reduction strategies on food waste across different sectors.")
    
    reduction_labels = [
        ("Household Waste Reduction (%)", "household"),
        ("Retail Waste Reduction (%)", "retail"),
        ("Food Service Reduction (%)", "food_service"),
    ]
    
    reduction_dict = {}
    for label, key in reduction_labels:
        reduction_dict[key] = st.slider(label, min_value=0.0, max_value=100.0, value=10.0, step=0.1)
    
    radar_chart = get_radar_chart(reduction_dict)
    st.plotly_chart(radar_chart)

