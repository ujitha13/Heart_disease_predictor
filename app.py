import pickle
import pandas as pd
import streamlit as st


#page setup
st.set_page_config(page_icon="💓",page_title="Heart Disease Predictor",layout="wide")

with st.sidebar:
    st.title("Heart Disease Predictor")
    st.image("https://images.vexels.com/media/users/3/136170/isolated/preview/1a0fc726567fe21282676126358b795d-heart-disease-logo.png")



#load the dataset
df = pd.read_csv("cleaned_data.csv")
#load the model
with open("Log_model.pkl","rb") as file:
    model = pickle.load(file)

#user input
with st.container(border=True):
    col1,col2 = st.columns(2)
    with col1:
        age = st.number_input("Age: ",min_value=1,max_value=100,step=5)
        gender = st.radio("Gender: ",options=["Male","Female"],horizontal=True)
        gender = 1 if gender=="Male" else 0
        d = {"Typical angina":0,"Atypical angina":1,"non-anginal pain":2,"Asymptomatic":3}
        chest_pain_type = st.selectbox("Chest pain type: ",options=d.keys())
        chest_pain_type = d[chest_pain_type]
        resting_bp  =st.number_input("Resting BP: ",min_value=50,max_value=250,step=5)
        cholestrol  =st.number_input("Cholestrol: ",min_value=50,max_value=600,step=5)
        fbs = st.radio("Fasting Blood Sugar: ",options=["Yes","No"],horizontal=True)
        fbs  =1 if fbs=="Yes" else 0

    with col2:
        d = {"Normal":0,"Having ST-T wave abnormality":1,"Left ventricular hypertrophy":2}
        restecg = st.selectbox("Resting ECG: ",options=d.keys())
        restecg = d[restecg]
        max_heart  =st.number_input("Max Heart Rate: ",min_value=50,max_value=250,step=5)
        exang = st.radio("Exer induced angina: ",options=["Yes","No"],horizontal=True)
        exang  =1 if exang=="Yes" else 0
        oldpeak  =st.number_input("Oldpeak ",min_value=0.0,max_value=10.0,step=1.0)
        d = {"upsloping":0,"flat":1,"downsloping":2}
        slope = st.selectbox("Slope: ",options=d.keys())
        slope = d[slope]
        num_vessels = st.selectbox("Num of Major Vessels: ",options=[0,1,2,3,4])
        d = { "normal": 1 , "fixed defect" :2 , "reversable defect":3}
        thal = st.selectbox("Thal:  ",options=d.keys())
        thal = d[thal]
    if st.button("Predict"):
        data = [[age,gender,chest_pain_type,resting_bp,cholestrol,fbs,restecg,max_heart,exang,
                oldpeak,slope,num_vessels,thal]]
        pred = model.predict(data)[0]
        
        if pred==0:
            st.subheader("Low Risk of Heart Disease")
            st.image("images\lowrisk.png",width=150)
        else:
            st.subheader("High Risk of Heart Disease")
            st.image("images\highrisk.png",width=150)