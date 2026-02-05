from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class AlgorithmResult:
    """Resultado padronizado de qualquer algoritmo."""
    steps: list[dict] = field(default_factory=list)
    result: Any = None
    metadata: dict = field(default_factory=dict)


@dataclass
class ParamConfig:
    """Configuração de um parâmetro de entrada."""
    name: str
    label: str
    validations: list[Callable[[int], tuple[bool, str]]] = field(default_factory=list)


class BaseAlgorithm(ABC):
    """Classe base para todos os algoritmos."""

    name: str = "Algoritmo Base"
    description: str = ""
    input_format_latex: str = ""

    @classmethod
    @abstractmethod
    def get_params(cls) -> list[ParamConfig]:
        """Retorna lista de parâmetros com nome, label e validações."""
        pass

    @abstractmethod
    def solve(self) -> AlgorithmResult:
        """Executa o algoritmo e retorna resultado estruturado."""
        pass
