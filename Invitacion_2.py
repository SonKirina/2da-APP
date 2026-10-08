import base64
import os
import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página (ancho completo)
st.set_page_config(
    page_title="Invitación de Boda", page_icon="💍", layout="wide"
)

# Ocultar los elementos de cabecera y pie de página predeterminados de Streamlit para ganar espacio limpio
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Función para cargar la imagen de fondo desde el repositorio de GitHub
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

# Código HTML y CSS de la invitación optimizado para pantalla completa sin scroll interno
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    html, body {{
        background-color: #2b2b2b;
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Elimina cualquier barra de scroll */
    }}
    .invitation-container {{
        max-width: 380px;
        width: 100%;
        max-height: 95vh;
        {background_css}
        padding: 25px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        font-family: 'Times New Roman', serif;
        color: #333333;
        text-align: center;
        box-sizing: border-box;
        overflow-y: auto; /* Si el contenido sobrepasa la pantalla móvil, se desplaza internamente de forma suave */
    }}
    /* Ocultar barra de scroll interna en navegadores modernos */
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
        height: 220px;
        object-fit: cover;
        border-radius: 4px;
        margin: 12px 0;
    }}
    .names {{
        font-family: 'Brush Script MT', cursive, serif;
        font-size: 36px;
        color: #2c2c2c;
        margin: 8px 0;
    }}
    .message {{
        font-size: 10.5px;
        line-height: 1.4;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #555555;
        margin-bottom: 15px;
        padding: 0 5px;
    }}
    .date-section {{
        margin: 12px 0;
        border-top: 1px solid #dcd1c0;
        border-bottom: 1px solid #dcd1c0;
        padding: 10px 0;
    }}
    .date-main {{
        font-style: italic;
        font-size: 20px;
        color: #2c2c2c;
    }}
    .date-day {{
        font-size: 30px;
        font-weight: bold;
        color: #2c2c2c;
        line-height: 1.1;
    }}
    .date-month {{
        font-size: 18px;
        letter-spacing: 2px;
        font-weight: bold;
        text-transform: uppercase;
        color: #2c2c2c;
    }}
    .event-details {{
        font-size: 11.5px;
        color: #555;
        margin: 12px 0;
        line-height: 1.3;
    }}
    .section-title {{
        font-weight: bold;
        letter-spacing: 2px;
        margin: 12px 0 3px 0;
        font-size: 13px;
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
        margin: 8px 0;
        font-family: sans-serif;
        font-weight: bold;
    }}
    .btn-rsvp:hover {{
        background-color: #3b352f;
    }}
</style>
</head>
<body>
    <div class="invitation-container">
        <div class="header-year">2026</div>
        <div class="header-title">Wedding</div>
        
        <img src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&q=80&w=600" class="photo-frame" alt="Boda">
        
        <div class="names">Carolina & Carlos</div>
        
        <div class="message">
            Con amor y con la presencia de Dios entre nosotros, esperamos que este momento sea inolvidable.<br><br>
            Tenemos el honor de invitarlos a celebrar nuestra unión matrimonial.
        </div>
        
        <div class="date-section">
            <div style="font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: #666;">Los esperamos el día</div>
            <div class="date-main">Sábado</div>
            <div class="date-day">21</div>
            <div style="font-size: 11px; font-style: italic;">de</div>
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
        <div style="font-style: italic; font-size: 13px; margin-bottom: 8px;">Formal</div>
        
        <div style="font-size: 10px; letter-spacing: 1px; text-transform: uppercase; margin-top: 10px;">Confirma tu asistencia</div>
        <div style="font-size: 8.5px; color: #777; margin-bottom: 4px;">POR FAVOR, CONFÍRNANOS VÍA WHATSAPP</div>
        
        <a href="https://wa.me/5216670000000?text=¡Hola!%20Confirmo%20mi%20asistencia%20a%20su%20boda." target="_blank" class="btn-rsvp">CONFIRMA AQUÍ</a>
        
        <div style="font-family: 'Brush Script MT', cursive; font-size: 18px; margin-top: 15px; color: #4a4a4a;">
            ¡Gracias por acompañarnos!
        </div>
    </div>
</body>
</html>
"""

# Renderizar ajustado a la altura total de la ventana sin barras de desplazamiento de la página
components.html(html_content, height=730, scrolling=False)
