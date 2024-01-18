
import streamlit as st
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth




























# st.set_page_config(
#     page_title= "Main Page",
#     page_icon= "🤡️️",
#     layout="wide",
# )
def app():
    if st.session_state.signout:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_hello = load_lottieurl("https://lottie.host/39fba1f0-f061-451c-9e3d-292d57298b18/kLKLhwcpbV.json")
        lottie_computer = "https://lottie.host/5fb05a02-20a0-49a4-9eb2-f0be7304af19/83PMREjmXk.json"
        lottie_video ="https://lottie.host/9cd8799b-d59b-4b19-8c56-3de7911d7e4f/zpoUqUxgY4.json"
        lottie_music = "https://lottie.host/4be2ab52-2f5c-4d2c-b9dc-d88be72b1be7/h05rAY72VK.json"
        lottie_tube = "https://lottie.host/7169c575-2f84-4d4f-9113-d00238ccc4fd/ywSpJiO1of.json"
        lottie_face = "https://lottie.host/c77baffc-7d8c-465f-b423-2bdcf50c6703/QmM40lHSNi.json"
        lottie_insta = "https://lottie.host/534755c3-38f1-4fa7-8478-26e3e3445180/hPTNI4ZjFi.json"
        lottie_twit = "https://lottie.host/eeb8a5c9-744a-45bf-ac4c-269276dc6f9c/jWZfFfF2Yj.json"

        with open('home.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        # st.subheader("Hey Guys 👋")
        # st.title("Enjoy free Video & Music")
        # st.write("""
        # This platform created to provide you best
        # Video and Music based on your current mood (Emotion).
        # """)
        # st.write("------")
        #
        # st_lottie(
        #             lottie_hello,
        #             speed=1,
        #             reverse=False,
        #             loop=True,
        #             quality="high",  # medium ; high
        #
        #             height=None,
        #             width=None,
        #             key=None,
        #         )
        # st.write("------")

        st.header("Emotion Based Video and Music Recommendation System")

        st.sidebar.success("Best things for entertainment. 👌")
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.write("Hey Guys 👋")
                st.title("Enjoy free Video & Music")
                st.write("""
                This platform created to provide you best
                Video and Music based on your current mood (Emotion).
                """)
            with col2:
                st_lottie(
                    lottie_hello,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )

        st.write("------")
        st.write("------")
        st.write("------")

        st.write("💡Know More About It")

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("MOTTO")
                st.write(
                    "✨The main motto behind this project is to reduce stress and save time of the people from their hectic schedule. This website provide you Video and Music based on your emotion. To read more about benefit of stress-free life click on read more.")

                st.title("")
            with col2:
                st_lottie(
                    lottie_computer,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )

        ###################################################################

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st_lottie(
                    lottie_video,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )
            with col2:
                st.subheader("Video")
                st.write(
                    "✨You can watch Short Movie/Video based on your emotion. After clicking on get started,show your face on webcame to detect your current emotion, after the detection completed select video to get variety of Video. To read more about benefit of Video click on below button.")

                st.title("")
        #################################################################

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Music")
                st.write(
                    "✨You can listen music based on your emotion. After clicking on Get Started button show your face to webcame to detect your emotion, after detection simply click on music to get music. To read more about benefit of Music click on below button.")

                st.title("")
            with col2:
                st_lottie(
                    lottie_music,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )

        with st.container():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st_lottie(
                    lottie_tube,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )
            with col2:
                st_lottie(
                    lottie_face,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )
            with col3:
                st_lottie(
                    lottie_insta,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )
            with col4:
                st_lottie(
                    lottie_twit,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality="high",  # medium ; high

                    height=None,
                    width=None,
                    key=None,
                )

        # with open('home.css') as f:
        #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

        # home = """
        #
        #
        # """
        # st.markdown(home, unsafe_allow_html=True)
        #
        # def local_css(file_name):
        #     with open(file_name) as f:
        #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        #
        # local_css("home.css")









    else:
        st.warning("Please Login 🥺")
        st.image("static/saddog.png")