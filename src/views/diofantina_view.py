import streamlit as st
from src.models.base import AlgorithmResult
from src.views.base_view import BaseView
from src.views.euclides_view import EuclidesView


class DiofantinaView(BaseView):
    """View para a Equação Diofantina."""
    
    def render(self, result: AlgorithmResult) -> None:
        meta = result.metadata
        
        if not meta.get("has_solution", True):
            st.error(f"Sem solução: {meta.get('reason', 'MDC não divide c')}")
            return
        
        a, b, c = meta['a'], meta['b'], meta['c']
        mdc = meta['mdc']
        alpha = meta['alpha']
        beta = meta['beta']
        x0, y0 = meta['x0'], meta['y0']
        divisor = meta['divisor']
        x_coef = meta['x_coef']
        y_coef = meta['y_coef']
        
        # Resultado em destaque
        st.success(f"**Solução encontrada:** X₀ = {x0}, Y₀ = {y0}")
        
        # Expander: Euclides Estendido
        with st.expander("Passo 1: Euclides Estendido"):
            EuclidesView().render(meta["euclides_result"], nested=True)
        
        # Expander: Solução Particular
        with st.expander("Solução Particular"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.latex(rf"X_0 = \alpha \cdot \left( \frac{{c}}{{\text{{mdc}}}} \right)")
                st.latex(rf"X_0 = {alpha} \cdot \left( \frac{{{c}}}{{{mdc}}} \right)")
                st.latex(rf"X_0 = {alpha} \cdot {divisor} = {x0}")
            
            with col2:
                st.latex(rf"Y_0 = \beta \cdot \left( \frac{{c}}{{\text{{mdc}}}} \right)")
                st.latex(rf"Y_0 = {beta} \cdot \left( \frac{{{c}}}{{{mdc}}} \right)")
                st.latex(rf"Y_0 = {beta} \cdot {divisor} = {y0}")
        
        # Expander: Solução Geral
        with st.expander("Solução Geral"):
            st.markdown("Para todo **t ∈ ℤ**:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.latex(rf"X = X_0 + \frac{{b}}{{\text{{mdc}}}} \cdot t")
                st.latex(rf"X = {x0} + \frac{{{b}}}{{{mdc}}} \cdot t")
                st.latex(rf"X = {x0} + ({x_coef}) \cdot t")
            
            with col2:
                st.latex(rf"Y = Y_0 - \frac{{a}}{{\text{{mdc}}}} \cdot t")
                st.latex(rf"Y = {y0} - \frac{{{a}}}{{{mdc}}} \cdot t")
                st.latex(rf"Y = {y0} - ({y_coef}) \cdot t")
        
        # Expander: Verificação
        with st.expander("Verificação"):
            v = a * x0 + b * y0
            st.latex(rf"{a} \cdot ({x0}) + {b} \cdot ({y0}) = {v}")
            if v == c:
                st.success("✓ Verificado")
