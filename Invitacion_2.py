import base64
import re
from datetime import datetime
import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Boda de Ismael & Elizabeth 💍",
    page_icon="💍",
    layout="centered",
)

# Función para convertir imágenes locales a Base64
def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"
    except FileNotFoundError:
        return ""

def cargar_svg(path_archivo):
    with open(path_archivo, "r", encoding="utf-8") as f:
        return f.read()


# Renderizar en la pantalla
###svg_contenido = cargar_svg("Frame 48.svg")  # pon aquí el nombre de tu archivo

#st.markdown(
#    f"""
#<div style="text-align: center; margin-top: 10px; margin-bottom: 20px;">
#{svg_contenido}
#</div>
#""",
#    unsafe_allow_html=True,
#)


# Carga de imágenes locales
fondo_b64 = get_image_base64("Fondo_5_brillo.jpg")

# Estilo visual avanzado con CSS (TEXTOS EN COLOR NEGRO / OSCURO) Y EFECTO DE PÉTALOS CAYENDO
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Montserrat:wght@400;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Montserrat:wght@400;600&display=swap');

    /* Fondo de pantalla directo */
    [data-testid="stAppViewContainer"] {{
        background-image: url({fondo_b64});
        background-size: cover;
        background-position: center 35%;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}

    /* --- ENCABEZADOS GLOBALES --- */
    h4, h4 * {{
        color: #EEE955 !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.3rem !important;
        font-weight: 800 !important;
        text-align: center !important;
    }}
    
    h2, h2 * {{
        color: #FFFFFF !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        text-align: center !important;
    }}

    h3, h3 * {{
        color: #FFFFFF !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        text-align: center !important;
    }}
    
    h1, .titulo-principal, h1 * {{
        color: #FAF9F6 !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 800 !important;
        font-size: 3.1rem !important;
        letter-spacing: 1px !important;
        text-align: center !important;
        width: 100% !important;
        margin-left: auto !important;
        margin-right: auto !important;
        display: block !important;
        text-shadow: 
            -0.5px -0.5px 0 #000,  
             0.5px -0.5px 0 #000,
            -0.5px  0.5px 0 #000,
             0.5px  0.5px 0 #000,
             2px  3px 8px rgba(0, 0, 0, 0.65) !important;
    }}

    /* Estilo transparente para los elementos del formulario sin st.form */
    div[data-testid="stVerticalBlock"] > div:has(input) {{
        background: rgba(0, 0, 0, 0.20) !important;
        backdrop-filter: blur(6px) !important;
        -webkit-backdrop-filter: blur(6px) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }}

    /* Garantizar texto blanco en todas las etiquetas de la sección */
    label, .stWidgetLabel p, [data-testid="stRadioButton"] p {{
        color: #FFFFFF !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
    }}
    
    .card {{
    background: rgba(0, 0, 0, 0.20) !important;
    backdrop-filter: blur(6px) !important;
    -webkit-backdrop-filter: blur(6px) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    padding: 24px 20px !important;
    border-radius: 12px !important;
    margin-bottom: 20px !important;
    text-align: center !important;
    }}

    /* Título principal de la tarjeta (Ej. Ceremonia Religiosa) */
    .card-title {{
        color: #ffffff !important; /* Amarillo / Dorado destacado */
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin-bottom: 12px !important;
        display: block !important;
    }}
    
    /* Fecha destacada */
    .card-date {{
        color: #f5f5f5 !important; /* Blanco destacado */
        font-family: 'Montserrat', sans-serif !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        margin-bottom: 14px !important;
        display: block !important;
    }}
    
    /* Detalles (Hora, Lugar, Ciudad) */
    .card-text {{
        color: #EEE955 !important; /* Blanco suave / Gris claro */
        font-family: 'Montserrat', sans-serif !important;
        font-size: 1rem !important;
        margin-bottom: 20px !important;
        display: block !important;
    }}
    
    /* Etiquetas resaltadas (Ej. Hora:, Lugar:) */
    .card-label {{
        color: #f5f5f5 !important; /* Tono dorado elegante */
        font-weight: 700 !important;
    }}
    
    /* Enlaces (Ej. Ubicación de la Misa) */
    .card-link {{
        color: #f5f5f5 !important;
        text-decoration: underline !important;
        font-weight: 600 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 1.05rem !important;
        display: inline-block !important;
        margin-top: 10px !important;
    }}

    .countdown-box {{
        background: #1a1a1a;
        color: #ffffff !important;
        padding: 12px 20px;
        border-radius: 30px;
        font-size: 1.2rem;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }}

    .stButton>button {{
        background: #000000;
        color: white !important;
        border-radius: 25px;
        width: 100%;
        font-weight: 600;
        border: none;
        padding: 12px;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }}

    .stButton>button:hover {{
        background: #333333;
        transform: translateY(-2px);
    }}

    .divider {{
        text-align: center;
        margin: 25px 0;
        color: #FFFFFF;
        font-size: 1.5rem;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# ----------------- ENCABEZADO -----------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h1>Ismael & Elizabeth</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align: center; font-size: 1.3rem; font-style: italic; color: #FFFFFF !important; font-weight: 900;'>¡NOS CASAMOS!</h4>",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="card-label">
    <p style="font-size: 1rem; line-height: 1.6; margin: 0; color: #000000 !important;">
        Hay momentos en la vida que son inolvidables, y compartirlos con las personas que más queremos los hace aún más especiales. 
        Queremos que seas parte de esta gran celebración.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- CUENTA REGRESIVA -----------------
st.markdown("<h2>⏳ Cuenta Regresiva</h2>", unsafe_allow_html=True)
fecha_boda = datetime(2026, 12, 18, 14, 0, 0)
tiempo_restante = fecha_boda - datetime.now()

if tiempo_restante.days > 0:
    st.markdown(
        f"""
    <div style="text-align: center; margin: 20px 0;">
        <span class="countdown-box">¡Faltan {tiempo_restante.days} días para el gran día!</span>
    </div>
    """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
    <div style="text-align: center; margin: 20px 0;">
        <span class="countdown-box">¡Hoy es el gran día! 🎉</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- DETALLES DEL EVENTO (MISA Y FIESTA) -----------------
st.markdown("<h2>✨ ¿Dónde & Cuándo?</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
   st.markdown(
    """
    <div class="card">
    <span class="card-title">⛪ Ceremonia Religiosa</span>
    <span class="card-date">18 de Diciembre de 2026</span>
    
    <p class="card-text"><span class="card-label">Hora:</span> 14:00 hrs</p>
    <p class="card-text"><span class="card-label">Lugar:</span> Parroquia San Gabriel</p>
    <p class="card-text">Culiacán, Sinaloa</p>
    
    <a href="https://maps.google.com" target="_blank" class="card-link">🗺️ Ubicación de la Misa</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
    """
    <div class="card">
    <span class="card-title">🎉 Fiesta</span>
    <span class="card-date">18 de Diciembre de 2026</span>
    
    <p class="card-text"><span class="card-label">Hora:</span> 19:00 hrs</p>
    <p class="card-text"><span class="card-label">Lugar:</span> Salón Metropolitan: Piso 1</p>
    <p class="card-text">Culiacán, Sinaloa</p>
    
    <a href="https://www.google.com/maps/place/Sal%C3%B3n+Metropolitan/@24.7943447,-107.4047708,16.67z/data=!4m6!3m5!1s0x86bcd0beee3643ff:0xf86e169e6767365b!8m2!3d24.7953022!4d-107.4048423!16s%2Fg%2F1tg7sg73?entry=ttu&g_ep=EgoyMDI2MDgxMi4wIKXMDSoASAFQAw%3D%3D" target="_blank" class="card-link">
        🗺️ Ubicación de la Fiesta
    </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- NOTAS IMPORTANTES -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>💡 Información Importante</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
<span class="card-title">🎁 Mesa de Regalos</span>
<p class="card-label">Tu presencia es nuestro mejor regalo. Si deseas tener un detalle adicional:</p>

<p class="card-text">
    • <span class="card-label">Liverpool:</span> 
    <a href="https://mesaderegalos.liverpool.com.mx/milistaderegalos/60030339" target="_blank" class="card-text">Ver mesa de regalos aquí</a>
</p>
""",
    unsafe_allow_html=True,
)

# ----------------- GALERÍA DE FOTOS LOCALES -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>📸 Nuestra Historia</h2>", unsafe_allow_html=True)

g_col1, g_col2, g_col3 = st.columns(3)
with g_col1:
    try:
        st.image("Foto_1.jpg", use_container_width=True)
    except Exception:
        st.write("📷 Foto 1")
with g_col2:
    try:
        st.image("Foto_2.jpg", use_container_width=True)
    except Exception:
        st.write("📷 Foto 2")
with g_col3:
    try:
        st.image("Foto_3.jpg", use_container_width=True)
    except Exception:
        st.write("📷 Foto 3")


# ----------------- FORMULARIO RSVP -----------------

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>💌 Confirmación de Asistencia</h2>", unsafe_allow_html=True)


# Creamos un contenedor reactivo que mantendrá la tarjeta transparente
with st.container():
    # 1. Nombre principal
    nombre = st.text_input("Nombre completo:")

    # 2. Teléfono celular
    telefono = st.text_input(
        "Teléfono celular (10 dígitos):",
        max_chars=10,
        placeholder="Ej. 6671234567",
    )

    # 3. Número de acompañantes
    acompanantes = st.number_input(
        "Número de acompañantes adicionales:",
        min_value=0,
        max_value=5,
        step=1,
        value=0,
    )

    # 4. Campos dinámicos para nombres de acompañantes
    nombres_acompanantes = []
    if acompanantes > 0:
        st.markdown(
            "<p style='color: #FFFFFF !important; font-weight: 600; margin-top: 15px; margin-bottom: 5px;'>Nombres de tus acompañantes:</p>",
            unsafe_allow_html=True,
        )
        for i in range(int(acompanantes)):
            nombre_acomp = st.text_input(
                f"Nombre completo del acompañante {i+1}:", key=f"acomp_{i}"
            )
            nombres_acompanantes.append(nombre_acomp)

    # 5. Asistencia y Restricciones
    asistencia = st.radio(
        "¿Nos acompañarás?",
        [
            "Sí, ahí estaré con mucho gusto 🥂",
            "Lamentablemente no podré asistir ❤️",
        ],
    )

    restricciones = st.text_input("Alergias o restricciones alimentarias:")

    # Botón normal
    enviar = st.button("Enviar Confirmación ✨", use_container_width=True)

    if enviar:
        nombre_clean = nombre.strip()
        telefono_clean = re.sub(r"\D", "", telefono.strip())  # Solo dígitos
        lista_nombres_acomp = [
            n.strip() for n in nombres_acompanantes if n.strip() != ""
        ]

        # Validaciones
        if not nombre_clean:
            st.error(
                "Por favor, ingresa tu nombre completo antes de enviar la confirmación."
            )

        elif len(telefono_clean) != 10:
            st.error(
                "Por favor, ingresa un número de teléfono celular válido a 10 dígitos (ej. 6671234567)."
            )

        elif acompanantes > 0 and len(lista_nombres_acomp) < acompanantes:
            st.error(
                "Por favor, completa los nombres de todos tus acompañantes."
            )

        else:
            try:
                df = pd.read_csv("asistentes.csv")
            except FileNotFoundError:
                df = pd.DataFrame(
                    columns=[
                        "Fecha_Registro",
                        "Nombre",
                        "Telefono",
                        "Asistencia",
                        "Acompañantes",
                        "Nombres_Acompañantes",
                        "Restricciones",
                        "Mesa",
                    ]
                )

            # Asegurar que la columna 'Telefono' exista si el CSV ya se había creado previamente sin ella
            if "Telefono" not in df.columns:
                df["Telefono"] = ""

            cadena_acompanantes = (
                ", ".join(lista_nombres_acomp)
                if lista_nombres_acomp
                else "Ninguno"
            )

            nuevo_dato = pd.DataFrame([
                {
                    "Fecha_Registro": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "Nombre": nombre_clean,
                    "Telefono": telefono_clean,
                    "Asistencia": asistencia,
                    "Acompañantes": acompanantes,
                    "Nombres_Acompañantes": cadena_acompanantes,
                    "Restricciones": restricciones,
                    "Mesa": "Por asignar",
                }
            ])

            df = pd.concat([df, nuevo_dato], ignore_index=True)
            df.to_csv("asistentes.csv", index=False)

            st.balloons()
            st.markdown(
                f"""
                <div style="
                    background-color: #FFFFFF; 
                    padding: 16px; 
                    border-radius: 8px; 
                    border: 1px solid #E0E0E0;
                    box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
                    margin: 10px 0px;">
                    <span style="font-size: 18px; margin-right: 8px;">✅</span>
                    <span style="color: #262730; font-weight: 500;">
                        ¡Muchas gracias <strong>{nombre_clean}</strong>! Hemos recibido tu confirmación.
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ----------------- BUSCADOR DE MESA PARA INVITADOS -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>🍽️ Consulta tu Mesa</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
    <p style="color: #000000 !important;">Ingresa tu nombre tal como lo registraste para consultar tu mesa asignada.</p>
</div>
""",
    unsafe_allow_html=True,
)

nombre_buscar = st.text_input("Escribe tu nombre:", key="buscar_mesa")

if nombre_buscar.strip() != "":
    try:
        df_mesas = pd.read_csv("asistentes.csv")
        if "Mesa" in df_mesas.columns:
            resultado = df_mesas[
                df_mesas["Nombre"].str.contains(
                    nombre_buscar, case=False, na=False
                )
            ]

            if not resultado.empty:
                for idx, row in resultado.iterrows():
                    mesa_asignada = row.get("Mesa", "Aún no asignada")
                    if (
                        pd.isna(mesa_asignada)
                        or str(mesa_asignada).strip() == ""
                    ):
                        mesa_asignada = "Por asignar"

                    st.info(
                        f"👤 **{row['Nombre']}**: Tu mesa asignada es la **Mesa"
                        f" {mesa_asignada}** 🥂"
                    )
            else:
                st.warning(
                    "No encontramos ninguna confirmación con ese nombre."
                )
        else:
            st.info("La asignación de mesas aún no está disponible.")
    except FileNotFoundError:
        st.info("Aún no hay confirmaciones registradas.")
        
# ----------------- BUSCADOR DE MESA PARA INVITADOS -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>🍽️ Consulta tu Mesa</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
    <p class="card-text">Ingresa tu nombre tal como lo registraste para consultar tu mesa asignada.</p>
</div>
""",
    unsafe_allow_html=True,
)

nombre_buscar = st.text_input("Escribe tu nombre:", key="buscar_mesa_invitado")

if nombre_buscar.strip() != "":
    try:
        df_mesas = pd.read_csv("asistentes.csv")
        if "Mesa" in df_mesas.columns:
            resultado = df_mesas[
                df_mesas["Nombre"].str.contains(
                    nombre_buscar, case=False, na=False
                )
            ]

            if not resultado.empty:
                for idx, row in resultado.iterrows():
                    mesa_asignada = row.get("Mesa", "Aún no asignada")
                    if (
                        pd.isna(mesa_asignada)
                        or str(mesa_asignada).strip() == ""
                    ):
                        mesa_asignada = "Por asignar"

                    st.info(
                        f"👤 **{row['Nombre']}**: Tu mesa asignada es la **Mesa"
                        f" {mesa_asignada}** 🥂"
                    )
            else:
                st.warning(
                    "No encontramos ninguna confirmación con ese nombre."
                )
        else:
            st.info("La asignación de mesas aún no está disponible.")
    except FileNotFoundError:
        st.info("Aún no hay confirmaciones registradas.")

# ----------------- PANEL DE ADMINISTRACIÓN -----------------
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("🔐 Panel de Administración (Novios)"):
    pin = st.text_input("Ingresa el PIN de administrador:", type="password", key="pin_admin")
    
    if pin == "1812":
        try:
            df_asistentes = pd.read_csv("asistentes.csv")

            if df_asistentes.empty:
                st.info("Aún no hay confirmaciones registradas en la lista.")
            else:
                if "Mesa" not in df_asistentes.columns:
                    df_asistentes["Mesa"] = "Por asignar"

                st.subheader("📋 Lista de Asistentes")
                st.dataframe(df_asistentes, use_container_width=True)

                st.markdown("---")
                st.subheader("🗑️ Eliminar una Confirmación")
                
                # Lista de nombres para el desplegable
                lista_invitados = df_asistentes["Nombre"].tolist()
                invitado_a_eliminar = st.selectbox(
                    "Selecciona el invitado que deseas borrar:",
                    options=lista_invitados,
                    key="select_eliminar"
                )

                if st.button("Eliminar Registro ❌", use_container_width=True):
                    # Filtrar el dataframe quitando la fila del invitado seleccionado
                    df_asistentes = df_asistentes[df_asistentes["Nombre"] != invitado_a_eliminar]
                    
                    # Guardar los cambios en el CSV
                    df_asistentes.to_csv("asistentes.csv", index=False)
                    
                    st.success(f"Se ha eliminado el registro de **{invitado_a_eliminar}** correctamente.")
                    st.rerun()  # Recarga la app para refrescar la tabla

        except FileNotFoundError:
            st.info("No hay lista de asistentes creada aún.")
