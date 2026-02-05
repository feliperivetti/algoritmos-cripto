"""
Testes para os validadores centralizados.
"""
import pytest
from src.models.validators import (
    validate_non_zero,
    validate_positive,
    validate_greater_than_one,
    validate_odd
)

class TestValidators:
    """Suite de testes para funções de validação."""

    @pytest.mark.parametrize("val, expected", [
        (1, True),
        (-1, True),
        (100, True),
        (0, False)
    ])
    def test_validate_non_zero(self, val, expected):
        is_valid, msg = validate_non_zero(val)
        assert is_valid == expected
        if not expected:
            assert "não pode ser zero" in msg

    @pytest.mark.parametrize("val, expected", [
        (1, True),
        (10, True),
        (0, False),
        (-5, False)
    ])
    def test_validate_positive(self, val, expected):
        is_valid, msg = validate_positive(val)
        assert is_valid == expected
        if not expected:
            assert "deve ser positivo" in msg

    @pytest.mark.parametrize("val, expected", [
        (2, True),
        (10, True),
        (1, False),
        (0, False),
        (-2, False)
    ])
    def test_validate_greater_than_one(self, val, expected):
        is_valid, msg = validate_greater_than_one(val)
        assert is_valid == expected
        if not expected:
            assert "maior que 1" in msg

    @pytest.mark.parametrize("val, expected", [
        (3, True),
        (1, True),
        (-3, True),
        (2, False),
        (0, False),
        (-4, False)
    ])
    def test_validate_odd(self, val, expected):
        is_valid, msg = validate_odd(val)
        assert is_valid == expected
        if not expected:
            assert "deve ser ímpar" in msg
