import streamlit as st

from src.models.base import AlgorithmResult
from src.views.base_view import BaseView


class TeoremaChinesView(BaseView):
    """View para o Teorema Chinês do Resto."""

    def render(self, result: AlgorithmResult) -> None:
        """Renderiza os resultados do CRT."""
        st.header("Teorema Chinês do Resto")

        # Verifica erro
        if result.metadata and result.metadata.get("error"):
            st.error(result.metadata["error_message"])
            return

        # Resultado Principal
        st.success(f"Solução: X ≡ {result.result} (mod {result.metadata['M']})")

        st.subheader("Passo a Passo")
        
        # Detalhes dos Termos
        terms = result.metadata.get("terms_details", [])
        if terms:
            st.markdown("### Cálculo dos Termos")
            st.markdown(r"A solução é dada por $X = \sum a_i \cdot M_i \cdot y_i \pmod M$")
            
            for term in terms:
                st.markdown("---")
                st.markdown(f"**Termo {term['i']}** (para $a_{term['i']}={term['a_i']}, m_{term['i']}={term['m_i']}$)")
                st.write(f"- $M_{term['i']} = M / m_{term['i']} = {term['M_i']}$")
                st.write(f"- $y_{term['i']} = (M_{term['i']})^{{-1}} \pmod{{m_{term['i']}}} = {term['y_i']}$")
                st.write(f"- Parcela: ${term['a_i']} \cdot {term['M_i']} \cdot {term['y_i']} = {term['term']}$")

        # Passos Gerais
        if result.steps:
            st.markdown("### Log de Execução")
            for step in result.steps:
                if "equation" in step:
                    st.text(f"Equação: {step['equation']} -> {step['calculation']}")
                elif "step" in step:
                     st.text(f"{step['step']}: {step.get('M', '')}")
