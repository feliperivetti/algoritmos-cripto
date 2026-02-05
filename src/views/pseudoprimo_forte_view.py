import streamlit as st

from src.models.base import AlgorithmResult
from src.views.base_view import BaseView


class PseudoPrimoForteView(BaseView):
    """View para Pseudoprimo Forte."""

    def render(self, result: AlgorithmResult) -> None:
        meta = result.metadata

        if meta.get("error"):
            st.error(meta["error_message"])
            return

        n, b = meta["n"], meta["b"]
        k, q = meta["k"], meta["q"]

        if meta["is_strong_pseudoprime"]:
            st.warning(f"{n} é pseudoprimo forte na base {b}")
        else:
            st.error(f"{n} é composto (base {b})")

        st.subheader("Decomposição")
        st.latex(rf"{n} - 1 = 2^{{{k}}} \cdot {q}")
        c1, c2 = st.columns(2)
        c1.metric("k", k)
        c2.metric("q", q)

        if result.steps:
            with st.expander("Passos"):
                for s in result.steps:
                    if s["resultado"] in (1, n-1):
                        st.success(f"i={s['i']}: {s['base']}^{s['expoente']} ≡ {s['resultado']}")
                    else:
                        st.text(f"i={s['i']}: {s['base']}^{s['expoente']} ≡ {s['resultado']}")
