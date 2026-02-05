"""
Componentes de formulário.
"""

import streamlit as st


def render_input_group(params: list, controller) -> dict:
    """
    Renderiza um grupo de inputs organizados.

    Args:
        params: Lista de ParamConfig
        controller: AlgorithmController

    Returns:
        Dicionário com os valores dos inputs
    """
    st.latex(controller.input_format_latex)
    st.markdown("")

    num_params = len(params)
    cols = st.columns(min(num_params, 3))

    raw_inputs = {}
    for i, param in enumerate(params):
        with cols[i % len(cols)]:
            value = st.text_input(
                param.label,
                key=param.name,
                placeholder=f"Digite {param.label}"
            )
            raw_inputs[param.name] = value

    return raw_inputs


def render_execute_button() -> bool:
    """Renderiza o botão de executar centralizado."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        return st.button("Executar", type="primary", use_container_width=True)
