import streamlit as st
import json
import pandas as pd
import numpy as np
import time

st.title("S.B.T.M")
st.caption("Secure* Berntsen Transfer Manager")
st.write("#\n#\n#\n#")

with open('data.json','r') as f:
    global users
    data = json.load(f)
    #data['users']
currUser = st.sidebar.selectbox("users", (data['users']))
col1, col2, col3 = st.columns(3)
col1.metric('ronan', str(data['users']['ronan']['money']) + "M€")
col2.metric('max', str(data['users']['max']['money']) + "M€")
col3.metric('lara', str(data['users']['lara']['money']) + "M€")

addBalance = st.number_input('amount to transfer') * -1
recipient = st.selectbox("recipient", (data['users']))
transfer = st.button('transfer')
if transfer and addBalance <= 0:
    data['users'][currUser]['money'] = data['users'][currUser]['money'] + addBalance
    data['users'][recipient]['money'] = data['users'][recipient]['money'] - addBalance
    st.balloons()

with open('data.json','w') as f:
    json.dump(data, f)
st.write("#\n#\n#\n#\n#\n#\n#")
st.caption("*I lied it isn't secure at all!")

