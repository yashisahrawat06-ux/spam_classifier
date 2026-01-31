import streamlit as st
import joblib 
import pandas as pd

model=joblib.load("spam_clf.pkl")
st.set_page_config(layout="wide")

st.sidebar.image("message_protection.jpg")
st.sidebar.title("ℹ️About us")
st.sidebar.text("This project is created as a student initiative to classify messages as Spam or Not Spam. It focuses on practical learning and provides an easy-to-use web interface for message prediction.")
st.sidebar.title("📞Contact Us")
st.sidebar.text("9999999999")

st.markdown("""
      <div style="
            background-color:#1E88E5;
            padding:20px;
            border-radius:12px;
            text-align:center;
            color:white;
            font-size:42px;
            font-weight:700;
            box-shdow: 0px 4px 12px rgba(0,0,0,0.3);
        ">
            Spam Classifier Project
        </div>   
""", unsafe_allow_html=True)

st.text("")
col1,col2=st.columns([2,2],gap="large")
with col1:
    st.markdown("""
    <div style="
        background-color:#f5f6ff;
        padding:2px;
        border-radius:12px;
        text-align:center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        margin-bottom:10px;
    ">
        <h1 style="
            margin:0;
            font-weight:600;
            font-size:34px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            color: transparent;
        ">
            Single Message Prediction
        </h1>
    </div>
    """,unsafe_allow_html=True)
    
    text=st.text_input("Enter Message", key="glass-input", placeholder="Type message here...." )
    
    if st.button("Predict"):
        result=model.predict([text])
        if result=="spam":
            st.error("Spam->Irrelevent ❌")
        else:
            st.success("Ham->Relevent ✔️")

with col2:
    st.markdown("""
    <div style="
        background-color:#f5f6ff;
        padding:1px;
        border-radius:12px;
        text-align:center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
        margin-bottom:8px;
    ">
        <h1 style="
            margin:0;
            font-weight:600;
            font-size:34px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            color: transparent;
        ">
            Bulk Message Prediction
        </h1>
    </div>
    """,unsafe_allow_html=True)
   
    file=st.file_uploader("select file containing bulk msgs",type=['txt','csv'])
    
    if file!=None:
        df=pd.read_csv(file.name,header=None,names=["Msg"])
        place=st.empty()
        place.dataframe(df)
        if st.button("Predict",key="b2"):
            result=model.predict(df.Msg)
            df['result']=model.predict(df.Msg)
            place.dataframe(df)
