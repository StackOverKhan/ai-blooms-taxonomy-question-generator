import os
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyBQXjsClH8Dq4AwXq-79kNOQEP3QMaUKKY")

model = genai.GenerativeModel("gemini-2.5-flash-lite")


st.title("AI-Powered Bloom’s Taxonomy Question Generator")

subject = st.text_input("Enter Subject")
topic = st.text_input("Enter Topic")

bloom_level = st.selectbox(
    "Select Bloom’s Taxonomy Level",
    ["Remember", "Understand", "Apply", "Analyze"]
)

if st.button("Generate Questions"):
    if subject and topic:
        prompt = f"""
        Generate 5 exam questions on the topic '{topic}'
        from the subject '{subject}'
        at the '{bloom_level}' level of Bloom’s Taxonomy.
        """

        response = model.generate_content(prompt)
        st.subheader("Generated Questions")
        st.write(response.text)
    else:
        st.warning("Please enter subject and topic.")
