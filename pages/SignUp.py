import streamlit as st
import pymongo
import smtplib

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
    conn=pymongo.MongoClient("mongodb+srv://anjalibhardwajjjj25_db_user:RGeVqX8ngrKphiH1@cluster0.uem1qrf.mongodb.net/?appName=Cluster0")
    mydb=conn["iter"]
    table=mydb["user_info"]
    table.insert_one({"user_name":t1,"password":t2,"email":t3,"mobile":t4,"address":t5,"gender":t6,"age":t7,"blood group":t8})
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("anjalibhardwajjjj25@gmail.com","qbff ogcm tsld kgix")
    server.sendmail("anjalibhardwajjjj25@gmail.com",t3,"Hello! Your signup was successful.")
    server.quit()
    st.write("SUCCESSFULLY SINGUP!")
