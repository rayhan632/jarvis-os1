import streamlit as st
import google.generativeai as genai
from datetime import datetime

# --- আপনার নাম ও পাসওয়ার্ড এখানে লিখুন ---
YOUR_NAME = "Rayhan Ahmed" 
MY_PASSWORD = "Rafan_jarvis_os" 
API_KEY = "AIzaSyAN9Ue7scUU4-C0YRcyDg6CX21I9MN67M8"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title=f"Jarvis OS | by {YOUR_NAME}", page_icon="⚡")

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("⚡ JARVIS OS v3.0")

def save_log(user, query, response):
    with open("logs.txt", "a", encoding="utf-8") as f:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{t}] {user}: {query} | AI: {response[:30]}...\n")

if 'user_name' not in st.session_state:
    u_name = st.text_input("সিস্টেমে প্রবেশের জন্য আপনার নাম লিখুন:")
    if u_name:
        st.session_state.user_name = u_name
        st.rerun()

if 'user_name' in st.session_state:
    st.write(f"অনলাইন বস! কি হুকুম {st.session_state.user_name}?")
    u_input = st.chat_input("কমান্ড দিন...")
    if u_input:
        st.chat_message("user").write(u_input)
        res = model.generate_content(f"Reply in Bengali like Jarvis: {u_input}")
        st.chat_message("assistant").write(res.text)
        save_log(st.session_state.user_name, u_input, res.text)

with st.sidebar:
    st.header("🛡️ Boss Control")
    access = st.text_input("গোপন পাসওয়ার্ড:", type="password")
    if access == MY_PASSWORD:
        st.success(f"স্বাগতম {YOUR_NAME}!")
        if st.button("ভিউ ইউজার লগ"):
            try:
                with open("logs.txt", "r") as f: st.text_area("সার্চ রেকর্ড", value=f.read(), height=300)
            except: st.info("এখনো কোনো রেকর্ড নেই।")

st.markdown(f'<div class="footer">🚀 Developed by {YOUR_NAME} | Jarvis AI</div>', unsafe_allow_html=True)
