import streamlit as st

# Configuración de la página centrada para simular una invitación móvil
st.set_page_config(
    page_title="Invitación de Boda", page_icon="💍", layout="centered"
)

# Estilos CSS para replicar la estructura visual de la tarjeta
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2b2b2b;
    }
    .invitation-container {
        max-width: 400px;
        margin: auto;
        background-color: #f2f1ed;
        padding: 30px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        font-family: 'Times New Roman', serif;
        color: #333333;
        text-align: center;
    }
    .header-year {
        font-size: 26px;
        letter-spacing: 3px;
        font-weight: bold;
        color: #2c2c2c;
    }
    .header-title {
        font-style: italic;
        font-size: 28px;
        margin-top: -5px;
        color: #555;
    }
    .photo-frame {
        width: 100%;
        height: 240px;
        object-fit: cover;
        border-radius: 4px;
        margin: 15px 0;
    }
    .names {
        font-family: 'Brush Script MT', cursive, serif;
        font-size: 38px;
        color: #2c2c2c;
        margin: 10px 0;
    }
    .message {
        font-size: 11px;
        line-height: 1.5;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #555555;
        margin-bottom: 20px;
        padding: 0 10px;
    }
    .date-section {
        margin: 15px 0;
        border-top: 1px solid #dcd1c0;
        border-bottom: 1px solid #dcd1c0;
        padding: 12px 0;
    }
    .date-main {
        font-style: italic;
        font-size: 22px;
        color: #2c2c2c;
    }
    .date-day {
        font-size: 34px;
        font-weight: bold;
        color: #2c2c2c;
        line-height: 1.1;
    }
    .date-month {
        font-size: 20px;
        letter-spacing: 2px;
        font-weight: bold;
        text-transform: uppercase;
        color: #2c2c2c;
    }
    .event-details {
        font-size: 12px;
        color: #555;
        margin: 15px 0;
        line-height: 1.4;
    }
    .section-title {
        font-weight: bold;
        letter-spacing: 2px;
        margin: 15px 0 5px 0;
        font-size: 14px;
    }
    .btn-rsvp {
        display: inline-block;
        background-color: #554d45;
        color: white !important;
        padding: 8px 22px;
        text-decoration: none;
        border-radius: 3px;
        font-size: 12px;
        letter-spacing: 1px;
        margin: 10px 0;
        font-family: sans-serif;
        font-weight: bold;
    }
    .btn-rsvp:hover {
        background-color: #3b352f;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Estructura HTML de la invitación
st.markdown(
    """
    <div class="invitation-container">
        <div class="header-year">2026</div>
        <div class="header-title">Wedding</div>
        
        <!-- Imagen de los novios (puedes cambiar el enlace por tu propia foto) -->
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
        
        <!-- Enlace directo para confirmar asistencia por WhatsApp -->
        <a href="https://wa.me/5216670000000?text=¡Hola!%20Confirmo%20mi%20asistencia%20a%20su%20boda." target="_blank" class="btn-rsvp">CONFIRMA AQUÍ</a>
        
        <div style="font-family: 'Brush Script MT', cursive; font-size: 20px; margin-top: 20px; color: #4a4a4a;">
            ¡Gracias por acompañarnos!
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
