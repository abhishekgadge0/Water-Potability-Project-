import streamlit as st
import pandas as pd
import pickle
from PIL import Image


st.markdown("<h1 style='text-align: center; color: greeen;'>Water Analysis</h1>", unsafe_allow_html=True)
image = Image.open('water.jpg')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.image(image,width=280 )
with col3:
    st.write('')
st.markdown("<h1 style='text-align: centre; color: black; font-size: 25px';>- AI ML</h1>", unsafe_allow_html=True)



st.sidebar.header('User Input Parameters')

 

def user_input_features():
    
    ph = st.sidebar.number_input('ph',min_value=0.00,max_value=14.00,step=0.01)
    Hardness = st.sidebar.number_input('Hardness',min_value=47.43,max_value=323.12,step=0.01)
    Solids = st.sidebar.number_input('Solids',min_value=321.94,max_value=61227.19,step=0.01)
    Chloramines = st.sidebar.number_input('Chloramines',min_value=0.35,max_value=13.12,step=0.01)
    Sulfate = st.sidebar.number_input('Sulfate',min_value=129.00,max_value=481.03,step=0.01)
    Conductivity = st.sidebar.number_input('Conductivity',min_value=181.48,max_value=753.34,step=0.01)
    OC = st.sidebar.number_input("Organic_carbon",min_value=2.20,max_value=28.30,step=0.01)
    Trihalomethanes = st.sidebar.number_input('Trihalomethanes',min_value=0.73,max_value=124.0,step=0.01)
    Turbidity = st.sidebar.number_input('Turbidity',min_value=1.45,max_value=6.73,step=0.1)

   
    
    user_input = {
    'ph': ph,
    'Hardness': Hardness,
    'Solids': Solids,
    'Chloramines': Chloramines,
    'Sulfate': Sulfate,
    'Conductivity': Conductivity,
    'Organic_carbon':OC,
    'Trihalomethanes':Trihalomethanes,
    'Turbidity':Turbidity
                    }
    
    

    features = pd.DataFrame(user_input,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)



with open(file="model.sav",mode="rb") as f1:
    model = pickle.load(f1)
    
    
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

st.subheader('Predicted Result')
st.write('Yes' if prediction_proba[0][1] > 0.5 else 'No')

st.subheader('Prediction Probability')
st.write(prediction[0])

