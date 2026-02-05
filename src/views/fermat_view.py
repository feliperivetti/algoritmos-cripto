import pandas as pd
import streamlit as st
from src.models.base import AlgorithmResult
from src.views.base_view import BaseView


class FermatView(BaseView):
    """View para o Algoritmo de Fermat."""
    
    def render(self, result: AlgorithmResult) -> None:
        meta = result.metadata
        n = meta["n"]
        
        if meta["is_prime"]:
            st.success(f"{n} é primo")
        else:
            f1, f2 = meta["factor1"], meta["factor2"]
            st.info(f"Fatoração: {n} = {f1} × {f2}")
            c1, c2 = st.columns(2)
            c1.metric("Fator 1", f1)
            c2.metric("Fator 2", f2)
        
        if result.steps:
            with st.expander("Passos"):
                st.dataframe(pd.DataFrame(result.steps), hide_index=True)
