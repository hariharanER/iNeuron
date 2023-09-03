
import streamlit as st
import pickle
st.title("Air Quality Index Predicter")
d = {'Good':1,'Moderate':2,'Unhealthy':3,'Very Unhealthy':4,'Unhealthy for sensitive groups':5,'Hazardous':6}
v1 = st.slider("Select the Value of Nitrous Di-Oxide:",0,91)
v2 = st.radio("Select the  Nitrous Di-Oxide Category:",list(d.keys())[0:2])
v3 = st.slider("Select the value of Carbon Monoxide:",0,133)
v4 = st.radio("Select the Carbon Monoxide Category:",list(d.keys())[0:2])
v5 = st.slider("Select the value of Ozone:",0,222)
v6 = st.radio("Select the Ozone Category:",list(d.keys())[0:5])

if st.button("Predict"):
    f = open("Model.pkl",'rb')
    model = pickle.load(f)
    predict = model.predict([[v1,d[v2],v3,d[v4],v5,d[v6]]])
    st.success(predict)
    
    if predict <= 50:
        st.success("Good")
    elif predict > 50 and predict <= 99:
        st.success("Moderate")
    elif predict > 99 and predict <= 150:
        st.success("Unhealthy for Sensitive Groups")
    elif predict > 150 and predict <= 200:
        st.success ("Unhealthy")
    elif predict > 300 and predict <= 500:
        st.success("Hazardous")
    else:
        st.success("Very Unhealthy")