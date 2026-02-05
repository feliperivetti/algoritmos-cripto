import streamlit as st

from src.models.base import AlgorithmResult
from src.views.base_view import BaseView


class ModularExpView(BaseView):
    """View para Exponenciação Modular."""

    MAX_VISIBLE_STEPS = 6  # 3 no início + 3 no final

    def render(self, result: AlgorithmResult) -> None:
        meta = result.metadata
        a, b, n = meta["a"], meta["b"], meta["n"]
        cycle_length = meta["cycle_length"]
        cycle_value = meta["cycle_value"]
        quotient = meta["quotient"]
        remainder_exp = meta["remainder_exp"]

        # Resultado em destaque
        st.success(f"**Resultado:** {a}^{b} mod {n} = **{result.result}**")

        # Expander: Achando o Ciclo
        with st.expander("Achando um Ciclo"):
            steps = result.steps
            total_steps = len(steps)

            if total_steps <= self.MAX_VISIBLE_STEPS:
                for s in steps:
                    st.latex(rf"{a}^{{{s['expoente']}}} \equiv {s['resto']} \pmod{{{n}}}")
            else:
                # Primeiros 3
                for s in steps[:3]:
                    st.latex(rf"{a}^{{{s['expoente']}}} \equiv {s['resto']} \pmod{{{n}}}")

                st.latex(r"\cdots")

                # Últimos 3
                for s in steps[-3:]:
                    st.latex(rf"{a}^{{{s['expoente']}}} \equiv {s['resto']} \pmod{{{n}}}")

                omitted = total_steps - self.MAX_VISIBLE_STEPS
                st.warning(f"{omitted} linhas omitidas no meio.")

        # Expander: Substituição
        with st.expander("Substituindo na Expressão"):
            # Passo 1: Decomposição
            st.latex(
                rf"{a}^{{{b}}} \equiv ({a}^{{{cycle_length}}})^{{{quotient}}} "
                rf"\cdot {a}^{{{remainder_exp}}} \pmod{{{n}}}"
            )

            # Passo 2: Substituir valor do ciclo
            st.latex(
                rf"{a}^{{{b}}} \equiv ({cycle_value})^{{{quotient}}} "
                rf"\cdot {a}^{{{remainder_exp}}} \pmod{{{n}}}"
            )

            # Passo 3: Calcular potência do ciclo
            cycle_power = pow(cycle_value, quotient, n)
            st.latex(
                rf"{a}^{{{b}}} \equiv ({cycle_power}) \cdot {a}^{{{remainder_exp}}} \pmod{{{n}}}"
            )

            # Passo 4: Substituir a^remainder
            remainder_value = meta["remainders"].get(remainder_exp, pow(a, remainder_exp, n))
            st.latex(rf"{a}^{{{b}}} \equiv ({cycle_power}) \cdot ({remainder_value}) \pmod{{{n}}}")

            # Resultado final
            st.latex(rf"{a}^{{{b}}} \equiv \boxed{{{result.result}}} \pmod{{{n}}}")
