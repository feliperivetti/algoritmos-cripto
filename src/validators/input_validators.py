from dataclasses import dataclass
from typing import Any

from src.models.base import ParamConfig


@dataclass
class ValidationResult:
    """Resultado de uma validação."""
    is_valid: bool
    value: Any = None
    error_message: str = ""


class InputValidator:
    """Validador unificado para todos os algoritmos."""

    @staticmethod
    def validate_int(value: str, param_name: str) -> ValidationResult:
        """Valida e converte string para inteiro."""
        try:
            return ValidationResult(True, int(value))
        except ValueError:
            return ValidationResult(
                False,
                error_message=f"{param_name} deve ser um número inteiro."
            )

    @classmethod
    def validate_param(cls, raw_value: str, param_config: ParamConfig) -> ValidationResult:
        """
        Valida um parâmetro usando sua configuração.

        1. Converte para inteiro
        2. Aplica todas as validações definidas no ParamConfig
        """
        # Primeiro converte para inteiro
        result = cls.validate_int(raw_value, param_config.label)
        if not result.is_valid:
            return result

        value = result.value

        # Aplica todas as validações do ParamConfig
        for validation_fn in param_config.validations:
            is_valid, error_msg = validation_fn(value)
            if not is_valid:
                return ValidationResult(
                    False,
                    error_message=f"{param_config.label}: {error_msg}"
                )

        return ValidationResult(True, value)

    @classmethod
    def validate_all(
        cls, raw_inputs: dict[str, str], params: list[ParamConfig]
    ) -> tuple[bool, dict]:
        """
        Valida todos os inputs de um algoritmo.

        Retorna (True, {valores_convertidos}) se válido
        Retorna (False, {errors: [lista_de_erros]}) se inválido
        """
        validated = {}
        errors = []

        for param in params:
            if param.name not in raw_inputs or raw_inputs[param.name] == "":
                errors.append(f"O campo {param.label} é obrigatório.")
                continue

            result = cls.validate_param(raw_inputs[param.name], param)

            if not result.is_valid:
                errors.append(result.error_message)
            else:
                validated[param.name] = result.value

        if errors:
            return False, {"errors": errors}

        return True, validated
