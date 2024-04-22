import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

@st.cache
def load_data():
    data_path = 'Data/data.csv'
    data = pd.read_csv(data_path)
    # Get unique regions before modifying the DataFrame
    unique_regions = data['Region'].unique()
    # Create dummy variables for region
    data = pd.get_dummies(data, columns=['Region'], drop_first=True)
    return data, unique_regions

def run():
    data, unique_regions = load_data()
    st.title("Predictive Modeling of Food Waste by Region")
    st.write("Predict waste amounts in household, retail, and food service sectors based on region.")

    # Prepare the data
    X = data.drop(['Country', 'combined figures (kg/capita/year)', 'Confidence in estimate', 'M49 code', 'Source'], axis=1)
    y_household = data['Household estimate (kg/capita/year)']
    y_retail = data['Retail estimate (kg/capita/year)']
    y_food_service = data['Food service estimate (kg/capita/year)']

    # Splitting data for each sector model
    X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(X, y_household, test_size=0.2, random_state=42)
    X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y_retail, test_size=0.2, random_state=42)
    X_train_f, X_test_f, y_train_f, y_test_f = train_test_split(X, y_food_service, test_size=0.2, random_state=42)

    # Linear Regression Models for each sector
    model_household = LinearRegression()
    model_retail = LinearRegression()
    model_food_service = LinearRegression()
    
    model_household.fit(X_train_h, y_train_h)
    model_retail.fit(X_train_r, y_train_r)
    model_food_service.fit(X_train_f, y_train_f)

    # Evaluate models
    mse_h = mean_squared_error(y_test_h, model_household.predict(X_test_h))
    mse_r = mean_squared_error(y_test_r, model_retail.predict(X_test_r))
    mse_f = mean_squared_error(y_test_f, model_food_service.predict(X_test_f))
    st.write(f"Household Model MSE: {mse_h}")
    st.write(f"Retail Model MSE: {mse_r}")
    st.write(f"Food Service Model MSE: {mse_f}")

    # Prediction Form
    st.subheader("Predict Waste by Region")
    region = st.selectbox("Select Region", options=unique_regions)
    if st.button("Predict"):
        # Create input vector for the selected region
        input_data = pd.get_dummies(pd.DataFrame({'Region': [region]}), columns=['Region']).reindex(columns=X.columns, fill_value=0)
        pred_h = model_household.predict(input_data)[0]
        pred_r = model_retail.predict(input_data)[0]
        pred_f = model_food_service.predict(input_data)[0]
        
        st.write(f"Predicted Household Waste (kg/capita/year): {pred_h}")
        st.write(f"Predicted Retail Waste (kg/capita/year): {pred_r}")
        st.write(f"Predicted Food Service Waste (kg/capita/year): {pred_f}")

if __name__ == '__main__':
    run()
