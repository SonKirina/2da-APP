import base64
from datetime import datetime
import os
import re
import pandas as pd
import streamlit as st

# Configuración de la página en modo ancho
st.set_page_config(
    page_title="Invitación de Boda", page_icon="💍", layout="wide"
)


# Función para cargar imagen en Base64 de forma segura
def get_image_base64(file_path):
  if os.path.exists(file_path):
    with open(file_path, "rb") as f:
      return base64.b64encode(f.read()).decode()
  return None


# Cargar recursos gráficos
fondo_b64 = get_image_base64("Fondo_5_brillo.jpg")
if fondo_b64:
  background_style = f"""
        background-image: linear-gradient(rgba(242, 241, 237, 0.95), rgba(242, 241, 237, 0.95)), url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover;
        background-position: center;
    """
else:
  background_style = "background-color: #f2f1ed;"

foto_1_b64 = get_image_base64("Foto_1.jpg")
foto_2_b64 = get_image_base64("Foto_2.jpg")
foto_3_b64 = get_image_base64("Foto_3.jpg")

# CSS Global para convertir todo el contenedor principal en la tarjeta de invitación unificada
st.markdown(
    f"""
    <style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    .stApp {{
        background-color: #2b2b2b;
    }}
    
    .block-container {{
        {background_style}
        max-width: 420px !important;
        margin: 30px auto !important;
        padding: 30px 20px !important;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        font-family: 'Times New Roman', serif;
        color: #333333 !important;
    }}

    /* Estilos de tipografía y elementos dentro de la tarjeta */
    .inv-header-year {{
        font-size: 24px;
        letter-spacing: 3px;
        font-weight: bold;
        color: #2c2c2c;
        text-align: center;
    }}
    .inv-header-title {{
        font-style: italic;
        font-size: 26px;
        margin-top: -3px;
        color: #555;
        text-align: center;
    }}
    .inv-names {{
        font-family: 'Brush Script MT', cursive, serif;
        font-size: 38px;
        color: #2c2c2c;
        margin: 10px 0;
        text-align: center;
    }}
    .inv-message {{
        font-size: 11px;
        line-height: 1.4;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #555555;
        margin-bottom: 15px;
        text-align: center;
        padding: 0 5px;
    }}
    .date-section {{
        margin: 12px 0;
        border-top: 1px solid #dcd1c0;
        border-bottom: 1px solid #dcd1c0;
        padding: 10px 0;
        text-align: center;
    }}
    .date-main {{
        font-style: italic;
        font-size: 18px;
        color: #2c2c2c;
    }}
    .date-day {{
        font-size: 30px;
        font-weight: bold;
        color: #2c2c2c;
        line-height: 1.1;
    }}
    .date-month {{
        font-size: 16px;
        letter-spacing: 2px;
        font-weight: bold;
        text-transform: uppercase;
        color: #2c2c2c;
    }}
    .event-details {{
        font-size: 12px;
        color: #555;
        margin: 8px 0;
        line-height: 1.4;
        text-align: center;
    }}
    .section-title {{
        font-weight: bold;
        letter-spacing: 2px;
        margin: 20px 0 5px 0;
        font-size: 13px;
        color: #2c2c2c;
        border-top: 1px solid #dcd1c0;
        padding-top: 15px;
        text-align: center;
    }}
    .link-btn {{
        display: inline-block;
        background-color: #554d45;
        color: white !important;
        padding: 6px 15px;
        text-decoration: none;
        border-radius: 3px;
        font-size: 11px;
        letter-spacing: 1px;
        margin-top: 6px;
        font-family: sans-serif;
        font-weight: bold;
    }}
    .link-btn:hover {{
        background-color: #3b352f;
    }}
    .divider {{
        text-align: center;
        color: #dcd1c0;
        font-size: 20px;
        margin: 25px 0;
    }}
    
    /* Adaptar etiquetas de Streamlit para que sean legibles en la tarjeta */
    .stTextInput label, .stNumberInput label, .stRadio label {{
        color: #2c2c2c !important;
        font-family: 'Times New Roman', serif;
        font-weight: bold;
    }}
    
    /* Estilizar botón de envío */
    .stButton button {{
        background-color: #554d45 !important;
        color: white !important;
        font-family: 'Times New Roman', serif;
        border-radius: 4px;
        border: none;
        width: 100%;
    }}
    .stButton button:hover {{
        background-color: #3b352f !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- CONTENIDO DE LA INVITACIÓN ---
st.markdown('<div class="inv-header-year">2026</div>', unsafe_allow_html=True)
st.markdown('<div class="inv-header-title">Wedding</div>', unsafe_allow_html=True)

if foto_1_b64:
  st.image(f"data:image/jpeg;base64,{foto_1_b64}", use_container_width=True)

st.markdown(
    '<div class="inv-names">Carolina & Carlos</div>', unsafe_allow_html=True
)

st.markdown(
    """
    <div class="inv-message">
        Con amor y con la presencia de Dios entre nosotros, esperamos que este momento sea inolvidable.<br>
        Tenemos el honor de invitarlos a celebrar nuestra unión matrimonial.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="date-section">
        <div style="font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: #666;">Los esperamos el día</div>
        <div class="date-main">Sábado</div>
        <div class="date-day">21</div>
        <div style="font-size: 10px; font-style: italic;">de</div>
        <div class="date-month">Noviembre</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- NUEVAS SECCIONES: MISA, FIESTA Y MESA DE REGALOS ---
st.markdown(
    """
    <div class="section-title">⛪ MISA</div>
    <div class="event-details">
        <b>Sábado 21 de Noviembre | 18:00 hrs</b><br>
        Parroquia Santiago Apóstol, Pueblo Puc.<br>
        <a href="https://maps.google.com" target="_blank" class="link-btn">VER UBICACIÓN</a>
    </div>

    <div class="section-title">🥂 FIESTA</div>
    <div class="event-details">
        <b>Sábado 21 de Noviembre | 20:00 hrs</b><br>
        Salón Yec<br>
        <a href="https://maps.google.com" target="_blank" class="link-btn">VER UBICACIÓN</a>
    </div>

    <div class="section-title">🎁 MESA DE REGALOS</div>
    <div class="event-details">
        Su presencia es nuestro mejor regalo, pero si desean tener un detalle con nosotros, pueden consultar nuestra mesa de regalos.<br>
        <a href="https://www.liverpool.com.mx" target="_blank" class="link-btn">VER MESA DE REGALOS</a>
    </div>

    <div class="section-title">VESTIMENTA</div>
    <div style="font-style: italic; font-size: 12px; margin-bottom: 5px; text-align: center;">Formal</div>
    """,
    unsafe_allow_html=True,
)

# --- SECCIÓN NUESTRA HISTORIA ---
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #2c2c2c; font-family: Times New Roman, serif; font-size: 14px; letter-spacing: 2px; font-weight: bold;'>NUESTRA HISTORIA</h3>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #555; font-style: italic; font-size: 12px; margin-bottom: 15px;'>Cada momento juntos nos ha traído hasta aquí...</p>",
    unsafe_allow_html=True,
)

if foto_2_b64:
  st.image(f"data:image/jpeg;base64,{foto_2_b64}", use_container_width=True)

if foto_3_b64:
  st.image(f"data:image/jpeg;base64,{foto_3_b64}", use_container_width=True)

# --- SECCIÓN DE CONFIRMACIÓN DE ASISTENCIA (AL FINAL) ---
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #2c2c2c; font-family: Times New Roman, serif; font-size: 14px; letter-spacing: 2px; font-weight: bold;'>💌 CONFIRMACIÓN DE ASISTENCIA</h3>",
    unsafe_allow_html=True,
)

with st.container():
  nombre = st.text_input("Nombre completo:")

  telefono = st.text_input(
      "Teléfono celular (10 dígitos):",
      max_chars=10,
      placeholder="Ej. 6671234567",
  )

  acompanantes = st.number_input(
      "Número de acompañantes adicionales:",
      min_value=0,
      max_value=5,
      step=1,
      value=0,
  )

  nombres_acompanantes = []
  if acompanantes > 0:
    st.markdown(
        "<p style='color: #2c2c2c !important; font-weight: bold; margin-top: 15px; margin-bottom: 5px; font-family: Times New Roman, serif;'>Nombres de tus acompañantes:</p>",
        unsafe_allow_html=True,
    )
    for i in range(int(acompanantes)):
      nombre_acomp = st.text_input(
          f"Nombre completo del acompañante {i+1}:", key=f"acomp_{i}"
      )
      nombres_acompanantes.append(nombre_acomp)

  asistencia = st.radio(
      "¿Nos acompañarás?",
      [
          "Sí, ahí estaré con mucho gusto 🥂",
          "Lamentablemente no podré asistir ❤️",
      ],
  )

  restricciones = st.text_input("Alergias o restricciones alimentarias:")

  enviar = st.button("Enviar Confirmación ✨", use_container_width=True)

  if enviar:
    nombre_clean = nombre.strip()
    telefono_clean = re.sub(r"\D", "", telefono.strip())
    lista_nombres_acomp = [
        n.strip() for n in nombres_acompanantes if n.strip() != ""
    ]

    if not nombre_clean:
      st.error(
          "Por favor, ingresa tu nombre completo antes de enviar la confirmación."
      )
    elif len(telefono_clean) != 10:
