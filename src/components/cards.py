"""
Componentes de cards e métricas.
"""

from typing import Optional

import streamlit as st


def render_metric_card(label: str, value: str) -> None:
    """Renderiza um card de métrica usando componentes nativos."""
    st.metric(label=label, value=value)


def render_result_card(content: str, variant: str = "default") -> None:
    """
    Renderiza um card de resultado.
    """
    if variant == "success":
        st.success(content)
    elif variant == "warning":
        st.warning(content)
    elif variant == "error":
        st.error(content)
    else:
        st.info(content)


def render_highlight_box(
    title: str,
    value: str,
    subtitle: Optional[str] = None,
    variant: str = "default"
) -> None:
    """Renderiza uma caixa de destaque para resultados importantes."""

    # Container com visual limpo
    with st.container():
        st.markdown(f"**{title}**")
        st.markdown(f"### {value}")
        if subtitle:
            st.caption(subtitle)
