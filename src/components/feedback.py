"""
Componentes de feedback (alertas, mensagens).
"""

import streamlit as st


def render_alert(message: str, variant: str = "info") -> None:
    """
    Renderiza um alerta usando componentes nativos do Streamlit.
    """
    if variant == "success":
        st.success(message)
    elif variant == "warning":
        st.warning(message)
    elif variant == "error":
        st.error(message)
    else:
        st.info(message)
