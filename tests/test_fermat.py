"""
Testes para o Algoritmo de Fermat.
"""

import pytest
from src.models.fermat import FermatModel, validate_odd, validate_positive


class TestFermatModel:
    """Testes para FermatModel."""

    @pytest.mark.parametrize("n, expected_factors", [
        (15, {3, 5}),
        (35, {5, 7}),
        (221, {13, 17}),
        (2021, {43, 47}), # 43*47 = 2021. Fatores próximos (Fermat é bom nisso)
    ])
    def test_fatoracao_compostos(self, n, expected_factors):
        """Testa fatoração de números compostos ímpares."""
        model = FermatModel(n)
        result = model.solve()
        
        f1 = result.metadata["factor1"]
        f2 = result.metadata["factor2"]
        
        # Verifica se o produto é N
        assert f1 * f2 == n
        # Verifica se os fatores são os esperados
        assert {f1, f2} == expected_factors
        # Não deve ser identificado como primo (pois f1, f2 != 1 e != n)
        assert result.metadata["is_prime"] is False

    @pytest.mark.parametrize("n, root", [
        (49, 7),
        (81, 9),
        (169, 13),
        (25, 5)
    ])
    def test_quadrados_perfeitos(self, n, root):
        """Testa quadrados perfeitos (N = root * root)."""
        model = FermatModel(n)
        result = model.solve()
        
        f1 = result.metadata["factor1"]
        f2 = result.metadata["factor2"]
        
        assert f1 * f2 == n
        assert f1 == root
        assert f2 == root
        assert result.metadata["is_prime"] is False

    @pytest.mark.parametrize("n", [
        17,
        13,
        101,
        3   # Primo pequeno
    ])
    def test_numeros_primos(self, n):
        """Testa se números primos são identificados corretamente (fator 1 e N)."""
        model = FermatModel(n)
        result = model.solve()
        
        f1 = result.metadata["factor1"]
        f2 = result.metadata["factor2"]
        is_prime = result.metadata["is_prime"]
        
        assert f1 * f2 == n
        assert {f1, f2} == {1, n}
        assert is_prime is True

    @pytest.mark.parametrize("value, expected_valid", [
        (3, True),
        (5, True),
        (4, False), # Par
        (10, False), # Par
        (0, False) # Par
    ])
    def test_validate_odd(self, value, expected_valid):
        """Testa validador de número ímpar."""
        is_valid, msg = validate_odd(value)
        assert is_valid == expected_valid

    @pytest.mark.parametrize("value, expected_valid", [
        (10, True),
        (1, True),
        (0, False),
        (-5, False)
    ])
    def test_validate_positive(self, value, expected_valid):
        """Testa validador de número positivo."""
        is_valid, msg = validate_positive(value)
        assert is_valid == expected_valid
