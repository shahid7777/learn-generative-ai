# https://docs.streamlit.io/library/api-reference/chat/st.chat_input

import streamlit as st

if prompt := st.chat_input("Say something"):
    st.write(f"User has sent the following prompt: {prompt}")