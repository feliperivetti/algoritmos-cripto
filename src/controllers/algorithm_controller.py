from typing import Type
import streamlit as st

from src.models.base import BaseAlgorithm
from src.models.euclides import EuclidesModel
from src.models.diofantina import DiofantinaModel
from src.models.fermat import FermatModel
from src.models.modular_exp import ModularExpModel
from src.models.achar_fator import AcharFatorModel
from src.models.pseudoprimo_forte import PseudoPrimoForteModel

from src.views.base_view import BaseView
from src.views.euclides_view import EuclidesView
from src.views.diofantina_view import DiofantinaView
from src.views.fermat_view import FermatView
from src.views.modular_exp_view import ModularExpView
from src.views.achar_fator_view import AcharFatorView
from src.views.pseudoprimo_forte_view import PseudoPrimoForteView

from src.validators.input_validators import InputValidator


# Registry de algoritmos: mapeia nome → (Model, View)
ALGORITHMS: dict[str, dict[str, Type]] = {
    "Euclides Estendido": {
        "model": EuclidesModel,
        "view": EuclidesView,
    },
    "Equação Diofantina": {
        "model": DiofantinaModel,
        "view": DiofantinaView,
    },
    "Algoritmo de Fermat": {
        "model": FermatModel,
        "view": FermatView,
    },
    "Exponenciação Modular": {
        "model": ModularExpModel,
        "view": ModularExpView,
    },
    "Achar um Fator": {
        "model": AcharFatorModel,
        "view": AcharFatorView,
    },
    "Pseudoprimo Forte": {
        "model": PseudoPrimoForteModel,
        "view": PseudoPrimoForteView,
    },
}


class AlgorithmController:
    """Controller que orquestra a execução entre Model e View."""
    
    def __init__(self, algorithm_name: str):
        if algorithm_name not in ALGORITHMS:
            raise ValueError(f"Algoritmo desconhecido: {algorithm_name}")
        
        config = ALGORITHMS[algorithm_name]
        self.model_class: Type[BaseAlgorithm] = config["model"]
        self.view_class: Type[BaseView] = config["view"]
        self.algorithm_name = algorithm_name
    
    @property
    def params(self):
        """Retorna os parâmetros do modelo."""
        return self.model_class.get_params()
    
    @property
    def input_format_latex(self):
        """Retorna o formato de entrada em LaTeX."""
        return self.model_class.input_format_latex
    
    def validate_inputs(self, raw_inputs: dict[str, str]) -> tuple[bool, dict]:
        """Valida todos os inputs usando o validador unificado."""
        return InputValidator.validate_all(raw_inputs, self.params)
    
    def execute(self, raw_inputs: dict[str, str]) -> None:
        """
        Valida, executa e renderiza o algoritmo.
        
        Este é o método principal que:
        1. Valida os inputs
        2. Instancia o Model com os valores validados
        3. Executa o algoritmo
        4. Renderiza o resultado via View
        """
        # Validação
        is_valid, result = self.validate_inputs(raw_inputs)
        
        if not is_valid:
            for error in result.get("errors", []):
                st.error(error)
            return
        
        # Execução do Model
        model = self.model_class(**result)
        algorithm_result = model.solve()
        
        # Renderização via View
        view = self.view_class()
        view.render(algorithm_result)
