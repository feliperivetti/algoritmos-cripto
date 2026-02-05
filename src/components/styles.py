"""
Estilos CSS globais.
"""

import streamlit as st


def inject_custom_css() -> None:
    """Injeta CSS customizado na página."""
    st.markdown("""
    <style>
        /* Reset e base */
        .stApp {
            background-color: #FFFFFF;
        }

        /* Esconder menu e footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Botão primário */
        .stButton > button[kind="primary"] {
            background-color: #1E3A5F;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: 500;
            padding: 0.5rem 1rem;
        }

        .stButton > button[kind="primary"]:hover {
            background-color: #2563EB;
        }

        /* Inputs */
        .stTextInput input {
            border: 1px solid #D1D5DB;
            border-radius: 6px;
        }

        .stTextInput input:focus {
            border-color: #1E3A5F;
            box-shadow: 0 0 0 1px #1E3A5F;
        }

        /* Selectbox */
        .stSelectbox > div > div {
            border-radius: 6px;
        }

        /* Expander */
        .streamlit-expanderHeader {
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)
