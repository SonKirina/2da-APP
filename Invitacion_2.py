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
    .block-container {
        padding: 0px !important;
        max-width: 100% !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Función para cargar imagen en Base64 de forma segura
def get_image_base64(file_path):
  if os.path.exists(file_path):
    with open(file_path, "rb") as f:
      return base64.b64encode(f.read()).decode()
  return None


# 1. Cargar fondo
fondo_b64 = get_image_base64("Fondo_5_brillo.jpg")
if fondo_b64:
  background_style = f"""
        background-image: linear-gradient(rgba(242, 241, 237, 0.92), rgba(242, 241, 237, 0.92)), url("data:image/jpeg;base64,{fondo_b64}");
        background-size: cover;
        background-position: center;
    """
else:
  background_style = "background-color: #f2f1ed;"

# 2. Cargar las fotos desde el repositorio
foto_1_b64 = get_image_base64("Foto_1.jpg")
foto_1_src = (
    f"data:image/jpeg;base64,{foto_1_b64}"
    if foto_1_b64
    else "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&q=80&w=600"
)

foto_2_b64 = get_image_base64("Foto_2.jpg")
foto_2_src = f"data:image/jpeg;base64,{foto_2_b64}" if foto_2_b64 else ""

foto_3_b64 = get_image_base64("Foto_3.jpg")
foto_3_src = f"data:image/jpeg;base64,{foto_3_b64}" if foto_3_b64 else ""

# HTML y CSS de la invitación con la sección "Nuestra Historia"
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    body {{
        margin: 0;
        padding: 0;
        background-color: #2b2b2b;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    }}
    .invitation-container {{
        width: 100%;
        max-width: 380px;
        height: 100vh;
        max-height: 850px;
        {background_style}
        padding: 25px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        font-family: 'Times New Roman', serif;
        color: #333333;
        text-align: center;
        box-sizing: border-box;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
    }}
    .invitation-container::-webkit-scrollbar {{
        display: none;
    }}
    .header-year {{
        font-size: 24px;
        letter-spacing: 3px;
        font-weight: bold;
        color: #2c2c2c;
    }}
    .header-title {{
        font-style: italic;
        font-size: 26px;
        margin-top: -3px;
        color: #555;
    }}
    .photo-frame {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 4px;
        margin: 10px 0;
    }}
    .names {{
        font-family: 'Brush Script MT', cursive, serif;
        font-size: 36px;
        color: #2c2c2c;
        margin: 5px 0;
    }}
    .message {{
        font-size: 10px;
        line-height: 1.4;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #555555;
        margin-bottom: 10px;
        padding: 0 5px;
    }}
    .date-section {{
        margin: 8px 0;
        border-top: 1px solid #dcd1c0;
        border-bottom: 1px solid #dcd1c0;
        padding: 8px 0;
    }}
    .date-main {{
        font-style: italic;
        font-size: 18px;
        color: #2c2c2c;
    }}
    .date-day {{
        font-size: 28px;
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
        font-size: 11px;
        color: #555;
        margin: 8px 0;
        line-height: 1.3;
    }}
    .section-title {{
        font-weight: bold;
        letter-spacing: 2px;
        margin: 15px 0 5px 0;
        font-size: 12px;
        color: #2c2c2c;
        border-top: 1px solid #dcd1c0;
        padding-top: 12px;
    }}
    .btn-rsvp {{
        display: inline-block;
        background-color: #554d45;
        color: white !important;
        padding: 7px 20px;
        text-decoration: none;
        border-radius: 3px;
        font-size: 11px;
        letter-spacing: 1px;
        margin: 6px 0;
        font-family: sans-serif;
        font-weight: bold;
    }}
    .btn-rsvp:hover {{
        background-color: #3b352f;
    }}
    .story-photo {{
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 4px;
        margin: 8px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }}
    .story-text {{
        font-size: 11px;
        font-style: italic;
        color: #555;
        margin-bottom: 8px;
    }}
</style>
</head>
<body>
    <div class="invitation-container">
        <div>
            <div class="header-year">2026</div>
            <div class="header-title">Wedding</div>
        </div>
        
        <img src="{foto_1_src}" class="photo-frame" alt="Boda">
        
        <div class="names">Carolina & Carlos</div>
        
        <div class="message">
            Con amor y con la presencia de Dios entre nosotros, esperamos que este momento sea inolvidable.<br>
            Tenemos el honor de invitarlos a celebrar nuestra unión matrimonial.
        </div>
        
        <div class="date-section">
            <div style="font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: #666;">Los esperamos el día</div>
            <div class="date-main">Sábado</div>
            <div class="date-day">21</div>
            <div style="font-size: 10px; font-style: italic;">de</div>
            <div class="date-month">Noviembre</div>
        </div>
        
        <div class="event-details">
            <b>MISA INICIA A LAS 18:00 HORAS</b><br>
            Parroquia Santiago Apóstol, Pueblo Puc.
        </div>
        
        <div class="event-details">
            <b>RECEPCIÓN 20:00 HORAS</b><br>
            Salón Yec
        </div>
        
        <div>
            <div class="section-title">VESTIMENTA</div>
            <div style="font-style: italic; font-size: 12px; margin-bottom: 5px;">Formal</div>
            
            <div style="font-size: 10px; letter-spacing: 1px; text-transform: uppercase; margin-top: 10px;">Confirma tu asistencia</div>
            <div style="font-size: 8px; color: #777; margin-bottom: 4px;">POR FAVOR, CONFÍRNANOS VÍA WHATSAPP</div>
            
            <a href="https://wa.me/5216670000000?text=¡Hola!%20Confirmo%20mi%20asistencia%20a%20su%20boda." target="_blank" class="btn-rsvp">CONFIRMA AQUÍ</a>
        </div>

        <!-- SECCIÓN NUESTRA HISTORIA -->
        <div>
            <div class="section-title">NUESTRA HISTORIA</div>
            <div class="story-text">Cada momento juntos nos ha traído hasta aquí...</div>
            
            {"<img src='" + foto_2_src + "' class='story-photo' alt='Nuestra Historia'>" if foto_2_b64 else ""}
            {"<img src='" + foto_3_src + "' class='story-photo' alt='Nuestra Historia'>" if foto_3_b64 else ""}
            
            <div style="font-family: 'Brush Script MT', cursive; font-size: 18px; margin: 15px 0 5px 0; color: #4a4a4a;">
                ¡Gracias por acompañarnos!
            </div>
        </div>
    </div>
</body>
</html>
"""

components.html(html_content, height=850, scrolling=False)
