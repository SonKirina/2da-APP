import base64
import os
import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página en modo ancho
st.set_page_config(
    page_title="Invitación de Boda", page_icon="💍", layout="wide"
)

# Ocultar elementos de la interfaz de Streamlit y establecer fondo oscuro global
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #2b2b2b;
    }
    .block
