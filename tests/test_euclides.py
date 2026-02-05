"""
Testes para o algoritmo Euclidiano Estendido.
"""

import pytest
from src.models.euclides import EuclidesModel


class TestEuclidesModel:
    """Testes para EuclidesModel."""
    
    def test_mdc_basico(self):
        """Testa MDC de números simples."""
        model = EuclidesModel(48, 18)
        result = model.solve()
        assert result.metadata["mdc"] == 6
    
    def test_mdc_primos_entre_si(self):
        """Testa MDC de números primos entre si."""
        model = EuclidesModel(17, 13)
        result = model.solve()
        assert result.metadata["mdc"] == 1
    
    def test_mdc_mesmo_numero(self):
        """Testa MDC de um número com ele mesmo."""
        model = EuclidesModel(25, 25)
        result = model.solve()
        assert result.metadata["mdc"] == 25
    
    def test_identidade_bezout(self):
        """Testa se alpha*a + beta*b = mdc (Identidade de Bézout)."""
        model = EuclidesModel(35, 15)
        result = model.solve()
        
        a = result.metadata["original_a"]
        b = result.metadata["original_b"]
        mdc = result.metadata["mdc"]
        alpha = result.metadata["alpha"]
        beta = result.metadata["beta"]
        
        assert alpha * a + beta * b == mdc
    
    def test_ordem_invertida(self):
        """Testa que a ordem dos parâmetros não afeta o resultado."""
        model1 = EuclidesModel(48, 18)
        model2 = EuclidesModel(18, 48)
        
        result1 = model1.solve()
        result2 = model2.solve()
        
        assert result1.metadata["mdc"] == result2.metadata["mdc"]
    
    def test_steps_gerados(self):
        """Testa que os passos intermediários são gerados."""
        model = EuclidesModel(48, 18)
        result = model.solve()
        
        assert len(result.steps) > 0
        assert "resto" in result.steps[0]
        assert "quociente" in result.steps[0]
