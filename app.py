import streamlit as st
import openai
from openai import OpenAI

# Add your OpenAI API key
client = OpenAI(
    api_key=st.secrets["openai_api_key"]
)

st.title("Medicare Hospice Compliance GPT")
st.write("Enter your query below to receive compliance guidance.")

user_query = st.text_area("Your Query:")
if st.button("Submit"):
    with ((((st.spinner("Generating response..."))))):
       try:
           response = client.chats.Completion.create(
               model="gpt-3.5-turbo-instruct",
               messages=user_query,
               temperature=1
	   )
           st.success("Response:")
           st.write(response.choices[0].text.strip())
       except Exception as e:
           st.error("An error occurred. Please check your input or try again.")
