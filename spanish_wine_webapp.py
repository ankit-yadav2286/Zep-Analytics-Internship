import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')


# loading the saved model
loaded_model = pickle.load(open('C:/Users/ankit/OneDrive/Desktop/streamlit_dashboard/trained_model3.pkl'
                                , 'rb'))

def main():

    # giving a title
    st.title('Spanish Wine Price Prediction')

    # getting the input data from the user
    winery = st.text_input('Name of winery')
    wine = st.text_input('Name of wine')
    year = st.text_input('year in which grape is harvested')
    rating = st.text_input('wine rating')
    num_reviews = st.text_input('no.of wine reviewers')
    region = st.text_input('region of wine')
    type1 = st.text_input('type of wine')
    body = st.text_input('body score')
    acidity = st.text_input('acidity score')



    # creating a button for Prediction

    if st.button('Spanish Wine Result'):
        price_prediction = loaded_model.predict([[winery,wine,year,rating,num_reviews,region,type1,body,acidity]])

        output = round(price_prediction[0],2)
        st.success("Price of Wine is {}".format(output))


if __name__ == '__main__':
    main()


