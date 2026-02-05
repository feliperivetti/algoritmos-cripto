"""
Testes para o algoritmo Achar um Fator (Trial Division).
"""

import pytest
from src.models.achar_fator import AcharFatorModel, validate_greater_than_one

class TestAcharFatorModel:
    """Testes para AcharFatorModel."""

    @pytest.mark.parametrize("n, expected, is_prime", [
        # Compostos
        (15, 3, False),   # 3 * 5
        (9, 3, False),    # 3 * 3
        (35, 5, False),   # 5 * 7
        (49, 7, False),   # 7 * 7
        (4, 2, False),    # 2 * 2
        
        # Primos
        (17, 17, True),
        (13, 13, True),
        (2, 2, True),
        (101, 101, True),
    ])
    def test_fatoracao(self, n, expected, is_prime):
        """Testa se encontra um fator ou identifica como primo."""
        model = AcharFatorModel(n)
        result = model.solve()
        
        # O resultado é o fator encontrado ou o próprio N se primo
        assert result.result == expected
        assert result.metadata["is_prime"] == is_prime
        
        # Se não é primo, valida que o resultado realmente divide N
        if not is_prime:
            assert n % result.result == 0
            assert result.result > 1

    @pytest.mark.parametrize("val, valid", [
        (1, False),
        (0, False),
        (-5, False),
        (2, True),
        (10, True)
    ])
    def test_validation(self, val, valid):
        """Testa validação de entrada (n > 1)."""
        is_valid, msg = validate_greater_than_one(val)
        assert is_valid == valid
        if not valid:
            assert msg != ""
