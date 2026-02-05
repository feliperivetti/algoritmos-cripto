"""
Módulo responsavel pelo registro centralizado de algoritmos.
"""
from typing import Type

from src.exceptions import AlgorithmNotFoundError
from src.models.base import BaseAlgorithm
from src.views.base_view import BaseView


class AlgorithmRegistry:
    """Registro central de algoritmos."""

    _registry: dict[str, dict[str, Type]] = {}

    @classmethod
    def register(cls, name: str, model_cls: Type[BaseAlgorithm], view_cls: Type[BaseView]) -> None:
        """Registra um novo algoritmo."""
        cls._registry[name] = {
            "model": model_cls,
            "view": view_cls
        }

    @classmethod
    def get(cls, name: str) -> dict[str, Type]:
        """Retorna a configuração de um algoritmo."""
        if name not in cls._registry:
            raise AlgorithmNotFoundError(name)
        return cls._registry[name]

    @classmethod
    def get_all(cls) -> dict[str, dict[str, Type]]:
        """Retorna todos os algoritmos registrados."""
        return cls._registry


def load_algorithms() -> None:
    """
    Carrega e registra todos os algoritmos disponíveis.
    """
    from src.models.achar_fator import AcharFatorModel
    from src.models.diofantina import DiofantinaModel
    from src.models.euclides import EuclidesModel
    from src.models.fermat import FermatModel
    from src.models.modular_exp import ModularExpModel
    from src.models.pseudoprimo_forte import PseudoPrimoForteModel
    from src.models.teorema_chines import TeoremaChinesModel
    from src.views.achar_fator_view import AcharFatorView
    from src.views.diofantina_view import DiofantinaView
    from src.views.euclides_view import EuclidesView
    from src.views.fermat_view import FermatView
    from src.views.modular_exp_view import ModularExpView
    from src.views.pseudoprimo_forte_view import PseudoPrimoForteView
    from src.views.teorema_chines_view import TeoremaChinesView

    AlgorithmRegistry.register("Euclides Estendido", EuclidesModel, EuclidesView)
    AlgorithmRegistry.register("Equação Diofantina", DiofantinaModel, DiofantinaView)
    AlgorithmRegistry.register("Algoritmo de Fermat", FermatModel, FermatView)
    AlgorithmRegistry.register("Exponenciação Modular", ModularExpModel, ModularExpView)
    AlgorithmRegistry.register("Achar um Fator", AcharFatorModel, AcharFatorView)
    AlgorithmRegistry.register("Pseudoprimo Forte", PseudoPrimoForteModel, PseudoPrimoForteView)
    AlgorithmRegistry.register("👲 Teorema Chinês do Resto", TeoremaChinesModel, TeoremaChinesView)
