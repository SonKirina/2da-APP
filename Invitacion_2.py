import base64
import os
import streamlit as st

# Configuración de la página en modo ancho completo (wide)
st.set_page_config(
    page_title="Invitación de Boda", page_icon="💍", layout="wide"
)

# Estilos CSS globales para eliminar márgenes de Streamlit y forzar pantalla completa
st.markdown(
    """
    <style>
    /* Ocultar elementos de la interfaz de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Eliminar márgenes y padding del contenedor principal de Streamlit */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    /* Fondo general de la aplicación a pantalla completa */
    .stApp {
        background-color: #2b2b2b;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    </style>
""",
    unsafe_allow_html=True,
)


# Función para cargar la imagen de fondo desde el repositorio local de GitHub
def get_image_base64(file_path):
  if os.path.exists(file_path):
    with open(file_path, "rb") as f:
      return base64.b64encode(f.read()).decode()
  return None


fondo_b64 = get_image_base64("Fondo_5_brillo.jpg")

if fondo_b64:
  background_css = f"""
    background-image: linear-gradient(rgba(242, 241, 237, 0.92), rgba(242, 241, 237, 0.92)), url("data:image/jpeg;base64,{fondo_b64}");
    background-size: cover;
    background-position: center;
"""
else:
  background_css = "background-color: #f2f1ed;"

# Estructura HTML y CSS adaptada para ocupar el 100% de la pantalla sin scroll general
invitation_html = f"""
<style>
    .invitation-fullscreen {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        {background_css}
        display: flex;
        justify-content: center;
        align-items: center;
        box-sizing: border-box;
        overflow-y: auto;
        font-family: 'Times New Roman', serif;
        color: #333333;
    }}
    
    .invitation-card {{
        width: 100%;
        max-width: 420px;
        min-height: 100vh;
        background: transparent;
        padding: 30px 20px;
        box-sizing: border-box;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}

    /* Ocultar barra de desplazamiento interna si el contenido es largo en algunos dispositivos */
    .invitation-fullscreen::-webkit-scrollbar {{
        display: none;
    }}

    .header-year {{
        font-size: 26px;
        letter-spacing: 3px;
        font-weight: bold;
        color: #2c2c2c;
    }}
    .header-title {{
        font-style: italic;
        font-size: 28px;
        margin-top: -3px;
        color: #555;
    }}
    .photo-frame {{
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 4px;
        margin: 15px 0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }}
    .names {{
        font-family: 'Brush Script MT', cursive, serif;
        font-size: 40px;
        color: #2c2c2c;
        margin: 10px 0;
    }}
    .message {{
        font-size: 11px;
        line-height: 1.5;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #555555;
        margin-bottom: 20px;
        padding: 0 10px;
    }}
    .date-section {{
        margin: 15px 0;
        border-top: 1px solid #dcd1c0;
        border-bottom: 1px solid #dcd1c0;
        padding: 12px 0;
    }}
    .date-main {{
        font-style: italic;
        font-size: 22px;
        color: #2c2c2c;
    }}
    .date-day {{
        font-size: 34px;
        font-weight: bold;
        color: #2c2c2c;
        line-height: 1.1;
    }}
    .date-month {{
        font-size: 20px;
        letter-spacing: 2px;
        font-weight: bold;
        text-transform: uppercase;
        color: #2c2c2c;
    }}
    .event-details {{
        font-size: 12px;
        color: #555;
        margin: 12px 0;
        line-height: 1.4;
    }}
    .section-title {{
        font-weight: bold;
        letter-spacing: 2px;
        margin: 15px 0 5px 0;
        font-size: 14px;
    }}
    .btn-rsvp {{
        display: inline-block;
        background-color: #554d45;
        color: white !important;
        padding: 9px 24px;
        text-decoration: none;
        border-radius: 3px;
        font-size: 12px;
        letter-spacing: 1px;
        margin: 12px 0;
        font-family: sans-serif;
        font-weight: bold;
    }}
    .btn-rsvp:hover {{
        background-color: #3b352f;
    }}
</style>

<div class="invitation-fullscreen">
    <div class="invitation-card">
        <div class="header-year">2026</div>
        <div class="header-title">Wedding</div>
        
        <img src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&q=80&w=600" class="photo-frame" alt="Boda">
        
        <div class="names">Carolina & Carlos</div>
        
        <div class="message">
            Con amor y con la presencia de Dios entre nosotros, esperamos que este momento sea inolvidable.<br><br>
            Tenemos el honor de invitarlos a celebrar nuestra unión matrimonial.
        </div>
        
        <div class="date-section">
            <div style="font-size: 10px; letter-spacing: 1px; text-transform: uppercase; color: #666;">Los esperamos el día</div>
            <div class="date-main">Sábado</div>
            <div class="date-day">21</div>
            <div style="font-size: 12px; font-style: italic;">de</div>
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
        
        <div class="section-title">VESTIMENTA</div>
        <div style="font-style: italic; font-size: 14px; margin-bottom: 10px;">Formal</div>
        
        <div style="font-size: 11px; letter-spacing: 1px; text-transform: uppercase; margin-top: 15px;">Confirma tu asistencia</div>
        <div style="font-size: 9px; color: #777; margin-bottom: 5px;">POR FAVOR, CONFÍRNANOS VÍA WHATSAPP</div>
        
        <a href="https://wa.me/5216670000000?text=¡Hola!%20Confirmo%20mi%20asistencia%20a%20su%20boda." target="_blank" class="btn-rsvp">CONFIRMA AQUÍ</a>
        
        <div style="font-family: 'Brush Script MT', cursive; font-size: 20px; margin-top: 15px; color: #4a4a4a;">
            ¡Gracias por acompañarnos!
        </div>
    </div>
</div>
"""

# Renderizar directamente con st.markdown para evitar los límites del iframe
st.markdown(invitation_html, unsafe_allow_html=True)
