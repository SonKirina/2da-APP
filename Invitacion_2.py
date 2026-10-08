import base64
import re
from datetime import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Boda de Ismael & Elizabeth 💍",
    page_icon="💍",
    layout="centered",
)


def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"
    except FileNotFoundError:
        return ""


fondo_b64 = get_image_base64("Fondo_5_brillo.jpg")

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Cormorant+Garamond:wght@400;600;700&family=Montserrat:wght@300;400;500;600&display=swap');

    /* Fondo de pantalla difuminado */
    [data-testid="stAppViewContainer"] {{
        background-image: url({fondo_b64});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}

    /* --- LIENZO CONTINUO ESTILO PAPEL / INVITACIÓN --- */
    .paper-canvas {{
        max-width: 420px !important;
        margin: 20px auto !important;
        background: #F4F1EA !important; /* Papel crema elegante */
        padding: 40px 25px !important;
        box-shadow: 0px 20px 40px rgba(0, 0, 0, 0.5) !important;
        text-align: center !important;
        color: #2C2A29 !important;
    }}

    /* Tipografías estilo la imagen */
    .year-header {{
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        color: #2C2A29 !important;
        line-height: 0.8 !important;
        margin-bottom: -15px !important;
    }}

    .script-wedding {{
        font-family: 'Great Vibes', cursive !important;
        font-size: 3.8rem !important;
        color: #2C2A29 !important;
        margin-bottom: 20px !important;
    }}

    .names-script {{
        font-family: 'Great Vibes', cursive !important;
        font-size: 3.5rem !important;
        color: #2C2A29 !important;
        margin: 20px 0 10px 0 !important;
    }}

    .sub-text {{
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.75rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: #5A5652 !important;
        line-height: 1.6 !important;
    }}

    .big-date {{
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 3.8rem !important;
        font-weight: 700 !important;
        line-height: 1 !important;
        margin: 5px 0 !important;
    }}

    .month-text {{
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.8rem !important;
        letter-spacing: 4px !important;
        font-weight: 700 !important;
    }}

    /* Adaptación limpia de los inputs para no romper el papel */
    div[data-testid="stVerticalBlock"] > div:has(input) {{
        background: transparent !important;
        padding: 0 !important;
        border: none !important;
    }}

    label, .stWidgetLabel p, [data-testid="stRadioButton"] p {{
        color: #2C2A29 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.85rem !important;
    }}

    .stButton>button {{
        background: #2C2A29 !important;
        color: #F4F1EA !important;
        border-radius: 4px !important;
        font-weight: 500 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }}

    .separator {{
        border-bottom: 1px solid #D5CFC4;
        margin: 30px 0;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# ==================== LIENZO ESTILO INVITACIÓN ====================
st.markdown('<div class="paper-canvas">', unsafe_allow_html=True)

# 1. Encabezado Año + Script
st.markdown(
    '<div class="year-header">2026</div><div class="script-wedding">Wedding</div>',
    unsafe_allow_html=True,
)

# 2. Foto de portada rectangular centrada
try:
    st.image("Foto_1.jpg", use_container_width=True)
except Exception:
    st.markdown("*(Foto de la pareja aquí)*")

# 3. Nombres de los Novios
st.markdown(
    '<div class="names-script">Ismael & Elizabeth</div>',
    unsafe_allow_html=True,
)

# 4. Mensaje introductorio
st.markdown(
    """
<p class="sub-text">
    Con amor y con la bendición de Dios,<br>
    tenemos el honor de invitarlos a celebrar nuestra unión matrimonial.
</p>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# 5. Fecha grande (Estilo "Sábado 18 de Diciembre")
st.markdown(
    """
<div class="sub-text">Los esperamos el día</div>
<div class="names-script" style="font-size: 2.8rem !important; margin: 5px 0 !important;">Viernes</div>
<div class="big-date">18</div>
<div class="month-text">DICIEMBRE</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# 6. Ceremonia Religiosa
st.markdown(
    """
<div style="font-size: 2rem;">⛪</div>
<div class="sub-text" style="font-weight: 600;">Ceremonia Religiosa</div>
<p class="sub-text" style="margin-top: 5px;">
    <b>14:00 HRS</b><br>
    Parroquia San Gabriel<br>
    Culiacán, Sinaloa
</p>
<a href="https://maps.google.com" target="_blank" class="sub-text" style="text-decoration: underline;">Ver Ubicación</a>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# 7. Recepción / Fiesta
st.markdown(
    """
<div style="font-size: 2rem;">🥂</div>
<div class="sub-text" style="font-weight: 600;">Recepción</div>
<p class="sub-text" style="margin-top: 5px;">
    <b>19:00 HRS</b><br>
    Salón Metropolitan: Piso 1<br>
    Culiacán, Sinaloa
</p>
<a href="https://maps.google.com" target="_blank" class="sub-text" style="text-decoration: underline;">Ver Ubicación</a>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# 8. Mesa de Regalos
st.markdown(
    """
<div class="sub-text" style="font-weight: 600; font-size: 0.9rem;">Mesa de Regalos</div>
<p class="sub-text" style="margin-top: 8px;">
    Tu presencia es nuestro mejor regalo.<br>
    • Liverpool: <a href="https://mesaderegalos.liverpool.com.mx/milistaderegalos/60030339" target="_blank" style="text-decoration: underline;">Ver Mesa</a><br>
    • Contaremos con lluvia de sobres.
</p>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# 9. Formulario RSVP dentro del diseño del pliego
st.markdown(
    '<div class="names-script" style="font-size: 2.5rem !important;">Confirma tu asistencia</div>',
    unsafe_allow_html=True,
)

nombre = st.text_input("Nombre completo:")
telefono = st.text_input("Teléfono (10 dígitos):", max_chars=10)
acompanantes = st.number_input(
    "Acompañantes adicionales:", min_value=0, max_value=5, value=0
)

nombres_acompanantes = []
if acompanantes > 0:
    for i in range(int(acompanantes)):
        nombre_acomp = st.text_input(
            f"Acompañante {i+1}:", key=f"acomp_papel_{i}"
        )
        nombres_acompanantes.append(nombre_acomp)

asistencia = st.radio(
    "¿Asistirás?",
    ["Sí, ahí estaré 🥂", "No podré asistir ❤️"],
)

restricciones = st.text_input("Alergias o restricciones:")
enviar = st.button("Enviar Confirmación ✨", use_container_
