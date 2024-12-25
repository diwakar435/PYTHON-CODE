import streamlit as st
import os

import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.environ['GEMINI_API_KEY'] = "AIzaSyABeAiyxRflEJhQml76hX0v_PVrgyIMKFQ"

import google.generativeai as genai
genai.configure(api_key = os.environ['GEMINI_API_KEY'])

def get_gemini_response(question):
  model = genai.GenerativeModel('gemini-2.0-flash-exp')
  response = model.generate_content(question)
  return response.text

st.set_page_config(page_title='GEMINI LLM APP')

st.header('Diwakar AI BOT application')

input = st.text_input('input: ',key = 'input')

submit = st.button('click me to generate response')

if submit:
  response = get_gemini_response(input)
  st.subheader('The Response is')
  st.write(response)