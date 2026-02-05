"""
Testes para os validadores de input.
"""

import pytest
from src.validators.input_validators import InputValidator, ValidationResult
from src.models.base import ParamConfig


class TestInputValidator:
    """Testes para InputValidator."""
    
    def test_validate_int_valido(self):
        """Testa conversão de inteiro válido."""
        result = InputValidator.validate_int("42", "N")
        
        assert result.is_valid is True
        assert result.value == 42
    
    def test_validate_int_invalido(self):
        """Testa rejeição de não-inteiro."""
        result = InputValidator.validate_int("abc", "N")
        
        assert result.is_valid is False
        assert "inteiro" in result.error_message.lower()
    
    def test_validate_int_negativo(self):
        """Testa que inteiros negativos são aceitos."""
        result = InputValidator.validate_int("-5", "N")
        
        assert result.is_valid is True
        assert result.value == -5
    
    def test_validate_param_com_validacoes(self):
        """Testa validação com múltiplas funções de validação."""
        def validate_positive(v):
            return (v > 0, "Deve ser positivo")
        
        param = ParamConfig(
            name="n",
            label="N",
            validations=[validate_positive]
        )
        
        # Válido
        result = InputValidator.validate_param("5", param)
        assert result.is_valid is True
        
        # Inválido
        result = InputValidator.validate_param("-5", param)
        assert result.is_valid is False
    
    def test_validate_all_sucesso(self):
        """Testa validação de múltiplos parâmetros."""
        params = [
            ParamConfig(name="a", label="A", validations=[]),
            ParamConfig(name="b", label="B", validations=[]),
        ]
        
        raw_inputs = {"a": "10", "b": "20"}
        is_valid, result = InputValidator.validate_all(raw_inputs, params)
        
        assert is_valid is True
        assert result["a"] == 10
        assert result["b"] == 20
    
    def test_validate_all_campo_vazio(self):
        """Testa rejeição de campo vazio."""
        params = [
            ParamConfig(name="a", label="A", validations=[]),
        ]
        
        raw_inputs = {"a": ""}
        is_valid, result = InputValidator.validate_all(raw_inputs, params)
        
        assert is_valid is False
        assert "errors" in result
