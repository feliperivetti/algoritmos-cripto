import pandas as pd
import streamlit as st
from src.models.base import AlgorithmResult
from src.views.base_view import BaseView


class AcharFatorView(BaseView):
    """View para Achar um Fator."""
    
    def render(self, result: AlgorithmResult) -> None:
        meta = result.metadata
        n = meta["n"]
        
        if meta["is_prime"]:
            st.success(f"{n} é primo")
        else:
            f = meta["factor"]
            st.info(f"Fator encontrado: **{f}** ({n} = {f} × {n//f})")
        
        st.metric("Passos", meta["steps_count"])
        
        if result.steps:
            with st.expander(f"Passos ({len(result.steps)})"):
                df = pd.DataFrame(result.steps)
                st.dataframe(df.head(20) if len(df) > 20 else df, hide_index=True)
