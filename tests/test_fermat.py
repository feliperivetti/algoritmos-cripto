"""
Testes para o Algoritmo de Fermat.
"""

import pytest
from src.models.fermat import FermatModel


class TestFermatModel:
    """Testes para FermatModel."""
    
    def test_fatoracao_simples(self):
        """Testa fatoração de um número composto."""
        model = FermatModel(15)
        result = model.solve()
        
        f1 = result.metadata["factor1"]
        f2 = result.metadata["factor2"]
        
        # Os fatores multiplicados devem dar n
        assert f1 * f2 == 15
        assert {f1, f2} == {3, 5}
    
    def test_numero_primo(self):
        """Testa detecção de número primo."""
        model = FermatModel(17)
        result = model.solve()
        
        assert result.metadata["is_prime"] is True
    
    def test_fatores_grandes(self):
        """Testa fatoração de número maior."""
        model = FermatModel(221)  # 13 * 17
        result = model.solve()
        
        f1 = result.metadata["factor1"]
        f2 = result.metadata["factor2"]
        
        assert f1 * f2 == 221
        assert {f1, f2} == {13, 17}
    
    def test_quadrado_perfeito(self):
        """Testa um quadrado perfeito."""
        model = FermatModel(49)  # 7 * 7
        result = model.solve()
        
        f1 = result.metadata["factor1"]
        f2 = result.metadata["factor2"]
        
        assert f1 * f2 == 49
