import streamlit as st
import pymongo
if st.session_state.get("user", False):
    st.write("You are safely inside the app!")
else:
       st.error("First Login !!!")
       st.stop()
p1=st.session_state['user']
p2=st.session_state['password']
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.9.2")
mydb=conn["iter"]
table=mydb["user_info"]
st.success(f"Welcome:{st.session_state['user']}")
st.title("⚕️Health Prediction Applications")


c1,c2,c3,c4=st.columns(4)
@st.dialog("Edit Profile")
def edit():
    res=table.find({"user_name":p1,"password":p2})
    for i in res:
        t1=st.text_input("USERNAME",value=i['user_name'])
        t2=st.text_input("PASSWORD",value=i['password'])
        t3=st.text_input("EMAIL ID",value=i['email'])
        t4=st.text_input("MOBILE NUMBER",value=i['mobile'])
        t5=st.text_input("ADDRESS",value=i['address'])
        t6=st.text_input("GENDER",value=i['gender'])
        t7=st.text_input("AGE",value=i['age'])
        t8=st.text_input("BLOOD GROUP",value=i['blood group'])
        if st.button("EDIT",key="b1"):
            pass
    
    
if c1.button("PROFILE",use_container_width=True):
    
    res=table.find({"user_name":p1,"password":p2})
    for i in res:
        st.success(f"user_name:{i['user_name']}")
        st.success(f"password:{i['password']}")
        st.success(f"Email:{i['email']}")
        st.success(f"Mobile:{i['mobile']}")
        st.success(f"Address:{i['address']}")
        st.success(f"Gender:{i['gender']}")
        st.success(f"Age:{i['age']}")
        st.success(f"Blood Group:{i['blood group']}")
         
if c2.button("EDIT",use_container_width=True):
    edit()
c3.button("AI-AGENT",use_container_width=True)
if c4.button("LOGOUT",use_container_width=True):
    del st.session_state['user']
    st.switch_page("index.py")
