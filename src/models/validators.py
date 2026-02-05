"""
Módulo centralizado de validadores para os modelos criptográficos.
"""

def validate_non_zero(value: int) -> tuple[bool, str]:
    """Valida que o valor não seja zero."""
    if value == 0:
        return False, "O valor não pode ser zero."
    return True, ""

def validate_positive(value: int) -> tuple[bool, str]:
    """Valida que o valor seja estritamente positivo (> 0)."""
    if value <= 0:
        return False, "O valor deve ser positivo."
    return True, ""

def validate_greater_than_one(value: int) -> tuple[bool, str]:
    """Valida que o valor seja maior que 1."""
    if value <= 1:
        return False, "O valor deve ser maior que 1."
    return True, ""

def validate_odd(value: int) -> tuple[bool, str]:
    """Valida que o valor seja ímpar."""
    if value % 2 == 0:
        return False, "O valor deve ser ímpar."
    return True, ""
