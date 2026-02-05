"""
Testes para o algoritmo Euclidiano Estendido.
"""

import pytest

from src.models.euclides import EuclidesModel, validate_non_zero


class TestEuclidesModel:
    """Testes para EuclidesModel."""

    @pytest.mark.parametrize("a, b, expected_mdc", [
        # Casos Básicos
        (48, 18, 6),
        (18, 48, 6),  # Ordem invertida
        (17, 13, 1),  # Primos entre si
        (100, 20, 20), # Um múltiplo do outro

        # Casos de Borda
        (25, 25, 25), # Mesmo número
        (500, 1, 1),  # Com 1
        (1, 500, 1),

        # Números Negativos (MDC deve ser positivo)
        (-48, 18, 6),
        (48, -18, 6),
        (-48, -18, 6),

        # Casos Maiores
        (123456, 7890, 6),
        (1071, 462, 21),
    ])
    def test_mdc_variados(self, a, b, expected_mdc):
        """Testa o cálculo do MDC para diversos cenários."""
        model = EuclidesModel(a, b)
        result = model.solve()

        # Verificações básicas
        assert result.metadata["mdc"] == expected_mdc
        assert result.result == expected_mdc

        # Validação da Identidade de Bézout: alpha*orig_a + beta*orig_b = mdc
        alpha = result.metadata["alpha"]
        beta = result.metadata["beta"]
        orig_a = result.metadata["original_a"]
        orig_b = result.metadata["original_b"]

        assert alpha * orig_a + beta * orig_b == expected_mdc

    @pytest.mark.parametrize("valor, expected_valid", [
        (0, False),
        (1, True),
        (-1, True),
        (100, True)
    ])
    def test_validacao_zero(self, valor, expected_valid):
        """Testa a função de validação de não-zero."""
        is_valid, msg = validate_non_zero(valor)
        assert is_valid == expected_valid
        if not expected_valid:
            assert msg != ""

    def test_fibonacci_stress(self):
        """
        Testa com números de Fibonacci consecutivos (Pior caso para Euclides).
        MDC(F_n, F_{n-1}) = 1.
        """
        # F_20 = 6765, F_19 = 4181
        a, b = 6765, 4181
        model = EuclidesModel(a, b)
        result = model.solve()

        assert result.metadata["mdc"] == 1

        # Identidade de Bézout
        alpha = result.metadata["alpha"]
        beta = result.metadata["beta"]
        assert alpha * a + beta * b == 1

    def test_steps_structure(self):
        """Verifica se os passos são gerados com a estrutura correta."""
        model = EuclidesModel(48, 18)
        result = model.solve()

        assert len(result.steps) > 0
        step = result.steps[0]
        assert "resto" in step
        assert "quociente" in step
        assert "x" in step
        assert "y" in step
