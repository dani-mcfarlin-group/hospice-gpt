import streamlit as st
import openai

# Add your OpenAI API key
openai.api_key = "your-api-key"

st.title("Medicare Hospice Compliance GPT")
st.write("Enter your query below to receive compliance guidance.")

user_query = st.text_area("Your Query:")
if st.button("Submit"):
    with ((((st.spinner("Generating response..."))))):
       try:
           response = openai.Completion.create(
               engine="text-davinci-003",
               prompt=user_query,
               max_tokens=200
	            )
           st.success("Response:")
           st.write(response.choices[0].text.strip())
       except Exception as e:
           st.error("An error occurred. Please check your input or try again.")
