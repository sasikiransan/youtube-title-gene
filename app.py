import streamlit as st
from groq_api import generate_metadata

st.set_page_config(page_title="YT Metadata Generator 🎬", layout="centered")
st.title("🎥 YouTube Title & Description Generator")

user_input = st.text_area("📄 Paste your video script or summary here:")

if st.button("✨ Generate"):
    if user_input.strip():
        with st.spinner("Generating metadata using LLaMA 3..."):
            title, description = generate_metadata(user_input)
            st.success("Done! Here's your metadata:")
            st.markdown(f"### 🏷️ Title:\n{title}")
            st.markdown(f"### 📋 Description:\n{description}")
    else:
        st.warning("Please enter some script text.")
