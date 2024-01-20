import streamlit as st
from langchain.llms import OpenAI

st.title('🤖🧠')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key='$OPENAI_API_KEY')
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Ask ChatGPT anything...')
  submitted = st.form_submit_button('Submit')