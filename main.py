import streamlit as st
import google.generativeai as genai

# সরাসরি API Key বসান
genai.configure(api_key="আপনার_API_KEY_এখানে_দিন")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 JARVIS AI")

# ইনপুট বক্স
prompt = st.chat_input("কি হুকুম বস?")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
