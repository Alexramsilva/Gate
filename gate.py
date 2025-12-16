import streamlit as st

st.set_page_config(page_title="Acceso por Servicio", layout="centered")

SERVICIOS = {
    "S1": {"usuario": "alexramsilva@hotmail.com", "password": "fanytequiero"},
    "S2": {"usuario": "alexramsilva@gmail.com", "password": "Fanytequiero1*"},
    "S3": {"usuario": "alexramsilva@hotmail.com", "password": "Fanytequiero1*"},
    "S3": {"usuario": "alexramsilva@hotmail.com", "password": "fanytequiero"},
    "Toca ": {"usuario": "Banorte", "password": "Oro"},

}


# -------------------------------------------------
# Estado de sesión
# -------------------------------------------------
if "login" not in st.session_state:
    st.session_state.login = False

# -------------------------------------------------
# LOGIN
# -------------------------------------------------
if not st.session_state.login:
    st.title("Login de acceso")

    user = st.text_input("Usuario")
    pwd = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        acceso = False
        for s in USUARIOS.values():
            if user == s["usuario"] and pwd == s["password"]:
                acceso = True
                break

        if acceso:
            st.session_state.login = True
            st.success("Acceso concedido")
            st.rerun()
        else:
            st.error("Credenciales incorrectas")

# -------------------------------------------------
# ÁREA INTERNA
# -------------------------------------------------
else:
    st.sidebar.success("Sesión activa")

    st.title("Consulta de usuarios y contraseñas")

    for servicio, datos in USUARIOS.items():
        with st.expander(servicio):
            st.write(f"Usuario: `{datos['usuario']}`")
            st.write(f"Password: `{datos['password']}`")

    if st.button("Cerrar sesión"):
        st.session_state.login = False
        st.rerun()


# Personalización de diseño
st.markdown("""
<style>
    .stApp {
        background-color:  #5BF58E;
    }
    .css-1d391kg {
        color:  #000000;
    }
</style>
""", unsafe_allow_html=True)

