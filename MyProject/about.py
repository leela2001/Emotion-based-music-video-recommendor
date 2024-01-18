import streamlit as st
import requests

import streamlit as st

def app():
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_hello = load_lottieurl("https://lottie.host/39fba1f0-f061-451c-9e3d-292d57298b18/kLKLhwcpbV.json")
    lottie_computer = "https://lottie.host/5fb05a02-20a0-49a4-9eb2-f0be7304af19/83PMREjmXk.json"
    lottie_video = "https://lottie.host/9cd8799b-d59b-4b19-8c56-3de7911d7e4f/zpoUqUxgY4.json"
    lottie_music = "https://lottie.host/4be2ab52-2f5c-4d2c-b9dc-d88be72b1be7/h05rAY72VK.json"
    lottie_tube = "https://lottie.host/7169c575-2f84-4d4f-9113-d00238ccc4fd/ywSpJiO1of.json"
    lottie_face = "https://lottie.host/c77baffc-7d8c-465f-b423-2bdcf50c6703/QmM40lHSNi.json"
    lottie_insta = "https://lottie.host/534755c3-38f1-4fa7-8478-26e3e3445180/hPTNI4ZjFi.json"
    lottie_twit = "https://lottie.host/eeb8a5c9-744a-45bf-ac4c-269276dc6f9c/jWZfFfF2Yj.json"

    with open('style/about.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("static/pandam.png")
        with col2:
            st.title("About Us")
            st.subheader("Computer Science Department")
            st.write(
                "✨I am a student of Computer Science Department. I can provide a clean code and also make the web application more and more interactive with web animations.")
            st.write("            ")

            st.write("🏡Address      : LNG college, ponneri")
            st.write("📱Phone Number : +91-1234567899")
            st.write("Ⓜ️Email Id     : leela@gmail.com")

    #
    # with st.container():
    #     col1,col2 = st.columns(2)
    #     with col1:
    #         st.write("🏡Address      : LNG college, ponneri")
    #         st.write("📱Phone Number : +91-1234567899")
    #         st.write("Ⓜ️Email Id     :leela@gmail.com")
    #     with col2:
    #         st.write("LNG college, ponneri")
    #         st.write("+91-1234567899")
    #         st.write("leela@gmail.com")
    #

