# Global-Food-Waste-Analysis
## Overview
The Global Food Waste Analysis app is a sophisticated tool designed to model and predict food waste across different sectors and regions using machine learning techniques. The application allows users to predict waste amounts in household, retail, and food service sectors based on regional data. It provides insights through interactive visualizations and predictive modeling, helping users understand and strategize waste reduction efforts effectively.

The app utilizes data from the dataset [Food Waste](https://www.kaggle.com/datasets/joebeachcapital/food-waste). Note that this dataset may not be reliable as this project was developed for educational purposes in the field of machine learning only and not for professional use.

A live version of the application can be accessed on [Streamlit Community Cloud](https://ljvu4tlka5suzndcmuqy4r.streamlit.app/).

## Installation
To run the Global Food Waste Analysis app locally, you must have Python 3.6 or higher installed on your machine. After setting up Python, install the required libraries using the following command:

~~~
pip install -r requirements.txt
~~~

This command will install all necessary dependencies, including Pandas, Scikit-Learn, and Streamlit.

## Usage

To start the application, execute the following command in your terminal:

~~~
streamlit run app.py
~~~

This command launches the app in your default web browser. The app interface allows you to select a region and predict the food waste in different sectors. You can explore the impacts of various factors on food waste through the app's interactive features. Predictions and evaluations of model accuracy (using metrics like MSE) are displayed, providing valuable insights into the effectiveness of different waste management strategies.

