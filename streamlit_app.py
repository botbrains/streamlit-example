import streamlit as st
from langchain.llms import OpenAI

st.title('🤖🧠')

def generate_response(input_text):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key='$OPENAI_API_KEY')
        response = llm(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")

with st.form('my_form'):
    text = st.text_area('Enter text:', 'Ask ChatGPT anything...')
    submitted = st.form_submit_button('Submit')

if submitted:
    generate_response(text)