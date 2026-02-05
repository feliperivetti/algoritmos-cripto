"""
Entry point para o Streamlit.
"""

import streamlit as st
from src.controllers.algorithm_controller import ALGORITHMS, AlgorithmController
from src.algorithm_info import get_algorithm_info

# Configuração da página
st.set_page_config(
    page_title="Algoritmos Cripto",
    page_icon="🔐",
    layout="centered",
)

# CSS mínimo
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


def main():
    st.title("Algoritmos de Criptografia")
    st.caption("Ferramentas para Teoria dos Números")
    
    # Seletor de algoritmo
    algorithm_list = list(ALGORITHMS.keys())
    selected = st.selectbox(
        "Selecione o algoritmo",
        algorithm_list,
        format_func=lambda x: f"{get_algorithm_info(x).get('icon', '')} {x}"
    )
    
    if not selected:
        return
    
    # Info do algoritmo
    info = get_algorithm_info(selected)
    if info.get("description"):
        with st.expander("Sobre este algoritmo"):
            st.markdown(info["description"])
            if info.get("example"):
                st.info(info["example"])
    
    st.divider()
    
    # Controller
    controller = AlgorithmController(selected)
    
    # Inputs
    st.subheader("Entrada")
    st.latex(controller.input_format_latex)
    
    params = controller.params
    cols = st.columns(len(params))
    
    raw_inputs = {}
    for i, param in enumerate(params):
        with cols[i]:
            raw_inputs[param.name] = st.text_input(
                param.label,
                key=param.name,
                placeholder=f"Digite {param.label}"
            )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        execute = st.button("Executar", type="primary", use_container_width=True)
    
    # Execução
    if execute:
        if all(raw_inputs.values()):
            st.divider()
            st.subheader("Resultados")
            with st.spinner("Processando..."):
                controller.execute(raw_inputs)
        else:
            st.warning("Preencha todos os campos.")


if __name__ == "__main__":
    main()
