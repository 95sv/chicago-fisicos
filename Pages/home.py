import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
from streamlit_option_menu import option_menu
import intro,cinematica,dinamica

# Correr aplicacion en terminal: python -m streamlit run ..../home.py


with st.sidebar:
    app = option_menu(
        menu_title='Proyecto',
        options=['Intro', 'Cinematica', 'Dinamica'],
        icons=['house', 'c-circle-fill', 'graph-up'],
        menu_icon='filter-square',
        default_index=0,
        styles={
            "container": {"padding": "3!important", "background-color": "black"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

if app == "Intro":
    intro.app()
elif app == "Cinematica":
    cinematica.app()
elif app == "Dinamica":
    dinamica.app()

