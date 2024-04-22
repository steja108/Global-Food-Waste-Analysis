import streamlit as st

# Define the main function to handle multipage setup
def main():
    st.set_page_config(page_title="Global Food Waste App", layout="wide")
    
    # Define pages
    pages = {
        "Food Waste Analysis": food_waste_analysis,
        "Reduction Simulator": reduction_simulator,
        "Predictive Modeling": predictive_modeling
    }

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", list(pages.keys()))

    # Display the selected page with the session state as argument
    pages[page]()

def food_waste_analysis():
    import food_waste_analysis
    food_waste_analysis.run()

def reduction_simulator():
    import reduction_simulator
    reduction_simulator.run()

def predictive_modeling():
    import predictive_modeling
    predictive_modeling.run()

if __name__ == "__main__":
    main()
