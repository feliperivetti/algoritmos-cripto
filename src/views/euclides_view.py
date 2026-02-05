import pandas as pd
import streamlit as st

from src.models.base import AlgorithmResult
from src.views.base_view import BaseView


class EuclidesView(BaseView):
    """View para o Algoritmo Euclidiano Estendido."""

    def render(self, result: AlgorithmResult, nested: bool = False) -> None:
        """
        Renderiza o resultado.

        Args:
            result: Resultado do algoritmo
            nested: Se True, não usa expanders (para evitar aninhamento)
        """
        meta = result.metadata
        a, b = meta["original_a"], meta["original_b"]
        mdc, alpha, beta = meta["mdc"], meta["alpha"], meta["beta"]

        # Métricas
        c1, c2, c3 = st.columns(3)
        c1.metric("MDC", mdc)
        c2.metric("α", alpha)
        c3.metric("β", beta)

        # Verificação
        verification = alpha*a + beta*b
        st.latex(rf"({alpha}) \cdot ({a}) + ({beta}) \cdot ({b}) = {verification}")
        if verification == mdc:
            st.success("✓ Identidade de Bézout verificada")

        # Passos
        if not nested:
            with st.expander("Passos do Algoritmo"):
                st.dataframe(pd.DataFrame(result.steps), hide_index=False, use_container_width=True)
        else:
            st.caption("Passos:")
            st.dataframe(pd.DataFrame(result.steps), hide_index=False, use_container_width=True)
