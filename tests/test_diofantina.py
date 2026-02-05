"""
Testes para a Equação Diofantina.
"""

import pytest
from src.models.diofantina import DiofantinaModel


class TestDiofantinaModel:
    """Testes para DiofantinaModel."""
    
    def test_solucao_existe(self):
        """Testa uma equação diofantina com solução."""
        model = DiofantinaModel(35, 15, 5)
        result = model.solve()
        
        assert result.metadata["has_solution"] is True
        assert result.metadata["x0"] is not None
        assert result.metadata["y0"] is not None
    
    def test_verifica_solucao_particular(self):
        """Testa que a solução particular satisfaz a equação."""
        a, b, c = 35, 15, 5
        model = DiofantinaModel(a, b, c)
        result = model.solve()
        
        x0 = result.metadata["x0"]
        y0 = result.metadata["y0"]
        
        # a*x0 + b*y0 deve ser igual a c
        assert a * x0 + b * y0 == c
    
    def test_sem_solucao(self):
        """Testa uma equação diofantina sem solução."""
        # 6x + 9y = 5 não tem solução (5 não é divisível por MDC(6,9)=3)
        model = DiofantinaModel(6, 9, 5)
        result = model.solve()
        
        assert result.metadata["has_solution"] is False
    
    def test_coeficientes_solucao_geral(self):
        """Testa que os coeficientes da solução geral estão corretos."""
        model = DiofantinaModel(35, 15, 5)
        result = model.solve()
        
        mdc = result.metadata["mdc"]
        x_coef = result.metadata["x_coef"]
        y_coef = result.metadata["y_coef"]
        
        # X = x0 + (b/mdc) * t
        assert x_coef == 15 // mdc
        # Y = y0 - (a/mdc) * t
        assert y_coef == 35 // mdc
