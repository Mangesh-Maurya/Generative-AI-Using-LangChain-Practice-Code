from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# model = AzureChatOpenAI()

st.header('Research Tool')

user_input = st.text_input('Enter your prompt')
if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)

    