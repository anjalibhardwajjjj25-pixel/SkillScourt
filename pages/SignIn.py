import streamlit as st
import pymongo
conn=pymongo.MongoClient("mongodb+srv://anjalibhardwajjjj25_db_user:RGeVqX8ngrKphiH1@cluster0.uem1qrf.mongodb.net/?appName=Cluster0")
    
mydb=conn["iter"]
table=mydb["user_info"]
st.title("⚕️Health Prediction Applications")
t1=st.text_input("USER NAME")
t2=st.text_input("PASSWORD")
if st.button("SIGN IN"):
       res=table.find({"user_name":t1,"password":t2})
       st.write(res)
       v=0
       for i in res:
              v=v+1
              st.session_state["user"]=i['user_name']
              st.session_state["password"]=i['password']
              st.switch_page("pages/profile.py")
              if v==0:
                     st.error("INVALID LOGIN")
       

