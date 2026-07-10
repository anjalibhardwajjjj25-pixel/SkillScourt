import streamlit as st
st.title("⚕️Health Prediction Applications")
t1=st.text_input("👤USER NAME")
t2=st.text_input("🔒PASSWORD",type="password")
t3=st.text_input("✉️EMAIL")
t4=st.text_input("📱MOBILE NUMBER")
t5=st.text_area("🏠ADDRESS")
t6=st.selectbox("⚧️GENDER",['M','F'])
t7=st.slider("🧑AGE",1,100)
t8=st.selectbox("🩸BLOOD GROUP",['A+','B-','AB+','AB-','O+'])

if st.button("📝SIGNUP"):
       pass
