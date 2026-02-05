"""
Componentes de layout.
"""

import streamlit as st
from typing import Optional


def render_page_header(title: str, subtitle: Optional[str] = None) -> None:
    """Renderiza o cabeçalho da página."""
    st.title(title)
    if subtitle:
        st.caption(subtitle)


def render_section_header(title: str) -> None:
    """Renderiza um título de seção."""
    st.subheader(title)


def render_divider() -> None:
    """Renderiza um divisor visual."""
    st.divider()
