from groq import Groq
import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(
  page_title = "Retirement Lifestyle Investigator",
  layout = "wide",
  initial_sidebar_state = "auto"
)
st.write("Estimate the amount of funds you would need in retirement based on the lifestyle you want to live. Results may not always be accurate as they are AI-generated and are assumptions.")
prompt = st.text_input("Describe your lifestyle")
api = st.secrets['api']
client = Groq(api_key = api)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are to gauge how much money would it cost (monthly and annually), to live 20, 40, and 60 years from now in Thai Baht. Living expenses and assumptions should be based on the lifestyle inputted by the user, the lifestyle is as follows" + prompt + "If any part of the inputted message is in Thai, respond in Thai.",
        }
    ],
    model="llama-3.3-70b-versatile",
)
result = response.choices[0].message.content
st.write(result)
