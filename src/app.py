"""
Entry point para o Streamlit.
"""

import streamlit as st

from src.algorithm_info import get_algorithm_info
from src.controllers.algorithm_controller import ALGORITHMS, AlgorithmController

# Configuração da página
st.set_page_config(
    page_title="Algoritmos Cripto",
    page_icon="🔐",
    layout="centered",
)

# CSS com acentos azuis
st.markdown("""
<style>
    /* Esconder elementos do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Título principal em azul */
    h1 {
        color: #1E3A5F !important;
    }

    /* Subtítulos com cor azul */
    h2, h3 {
        color: #1E3A5F !important;
    }

    /* Borda azul nos expanders */
    .streamlit-expanderHeader {
        background-color: #EFF6FF !important;
        border-left: 4px solid #3B82F6 !important;
        border-radius: 4px;
    }

    /* Métricas com destaque */
    [data-testid="stMetricValue"] {
        color: #1E3A5F !important;
        font-weight: 600;
    }

    /* Labels das métricas */
    [data-testid="stMetricLabel"] {
        color: #3B82F6 !important;
    }

    /* Selectbox com borda azul no foco */
    .stSelectbox > div > div {
        border-color: #3B82F6 !important;
    }

    /* Inputs com borda azul no foco */
    .stTextInput input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 1px #3B82F6 !important;
    }

    /* Divider com tom azul */
    hr {
        border-color: #BFDBFE !important;
    }

    /* Success com tom azul-esverdeado */
    .stSuccess {
        background-color: #ECFDF5 !important;
        border-left: 4px solid #10B981 !important;
    }

    /* Info com tom azul */
    .stInfo {
        background-color: #EFF6FF !important;
        border-left: 4px solid #3B82F6 !important;
    }

    /* Caption com cor azul suave */
    .stCaption {
        color: #64748B !important;
    }
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
