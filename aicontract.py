import streamlit as st
import openai

# Set up OpenAI API client
openai.api_key = "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"

# Set up GPT-3 model
model_engine = "text-davinci-002"

def generate_contract(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title("Legal Contract Generator")

# Get input from user
party_a = st.text_input("Party A:")
party_b = st.text_input("Party B:")
party_c = st.text_input("Party C (optional):")
contract_type = st.text_input("Enter contract type:")
description = st.text_area("Enter contract description:")

# Generate contract
prompt = (
    f"Generate a legal contract between {party_a} and {party_b}"
    + (f", with {party_c} as a witness" if party_c else "")
    + f" for a {contract_type} agreement. {description} "
)

contract = generate_contract(prompt)

st.markdown(contract, unsafe_allow_html=True)
