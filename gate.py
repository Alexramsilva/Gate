import streamlit as st

st.set_page_config(page_title="Acceso por Servicio", layout="centered")

# ---------------------------------------
# Base de servicios / usuarios
# ---------------------------------------
SERVICIOS = {
    "S1": {"usuario": "U1", "password": "P1"},
    "S2": {"usuario": "U2", "password": "P2"},
    "S3": {"usuario": "U3", "password": "P3"},
    "S4": {"usuario": "U4", "password": "P4"},
    "Toca": {"usuario": "Banorte", "password": "Oro"},
}

# ---------------------------------------
# Estado de sesión
# ---------------------------------------
if "login" not in st.session_state:
    st.session_state.login = False

# ---------------------------------------
# LOGIN
# ---------------------------------------
if not st.session_state.login:
    st.title("🔐 Login de acceso")

    user = st.text_input("Usuario")
    pwd = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        acceso = False
        for s in SERVICIOS.values():   # ✅ CORREGIDO
            if user == s["usuario"] and pwd == s["password"]:
                acceso = True
                break

        if acceso:
            st.session_state.login = True
            st.success("Acceso concedido")
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

# ---------------------------------------
# ÁREA INTERNA
# ---------------------------------------
else:
    st.sidebar.success("Sesión activa")

    st.title("📋 Consulta de usuarios y contraseñas")

    for servicio, datos in SERVICIOS.items():  # ✅ CORREGIDO
        with st.expander(servicio):
            st.write(f"Usuario: `{datos['usuario']}`")
            st.write(f"Password: `{datos['password']}`")

    if st.button("Cerrar sesión"):
        st.session_state.login = False
        st.rerun()

# ---------------------------------------
# Personalización visual
# -----------------
