"""
Informações e descrições dos algoritmos.

Importa as informações de cada algoritmo dos arquivos separados.
"""

from src.algorithm_info import (
    euclides,
    diofantina,
    fermat,
    modular_exp,
    achar_fator,
    pseudoprimo_forte,
)

ALGORITHM_INFO = {
    "Euclides Estendido": euclides.INFO,
    "Equação Diofantina": diofantina.INFO,
    "Algoritmo de Fermat": fermat.INFO,
    "Exponenciação Modular": modular_exp.INFO,
    "Achar um Fator": achar_fator.INFO,
    "Pseudoprimo Forte": pseudoprimo_forte.INFO,
}


def get_algorithm_info(name: str) -> dict:
    """Retorna as informações do algoritmo."""
    return ALGORITHM_INFO.get(name, {})
