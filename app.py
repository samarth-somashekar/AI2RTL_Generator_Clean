import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load your OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_verilog(description):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Verilog engineer. Generate synthesizable Verilog code for user's functional description."},
                {"role": "user", "content": description}
            ],
            temperature=0.2,
            max_tokens=1000
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

st.title("🧠 AI2RTL - Verilog Generator")

desc = st.text_area("📝 Describe your logic circuit:", "4-bit synchronous up counter with async reset")

if st.button("⚙️ Generate Verilog"):
    if desc.strip():
        result = generate_verilog(desc)
        st.code(result, language='verilog')
    else:
        st.warning("Please enter a valid description.")
