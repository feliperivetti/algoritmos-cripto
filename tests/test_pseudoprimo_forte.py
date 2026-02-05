import pytest

from src.models.pseudoprimo_forte import PseudoPrimoForteModel
from src.models.validators import validate_odd


class TestPseudoPrimoForteModel:
    """Testes para PseudoPrimoForteModel."""

    @pytest.mark.parametrize(
        "n, b, expected_result",
        [
            # Primos verdadeiros (Devem retornar True para qualquer base)
            (17, 3, True),
            (13, 2, True),
            (101, 5, True),
            # Compostos (Devem retornar False geralmente)
            (15, 2, False),  # 15 = 3 * 5
            (9, 2, False),  # 9 = 3 * 3
            (35, 2, False),  # 35 = 5 * 7
            # Pseudoprimo Forte (Edge Case: Composto que passa no teste para base específica)
            # 2047 = 23 * 89.
            # 2^2046 mod 2047 = 1.
            (2047, 2, True),
        ],
    )
    def test_pseudoprimo(self, n, b, expected_result):
        """Testa verificação de pseudoprimo forte."""
        model = PseudoPrimoForteModel(n, b)
        result = model.solve()

        assert result.result == expected_result
        assert result.metadata["is_strong_pseudoprime"] == expected_result
        assert result.metadata["b"] == b
        assert result.metadata["n"] == n

    @pytest.mark.parametrize(
        "n, b, expected_error_msg",
        [
            (15, 15, "B (15) não pode ser múltiplo de N (15)"),  # B multiplo de N
            (15, 30, "B (30) não pode ser múltiplo de N (15)"),  # B multiplo de N
        ],
    )
    def test_validation_logic_in_solve(self, n, b, expected_error_msg):
        """Testa validações específicas dentro do método solve (ex: b multiplo de n)."""
        model = PseudoPrimoForteModel(n, b)
        result = model.solve()

        # Verifica se retornou erro
        assert result.result is None
        assert result.metadata.get("error") is True
        assert expected_error_msg in result.metadata["error_message"]

    @pytest.mark.parametrize(
        "val, valid",
        [
            (3, True),  # Ímpar
            (2, False),  # Par
            (10, False),  # Par
            (0, False),  # Par
        ],
    )
    def test_validate_odd(self, val, valid):
        """Testa validador de número ímpar (n deve ser ímpar para Miller-Rabin)."""
        is_valid, msg = validate_odd(val)
        assert is_valid == valid
