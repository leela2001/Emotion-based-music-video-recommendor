import streamlit as st

from streamlit_option_menu import option_menu

import video, music, home, contact, account, about

st.set_page_config(
    page_title= "Main Page",
    page_icon= "🤡️️",
    layout="wide",
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title,function):
        self.apps.append({
            "title":title,
            "function":function
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Music/Video ',
                options=['Home', 'Account', 'Music', 'Video', 'Contact','About'],
                icons=['house-fill', 'person-circle', 'music-note-beamed', 'camera-reels', 'person-video2','chat-left-text'],
                menu_icon='film',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "purple"}, }

            )

        if app == "Home":
            home.app()
        if app == "Account":
            account.app()
        if app == "Music":
            music.app()
        if app == 'Video':
            video.app()
        if app == 'Contact':
            contact.app()
        if app == 'About':
            about.app()

    run()
